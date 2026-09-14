"""Deterministic, reference-only Markdown views of the shared inventory."""
# Version-Timestamp: 2026-09-07 13:54:06 AST
from pathlib import Path
from .system_inventory import CATEGORIES, PROFILES


def render_views(data):
    """Return fixed relative paths and content. No writes, clock, network or execution."""
    stamp=data['Version-Timestamp'];entries={e['id']:e for e in data['entries']}
    def header(title):
        return [f'# {title}',f'\nVersion-Timestamp: {stamp}',
                '\nGenerated from master.json. Listed concepts and shared specification starters only. '
                'No completed component specifications, implementation or testing is supplied. '
                'Profile selections are starting recommendations, not approved project scope.\n']
    def link(eid):
        e=entries[eid];return f'[{eid}: {e["name"]}]({e["category"]}.md#{eid.lower()})'
    def bullets(values):return ['- '+x for x in values] or ['- None recorded.']
    views={}
    cats={x['id']:x['name'] for x in data['categories']}
    profiles={x['id']:x for x in data['profiles']}
    index=header('Shared system inventory index')
    index+=['[Scope and method](../SYSTEM-INVENTORY.md) | [Shared contracts](families.md) | [Profile summary](profiles.md)\n',
            '| Layer | Entries |','| --- | ---: |']
    for category in sorted(CATEGORIES):
        members=sorted((e for e in entries.values() if e['category']==category),key=lambda e:e['id'])
        index.append(f'| [{cats[category]}]({category}.md) | {len(members)} |')
        lines=header(cats[category])+['[Index](index.md) | [Specification template](../templates/system-item.md)\n']
        for e in members:
            lines += [f'<a id="{e["id"].lower()}"></a>',f'\n## {e["id"]}: {e["name"]}',
                      '\n'+e['definition'],f'\nKind: {e["kind"]}. Shared contract: [{e["family"]}](families.md#{e["family"]}).',
                      '\n### Variants to specify\n']+bullets(e['variants'])
            lines+=['\n### Entry-specific states and behavior\n']+bullets(e['state_notes'])
            lines+=['\n### Project decisions still required\n']+bullets(e['decisions'])
            lines+=['\n### Profile starting points\n','| Profile | Selection | Rationale |','| --- | --- | --- |']
            for pid in sorted(PROFILES):
                p=e['profiles'][pid];lines.append(f'| [{profiles[pid]["name"]}](profile-{pid}.md) | {p["selection"]} | {p["rationale"]} |')
            lines+=['\nToken roles: '+(', '.join(link(x) for x in e['token_ids']) or 'None required by this entry.'),
                    '\nDependencies: '+(', '.join(link(x) for x in e['depends_on']) or 'None recorded.'),
                    '\nRelated concepts: '+(', '.join(link(x) for x in e['related']) or 'See shared family and dependencies.'),
                    '\nSource basis: '+', '.join(f'[{sid}](../INVENTORY-SOURCES.md#{sid})' for sid in e['source_ids'])+'. '+e['evidence_note'],
                    '\nStatus: inventoried; common specification template available; implementation not provided; testing not performed.\n']
        views[f'inventory/{category}.md']='\n'.join(lines)+'\n'
    views['inventory/index.md']='\n'.join(index)+'\n'
    lines=header('Shared specification family contracts')
    lines+=['These contracts identify questions and acceptance topics. Apply them with the entry notes and record exclusions. They are not complete specifications for every family member.\n']
    for f in sorted(data['families'],key=lambda f:f['id']):
        lines += [f'<a id="{f["id"]}"></a>',f'\n## {f["name"]}', '\n'+f['purpose'],
                  '\nInteraction class: '+f['interaction']+'. State slots: '+', '.join(f['states'])+'.',
                  '\nA slot is a review prompt. Record not-applicable with a reason when the entry cannot have that state.']
        for label,key in [('Behavior','behavior'),('Accessibility','accessibility'),('Content and data','content_data'),('Decisions','decision_prompts')]:
            lines+=['\n### '+label+'\n']+bullets(f[key])
        lines+=['\n### Platform adaptations\n']
        for platform,value in sorted(f['platform_variants'].items()):lines+=['- '+platform+': '+(' '.join(value) if isinstance(value,list) else value)]
        lines+=['\nMembers: '+', '.join(link(e['id']) for e in entries.values() if e['family']==f['id'])+'\n']
    views['inventory/families.md']='\n'.join(lines)+'\n'
    summary=header('Profile starting points')+['Profiles can be combined. Reconcile conflicting selections in the blank scoping record. Required means a reusable starting dependency, not a demand to ship the feature.\n',
        '| Profile | Required | Optional | Not applicable | Needs discovery |','| --- | ---: | ---: | ---: | ---: |']
    for pid in sorted(PROFILES):
        p=profiles[pid];counts={s:sum(e['profiles'][pid]['selection']==s for e in entries.values()) for s in ['required','optional','not-applicable','needs-discovery']}
        summary.append(f'| [{p["name"]}](profile-{pid}.md) | '+ ' | '.join(str(x) for x in counts.values())+' |')
        lines=header(p['name'])+['\n'+p['purpose'],'\n[Blank scoping record](../templates/system-scope.md) | [Profile summary](profiles.md)\n']
        for selection in counts:
            lines += ['\n## '+selection+'\n']
            for e in sorted(entries.values(),key=lambda e:e['id']):
                if e['profiles'][pid]['selection']==selection:lines+=['- '+link(e['id'])+': '+e['profiles'][pid]['rationale']]
        views[f'inventory/profile-{pid}.md']='\n'.join(lines)+'\n'
    views['inventory/profiles.md']='\n'.join(summary)+'\n'
    return views


def check_views(root, views):
    errors=[];root=Path(root).resolve()
    for relative, expected in views.items():
        target=(root/relative).resolve()
        if not target.is_relative_to(root):errors.append(f'{relative}: outside root');continue
        try:
            if target.read_text(encoding='utf-8')!=expected:errors.append(f'{relative}: stale generated view')
        except (OSError,UnicodeError):errors.append(f'{relative}: missing or unreadable generated view')
    return {'valid':not errors,'checked_views':len(views),'errors':errors,'executes':False}
