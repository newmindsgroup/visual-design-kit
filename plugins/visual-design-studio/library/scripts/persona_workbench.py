"""Build a dependency-free private persona workbench from complete canonical records."""
# Version-Timestamp: 2026-10-22 08:20:00 AST
import argparse
import base64
import copy
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import re
import sys

LIBRARY = Path(__file__).resolve().parents[1]
ASSETS = LIBRARY / 'draft-skills/design-persona-build/assets'
DEFINITIONS = json.loads((LIBRARY / 'templates/persona-fields.json').read_text())['fields']
COMPONENTS = json.loads((LIBRARY / 'templates/persona-components.json').read_text())['components']
FIELD_SET = {f['path'] for f in DEFINITIONS}
sys.path.insert(0,str(LIBRARY))
from design_system.validation import Check, persona as validate_persona



def validate(data, project_root=None):
    errors = []
    records = data.get('records') if isinstance(data, dict) else None
    if not isinstance(records, list) or not records:
        return ['records must be a nonempty array']
    ids = [r.get('record_id') for r in records if isinstance(r, dict)]
    if len(ids) != len(records) or not all(isinstance(i,str) and re.fullmatch(r'[A-Za-z0-9_-]+',i) for i in ids) or len(set(ids)) != len(ids):
        errors.append('record IDs must be unique safe strings')
    for index, record in enumerate(records):
        if not isinstance(record,dict):continue
        fields = record.get('fields',{})
        if not isinstance(fields,dict) or set(fields) != FIELD_SET:
            errors.append(f'record {index}: exact 118 fields required');continue
        for key, field in fields.items():
            if not isinstance(field,dict) or not all(k in field for k in ['value','status','reason']):
                errors.append(f'{index}/{key}: value, status and reason required')
            elif not isinstance(field['status'],str) or not field['status'] or not isinstance(field['reason'],str) or not field['reason']:
                errors.append(f'{index}/{key}: meaningful status/reason required')
            elif field['value'] is None and field['status'] not in ['unknown','not_applicable','not-applicable']:
                errors.append(f'{index}/{key}: null value must remain unknown or not applicable')
        for key, field in fields.items():
            if not isinstance(field,dict):continue
            translations=field.get('translations',{})
            if not isinstance(translations,dict):errors.append(f'{index}/{key}: translations must be an object');continue
            for locale, translation in translations.items():
                if locale not in {'en','es'} or not isinstance(translation,dict) or 'value' not in translation or translation['value'] is None:
                    errors.append(f'{index}/{key}: translation must declare en/es and a known value');continue
                value=translation['value']
                if '[].' in key:
                    if not isinstance(value,list) or not value or any(not isinstance(x,dict) or not isinstance(x.get('item_id'),str) or not isinstance(x.get('text'),str) for x in value):
                        errors.append(f'{index}/{key}: translated object items require item_id and text');continue
                    source_ids={x['item_id'] for x in field['value'] or [] if isinstance(x,dict) and 'item_id' in x}
                    if {x['item_id'] for x in value} != source_ids:errors.append(f'{index}/{key}: translated item linkage differs')
                elif '[]' in key:
                    if not isinstance(value,list) or not value or any(not isinstance(x,str) or not x for x in value):errors.append(f'{index}/{key}: translated scalar list required')
                elif not isinstance(value,str) or not value:errors.append(f'{index}/{key}: translated text required')
        if not isinstance(record.get('components'),dict) or set(record.get('components',{})) != {c['id'] for c in COMPONENTS}:
            errors.append(f'record {index}: all 35 components required')
        check=Check(project_root or Path.cwd(),None)
        validate_persona(check,record)
        errors.extend(f"record {index}/{item['path']}: {item['message']}" for item in check.errors)
    theme=data.get('theme',{})
    if not isinstance(theme,dict) or any(k not in {'accent','ink','ground','surface','border'} or not isinstance(v,str) or not re.fullmatch(r'#[0-9a-fA-F]{6}',v) for k,v in theme.items()):
        errors.append('theme accepts only five named six-digit hex colors')
    mapping=data.get('mapping',{})
    if not isinstance(mapping,dict):return errors+['mapping must be an object']
    pages=mapping.get('pages',[])
    if not isinstance(pages,list):return errors+['mapping pages must be an array']
    seen=set()
    for page in pages:
        if not isinstance(page,dict):errors.append('mapping page must be an object');continue
        path=page.get('path')
        if not isinstance(path,str) or not path.startswith('/') or path.startswith('//') or path in seen:
            errors.append('mapping paths must be unique local paths')
        if isinstance(path,str):seen.add(path)
        assigned=[]
        for k in ['primary_ids','secondary_ids','tertiary_ids']:
            value=page.get(k,[])
            if not isinstance(value,list):errors.append('mapping role IDs must be arrays');continue
            assigned.extend(i for i in value if isinstance(i,str))
            if any(i not in ids for i in value):errors.append('unknown mapping persona reference')
        if len(assigned)!=len(set(assigned)):errors.append('persona cannot occupy multiple priorities on the same page')
        weights=page.get('weights_by_persona',{})
        if not isinstance(weights,dict):errors.append('mapping weights must be an object');continue
        for key,value in weights.items():
            if key not in assigned:errors.append('weighted persona must have a page priority assignment')
            if key not in ids or isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
                errors.append('mapping weights must be finite nonnegative numbers for known IDs')
        numeric=[value for value in weights.values() if isinstance(value,(int,float)) and not isinstance(value,bool)]
        if not math.isfinite(sum(numeric)):errors.append('mapping weight total must remain finite')
    sections=mapping.get('sections',[])
    if not isinstance(sections,list):errors.append('mapping sections must be an array')
    else:
        for section in sections:
            if not isinstance(section,dict):errors.append('mapping section must be an object');continue
            usage=section.get('persona_usage',section.get('personaUsage',[]))
            if not isinstance(usage,list) or any(i not in ids+['primary','secondary','tertiary','all'] for i in usage):
                errors.append('section usage must reference known personas or explicit priority roles')
    return errors


