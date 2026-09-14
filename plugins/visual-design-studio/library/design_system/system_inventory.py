"""Consistency checks for the original inventory, not component acceptance."""
# Version-Timestamp: 2026-09-07 14:00:59 AST
import re
from urllib.parse import urlsplit
from .reference_decision import structure, check_schema

PROFILES = {'brand','website','web-app','native-phone','native-tablet','marketing-sales','display','touch'}
CATEGORIES = {'foundations','ui','patterns','templates','assets','governance'}
STATE_MINIMUM = {
    'none':{'default'}, 'action':{'default','focus','pressed','unavailable'},
    'input':{'default','focus','filled','invalid'}, 'selection':{'default','focus','selected','unavailable'},
    'disclosure':{'default','focus','expanded','collapsed'}, 'overlay':{'default','focus','open','closed'},
    'data':{'default','loading','empty','partial','error'},
    'flow':{'default','loading','error','offline','permission-denied','success'},
    'media':{'default','loading','error','paused','reduced-motion'},
    'physical':{'default','idle','offline','error','reset'},
}


def system_inventory(c, data):
    from .validation import ROOT, load_json
    try:
        schema=load_json(ROOT/'templates/system-inventory.schema.json');check_schema(schema)
    except (OSError,ValueError,TypeError,KeyError,RecursionError):
        c.error('config_error','package.inventory_schema','Bundled inventory schema unavailable or unsupported');return
    structure(c,data,schema)
    if c.errors:return
    c.ref({'path':data['spec_template']},'spec_template')

    def index(rows,path):
        result={}
        for i,row in enumerate(rows):
            if row['id'] in result:c.error('duplicate_id',f'{path}.{i}','Repeated identifier')
            result[row['id']]=row
        return result
    profiles=index(data['profiles'],'profiles');categories=index(data['categories'],'categories')
    sources=index(data['sources'],'sources');families=index(data['families'],'families');entries=index(data['entries'],'entries')
    if set(profiles)!=PROFILES:c.error('profile_coverage','profiles','All eight named starter profiles are required')
    if set(categories)!=CATEGORIES:c.error('category_coverage','categories','All six named layers are required')
    for i,source in enumerate(data['sources']):
        day=c.day(source['checked_at'],f'sources.{i}.checked_at')
        if day and day>c.as_of:c.error('future_source',f'sources.{i}','Source check date is in the future')
        if source['verification']!='original-synthesis':
            url=urlsplit(source['url'])
            if url.scheme!='https' or not url.hostname or url.username or url.password:c.error('source_location',f'sources.{i}','Recorded primary source requires an HTTPS URL without credentials')
    for i,family in enumerate(data['families']):
        if not STATE_MINIMUM[family['interaction']].issubset(set(family['states'])):
            c.error('state_contract',f'families.{i}','Minimum state slots missing for the declared interaction family')
    used_sources={sid for e in entries.values() for sid in e['source_ids']}
    used_families={e['family'] for e in entries.values()}
    if set(sources)-used_sources:c.error('unused_source','sources','Every source record must support an entry')
    if set(families)-used_families:c.error('unused_family','families','Every family must have an inventory member')
    names=set()
    for i,entry in enumerate(data['entries']):
        path=f'entries.{i}'
        if not re.fullmatch(r'[A-Z]{1,3}-[0-9]{3}',entry['id']):c.error('entry_id',path,'Use a stable uppercase prefix and three-digit ID')
        name=entry['name'].strip().casefold()
        if name in names:c.error('duplicate_name',path,'Repeated concept name; represent platform differences as variants')
        names.add(name)
        allowed_kinds={'foundations':{'foundation','token'},'ui':{'primitive','component'},'patterns':{'pattern'},'templates':{'template'},'assets':{'asset'},'governance':{'requirement'}}
        if entry['kind'] not in allowed_kinds[entry['category']]:c.error('entry_kind',path,'Entry kind must match its layer')
        family=families.get(entry['family'])
        if not family or family['category']!=entry['category']:c.error('family_reference',path,'Family must exist in the same layer')
        if set(entry['profiles'])!=PROFILES:c.error('profile_coverage',path,'Every profile needs an explicit selection and rationale')
        for sid in entry['source_ids']:
            if sid not in sources:c.error('source_reference',path,'Unknown evidence source ID')
        for tid in entry['token_ids']:
            if tid not in entries or entries[tid]['kind']!='token':c.error('token_reference',path,'Token dependencies must reference token entries')
        if set(entry['related']) & (set(entry['depends_on']) | set(entry['token_ids'])):
            c.error('duplicate_relationship',path,'Required prerequisites and informational relationships must be distinct')
        for other in entry['depends_on']+entry['related']:
            if other not in entries or other==entry['id']:c.error('entry_reference',path,'Related or dependency ID is missing or self-referencing')
        for pid,decision in entry['profiles'].items():
            for depid in entry['depends_on']+entry['token_ids']:
                dep=entries.get(depid,{}).get('profiles',{}).get(pid,{})
                if not dep:continue
                if decision['selection']=='required' and dep['selection']!='required' or decision['selection'] in {'optional','needs-discovery'} and dep['selection']=='not-applicable':
                    c.error('dependency_profile',path,'Selected item requires a coherent dependency selection; required is transitive')
    visited=set();active=set()
    def visit(eid):
        if eid in active:c.error('dependency_cycle','entries','Dependency cycle detected');return
        if eid in visited or eid not in entries:return
        active.add(eid)
        for dep in entries[eid]['depends_on']+entries[eid]['token_ids']:visit(dep)
        active.remove(eid);visited.add(eid)
    for eid in entries:visit(eid)
    # Narrow claim tripwires, not natural-language truth verification.
    def texts(value):
        if isinstance(value,str):yield value
        elif isinstance(value,list):
            for item in value:yield from texts(item)
        elif isinstance(value,dict):
            for item in value.values():yield from texts(item)
    claim=re.compile(r'\b(?:is|are)\s+(?:WCAG[^\n]{0,25}\s+)?(?:compliant|conformant|certified|production.ready)|\b(?:approved|endorsed) by (?:W3C|Apple|Google|IBM)\b',re.I)
    for text in texts(data['entries']+data['families']):
        if claim.search(text):c.error('assurance_claim','inventory','Unsupported completed conformance or endorsement claim');break
    for category in CATEGORIES:
        if not any(e['category']==category for e in entries.values()):c.error('category_coverage','entries','A required inventory layer is empty')
    for pid in PROFILES:
        active_categories={e['category'] for e in entries.values() if e['profiles'].get(pid,{}).get('selection') in {'required','optional','needs-discovery'}}
        needed={'foundations','governance'} | ({'ui','patterns','templates'} if pid in {'website','web-app','native-phone','native-tablet','touch'} else {'assets'})
        if not needed.issubset(active_categories):c.error('profile_coverage','entries','Starter profile has an empty required layer')
    c.inventory_coverage={'entries':len(entries),'families':len(families),'profiles':len(profiles),'implemented':sum(e['status']['implementation']!='not-provided' for e in entries.values()),'tested':sum(e['status']['testing']!='not-performed' for e in entries.values()),
        'by_profile':{pid:{state:sum(e['profiles'].get(pid,{}).get('selection')==state for e in entries.values()) for state in ['required','optional','not-applicable','needs-discovery']} for pid in sorted(PROFILES)}}