def demo_collection():
    """Original fictional repair-service planning fixture. Never research evidence."""
    template=json.loads((LIBRARY/'templates/persona-record.json').read_text())
    records=[]
    names=['Service business owner','Operations coordinator','Digital delivery evaluator']
    for n,name in enumerate(names,1):
        record=copy.deepcopy(template);pid=f'demo-{n}'
        record.update(record_id=pid,owner='Fictional demonstration team',scope='Illustrative planning fixture only',persona_status='fictional example, not research')
        for key,field in record['fields'].items():
            field.update(value=None,status='unknown',reason='No evidence supplied; do not infer personal details.',evidence=[])
        def put(key,value):
            record['fields'][key].update(value=value,status='synthetic',reason='Original fictional example, not an interview finding.',confidence='not research',evidence=[])
        for key,value in {'id':pid,'name':name,'shortName':['Owner','Coordinator','Evaluator'][n-1],'priority':['primary','secondary','secondary'][n-1],'demographics.role':name,'demographics.company':'Fictional repair-service organization','demographics.industry':'Local services','jtbd':['Choose a coherent service partner without disrupting day-to-day work.','Make inquiries and handoffs dependable for the team.','Understand whether the proposed experience is maintainable.'][n-1]}.items():put(key,value)
        # Every domain has deliberately substantive fixture content, without invented personal biography.
        content={
          'goals[]':['Make service information clear before a customer calls','Reduce avoidable handoffs','Keep ownership clear after launch'],
          'frustrations[]':['Repeatedly explaining the same service boundaries','Losing the context between teams','Not knowing who owns a failed handoff'],
          'behaviors[]':['Compares scope and evidence before booking a discussion','Shares relevant information with another reviewer','Returns to the process page to check responsibilities'],
          'psychographics.values[]':['Clarity','Responsible ownership','Respect for the customer'],
          'psychographics.attitudes':'Prefers a useful bounded improvement to an untested promise.',
          'psychographics.motivations[]':['Give the team a system they can operate','Make customer requests easier to understand'],
          'psychographics.fears[]':['Introducing a fragile dependency','Making a change without a recovery path'],
          'dayInTheLife.workActivities[]':['Reviews open requests','Checks handoffs with colleagues','Resolves unclear service questions'],
          'dayInTheLife.challenges[]':['Interruptions while evaluating detailed information','Different stakeholders need different levels of detail'],
          'dayInTheLife.interactionPoints[]':['Service information','Internal review','Project conversation'],
          'buyingJourney.awareness.triggers[]':['Repeated customer confusion','A planned service update'],
          'buyingJourney.awareness.questions[]':['Which kind of help fits?','What evidence should I inspect?'],
          'buyingJourney.awareness.channels[]':['Referral','Direct visit'],
          'buyingJourney.awareness.contentNeeds[]':['A clear service explanation','Relevant examples'],
          'buyingJourney.consideration.evaluationCriteria[]':['Scope clarity','Maintainability','Relevant delivered work'],
          'buyingJourney.consideration.criteria[]':['Scope clarity','Ownership','Recovery'],
          'buyingJourney.consideration.comparisons[]':['Improve internally','Use an existing vendor','Find a specialist'],
          'buyingJourney.consideration.objections[]':['How much disruption does the change introduce?'],
          'buyingJourney.consideration.contentNeeds[]':['Scope and limitations','Actual responsibilities'],
          'buyingJourney.decision.finalTriggers[]':['Reviewers agree on a bounded next step'],
          'buyingJourney.decision.barriers[]':['Unclear responsibilities','No verified recovery plan'],
          'buyingJourney.decision.factors[]':['Relevant evidence','Feasible handoff'],
          'buyingJourney.decision.stakeholders[]':['Business lead','Operations reviewer','Technical evaluator'],
          'buyingJourney.decision.contentNeeds[]':['What happens next','Who owns each step'],
          'influences.sources[]':['Actual previous work','A trusted colleague'],
          'influences.decisionFactors[]':['Responsibility','Scope','Evidence'],
          'influences.influencers[]':['A colleague responsible for operating the result'],
          'influences.peerInfluence':'An experienced colleague can help evaluate the scope.',
          'decisionCriteria.mustHaves[]':['Clear scope and limits','An accountable handoff'],
          'decisionCriteria.niceToHaves[]':['Reusable content and components'],
          'decisionCriteria.dealBreakers[]':['Unsupported guarantees','No meaningful recovery path'],
          'decisionCriteria.priorityOrder[]':['Fit','Evidence','Ownership'],
          'contentPreferences.formats[]':['Concise overview','Detailed scope','Real examples'],
          'contentPreferences.channels[]':['Website','Project conversation'],
          'contentPreferences.tone':'Direct, respectful and specific.',
          'contentPreferences.topics[]':['Service boundaries','Delivery responsibilities','Maintenance'],
          'contentPreferences.avoidTopics[]':['Unsupported claims and jargon'],
          'contentPreferences.readingLevel':'Plain-language demonstration requirement, not a measured preference.',
          'contentPreferences.length':'Overview with optional detailed sections.',
          'communicationStyle.persuasionStyle':'Explain the tradeoff and show relevant evidence.',
          'communicationStyle.proofPoints[]':['A real delivered example','A clear responsibility map'],
          'communicationStyle.keyPhrases[]':['What your team receives','How the handoff works'],
          'communicationStyle.languageLevel':'Plain professional language.',
          'communicationStyle.formality':'Approachable and professional.',
          'communicationStyle.avoidPhrases[]':['Unsupported promises'],
          'successMetrics.winDefinition':'Identify a feasible next step and who is responsible.',
          'successMetrics.personalSuccess[]':['Can explain the proposed next step'],
          'successMetrics.professionalSuccess[]':['Team understands the handoff'],
          'successMetrics.kpis[]':['Task completion','Unresolved questions','Wrong turns'],
          'technologyUsage.devices[]':['Test desktop and mobile as conditions, not claimed personal ownership'],
          'technologyUsage.digitalBehavior':'Verify with actual users; this fixture demonstrates the field.',
          'competitiveContext.alternatives[]':['Existing vendor','Internal improvements','No action'],
          'competitiveContext.currentSolutions[]':['Separate service and inquiry tools'],
          'competitiveContext.switchingBarriers[]':['Working processes must continue during change']}
        for k,v in content.items():put(k,v)
        for stage in ['beforeEngagement','duringConsideration','atDecision','afterPurchase']:
            put('emotionalJourney.'+stage+'.mindset','Illustrative scenario: wants clarity before committing to a next step.')
            put('emotionalJourney.'+stage+'.emotions[]',['Illustrative uncertainty, not a psychological observation'])
            put('emotionalJourney.'+stage+'.needs[]',['Specific evidence and a clear next action'])
        put('emotionalJourney.duringConsideration.concerns[]',['Will the result be operable?'])
        put('emotionalJourney.afterPurchase.desiredEmotions[]',['Illustrative confidence through clear ownership'])
        put('emotionalJourney.afterPurchase.successIndicators[]',['Can operate the delivered result'])
        for stage in ['awareness','consideration','decision','retention']:put('contentMapping.'+stage+'[]',['Relevant evidence','Scope and responsibilities','A useful next action'])
        for prefix,items in {'painPoints':[{'pain':'Context is lost between inquiry and delivery','urgency':'unknown','impact':'unknown','currentWorkaround':'Manual clarification between teams','desiredSolution':'A clear responsible handoff'}], 'objections':[{'objection':'How will this affect working processes?','category':'delivery confidence','response':'Describe verified scope, staged change and responsibilities.','proofNeeded':'Actual handoff and recovery evidence'}], 'scenarios':[{'name':'Evaluate a service partner','description':'Compare scope, proof and responsibilities across two alternatives.','trigger':'Repeated confusion in customer requests','outcome':'Agree a bounded next conversation'}], 'competitiveContext.competitorPerceptions':[{'competitor':'Generic alternative, not a named company','perception':'Evaluate against actual constraints; no market claim'}]}.items():
            for suffix in items[0]:put(prefix+'[].'+suffix,[{'item_id':pid+'-'+prefix+'-1','text':item[suffix]} for item in items])
        for c in record['components'].values():c.update(status='represented',presentation='working data-driven workbench; actual acceptance separately recorded')
        record['ai_extensions']['localization']['source_locale']='en'
        record['ai_extensions'].update(role_type='illustrative buyer/operator/evaluator',approval='none',use_scope='Fictional demonstration only',traceability=[{'need_id':pid+'-N1','use_case_id':pid+'-U1','requirement_id':pid+'-R1','decision_id':'proposed','criterion_id':pid+'-A1','need':'Understand the service','use_case':'Evaluate a feasible next step','requirement':'Clear scope and ownership','decision':'Proposed profile presentation','criterion':'Review actual task completion'}],validation_plan='Replace illustrative content with authorized research and validate the decisions.',refresh_owner='Project owner',refresh_trigger='New research or changed scope')
        records.append(record)
    return {'version_timestamp':datetime.now(timezone.utc).isoformat(),'title':'Persona research workbench','subtitle':'A complete profile, with the evidence in view.','status':'Original fictional demonstration. No research or design approval implied.','records':records,'mapping':{'pages':[{'page_id':'services','label':'Services','path':'/services/','primary_ids':['demo-1'],'secondary_ids':['demo-2'],'tertiary_ids':['demo-3'],'weights_by_persona':{'demo-1':50,'demo-2':30,'demo-3':20},'buying_stage':'consideration','rationale':'Illustrative planning weights, not measured audience shares.'},{'page_id':'contact','label':'Contact','path':'/contact/','primary_ids':['demo-2'],'secondary_ids':['demo-1'],'tertiary_ids':[],'weights_by_persona':{},'buying_stage':'decision','rationale':'Unweighted example; no percentages invented.'}],'sections':[{'section_type':'Service explanation','strategy':'clear scope','persona_usage':['demo-1','demo-2','demo-3'],'guidance':'Define responsibilities and limits before asking for a commitment.'}],'legend':'Project-specific planning priorities; weights are not measured traffic or a universal rule.'}}


def _get_nested(data, path):
    for part in path.split('.'):
        if not isinstance(data,dict) or part not in data:return None
        data=data[part]
    return data


def from_legacy(legacy, targeting=None, source_locale='es'):
    """Normalize nested persona data without accepting its factual claims as research."""
    if not isinstance(legacy,dict) or not isinstance(legacy.get('personas'),list):
        raise ValueError('legacy input requires a personas array')
    skeleton=json.loads((LIBRARY/'templates/persona-record.json').read_text())
    records=[]
    for index, source in enumerate(legacy['personas']):
        if not isinstance(source,dict):raise ValueError('legacy persona must be an object')
        record=copy.deepcopy(skeleton);pid=source.get('id',f'import-{index+1}')
        record.update(record_id=pid,owner='Project owner, verify',scope='Imported reference; factual/research status unverified',persona_status='imported reference, not independently validated')
        sources=[('source',source)]+list((source.get('translations') or {}).items())
        for definition in DEFINITIONS:
            path=definition['path'];field=record['fields'][path]
            field.update(value=None,status='unknown',reason='Absent from supplied source. Do not invent a value.',evidence=[])
            for locale, content in sources:
                value=None
                if '[].' in path:
                    prefix,suffix=path.split('[].',1);items=_get_nested(content,prefix)
                    if isinstance(items,dict) and prefix=='competitiveContext.competitorPerceptions':
                        items=[{'competitor':key,'perception':v} for key,v in items.items()]
                    if isinstance(items,list):
                        value=[{'item_id':f'{pid}-{prefix}-{i+1}','text':str(_get_nested(item,suffix))} for i,item in enumerate(items) if _get_nested(item,suffix) is not None]
                        if not value:value=None
                else:value=_get_nested(content,path.removesuffix('[]'))
                if value is None or value==[]:continue
                if '[]' not in path:value=str(value)
                if locale=='source':field.update(value=value,status='proposed',confidence='unverified source wording',reason='Supplied reference wording; not independently validated research or participant quotation.',evidence=[])
                else:field.setdefault('translations',{})[locale]={'value':value,'status':'imported-unverified','reason':'Supplied translated content, not independently reviewed.'}
        record['ai_extensions'].update(traceability=[{'need':'Represent the supplied profile without loss','use_case':'Review profile content and evidence','requirement':'Retain known fields and explicit unknowns','decision':'Proposed import into workbench','criterion':'Field and content parity plus owner review'}],role_type='Source role, verify actual decision authority',use_scope=record['scope'],approval='Visual reference selected by owner; factual research approval not established',validation_plan='Check claims, quotes, permissions and observed behavior before research use.',refresh_owner='Project owner',refresh_trigger='Changed source or research findings',localization={'source_locale':source_locale,'requested_locales':['es','en'],'translation_status':'Preserve supplied partial translations; label fallback'})
        records.append(record)
    mapping={'pages':[],'sections':[],'legend':'Imported project planning weights, not audience measurements or universal thresholds.'}
    if targeting:
        for page_id,page in targeting.get('pages',{}).items():
            mapping['pages'].append({'page_id':page_id,'label':page.get('label',page_id),'path':page.get('path','/' if page_id=='home' else '/'+page_id+'/'),'primary_ids':page.get('primary',[]),'secondary_ids':page.get('secondary',[]),'tertiary_ids':page.get('tertiary',[]),'weights_by_persona':page.get('weights',{}),'buying_stage':page.get('buyingStage','unknown'),'rationale':page.get('notes','Imported mapping; verify intended use')})
        for key,value in targeting.get('sections',{}).items():
            mapping['sections'].append({'section_type':key,**value})
    return {'version_timestamp':datetime.now(timezone.utc).isoformat(),'source_locale':source_locale,'title':'Persona reference workbench','subtitle':'Complete profiles, comparison and page mapping','status':'Owner-selected visual reference. Imported content retains unverified research status.','records':records,'mapping':mapping}


def build(data, target, portrait_root=None, project_root=None):
    errors=validate(data,project_root)
    if errors:raise ValueError('; '.join(errors))
    target=Path(target)
    if target.exists():raise FileExistsError(target)
    portraits={}
    if portrait_root:
        asset_root=Path(portrait_root).resolve(strict=True)
        for record in data['records']:
            value=record['fields']['image']['value']
            if not value:continue
            if not isinstance(value,str) or ':' in value:raise ValueError('portraits must be explicit local raster paths')
            source=(asset_root/value.lstrip('/')).resolve()
            if not source.is_relative_to(asset_root):raise ValueError('portrait escapes authorized asset root')
            content=source.read_bytes()
            if len(content)>10*1024*1024:raise ValueError('portrait exceeds 10MiB')
            if content.startswith(b'\x89PNG\r\n\x1a\n'):mime='image/png'
            elif content.startswith(b'\xff\xd8\xff'):mime='image/jpeg'
            elif content.startswith(b'RIFF') and content[8:12]==b'WEBP':mime='image/webp'
            else:raise ValueError('portrait must be PNG, JPEG or WebP; active SVG is not accepted')
            portraits[record['record_id']]='data:'+mime+';base64,'+base64.b64encode(content).decode()
    payload={'collection':data,'definitions':DEFINITIONS,'components':COMPONENTS,'portraits':portraits}
    encoded=json.dumps(payload,ensure_ascii=False,allow_nan=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    html=(ASSETS/'workbench.html').read_text().replace('/* WORKBENCH_CSS */',(ASSETS/'workbench.css').read_text()).replace('/* WORKBENCH_JS */',(ASSETS/'workbench.js').read_text()).replace('PERSONA_DATA_JSON',encoded)
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('x',encoding='utf-8') as output:output.write(html)
    return {'output':str(target),'records':len(data['records']),'fields_per_record':118,'components_per_record':35,'version_timestamp':datetime.now(timezone.utc).isoformat(),'limits':['Structure is not research validation','Human presentation approval separate','Browser print/PDF destination requires local user choice']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    source=parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--input',type=Path);source.add_argument('--demo',action='store_true');source.add_argument('--legacy-input',type=Path)
    parser.add_argument('--targeting',type=Path)
    parser.add_argument('--source-locale',choices=['es','en'],help='Declared source language for legacy input; required with --legacy-input')
    parser.add_argument('--portrait-root',type=Path,help='Explicit authorized local raster-asset root; no network image fetch')
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--project-root',type=Path,help='Authorized root used by canonical evidence/path validation; defaults to current directory')
    args=parser.parse_args()
    try:
        if args.legacy_input and not args.source_locale:raise ValueError('--source-locale is required for legacy input')
        data=demo_collection() if args.demo else (from_legacy(json.loads(args.legacy_input.read_text()),json.loads(args.targeting.read_text()) if args.targeting else None,args.source_locale) if args.legacy_input else json.loads(args.input.read_text()))
        print(json.dumps(build(data,args.output,args.portrait_root,args.project_root),indent=2));return 0
    except (ValueError,OSError,TypeError) as error:
        print(json.dumps({'status':'failed','error':str(error)}));return 1

if __name__=='__main__':raise SystemExit(main())
