# Information architecture

Version-Timestamp: 2026-10-20 02:04:32 UTC

Good IA lets people predict where something lives before they click. Build it from user tasks and real content, name things in users' words, then prove it with a tree test before anyone designs a screen.

## Start from content and tasks

1. **Content inventory.** One row per page or content item: ID, URL or screen, title, type, owner, last updated, traffic (12 months), inbound links, status. For sites over about 500 pages, sample by template and traffic.
2. **Content audit.** Mark each item keep, merge, rewrite or delete. ROT (redundant, outdated, trivial) content commonly makes up a large share of legacy sites; deleting it simplifies IA more than any menu redesign.
3. **Top tasks.** Gerry McGovern's top-tasks method: build a list of 50-100 candidate tasks from search logs, support, analytics and stakeholders; have a few hundred users each vote for their top 5. The top 5-10 tasks get the most prominent paths.
4. **Vocabulary.** Collect the words users actually use from site search logs, support tickets, interviews and open card sort group names.

## Organization schemes

| Scheme | Type | Use when | Watch for |
| --- | --- | --- | --- |
| Alphabetical | Exact | People know the name (glossaries, directories, brands) | Useless when people do not know the term |
| Chronological | Exact | News, events, releases, history | Needs topic filters for archives |
| Geographical | Exact | Locations, stores, regional services | Edge cases across borders |
| Topic or subject | Ambiguous | Most content sites | Overlap between topics; test labels |
| Task | Ambiguous | Services and apps ("Pay a bill", "Report a problem") | Can fragment content that serves several tasks |
| Audience | Ambiguous | Content truly differs by audience (patients versus clinicians) | People rarely self-identify; overlapping content duplicates |
| Metaphor | Ambiguous | Rarely; playful or spatial products | Breaks when the metaphor stretches |

Source: Rosenfeld, Morville and Arango, *Information Architecture: For the Web and Beyond* (4th ed., 2015). Combine schemes deliberately (task-based primary navigation with a topic index), not by committee.

## Structures

- **Hierarchy** for most sites and apps.
- **Database or faceted** for large uniform collections (products, listings, documents, people): facets are independent dimensions such as type, price, size, location, date.
- **Sequential** for linear processes (applications, onboarding, checkout).
- **Hypertext** cross-links for related content, never as the only path.

## Breadth versus depth

- Prefer broad and shallow. Studies from Miller (1981) to Larson and Czerwinski (1998) found people find items faster in broader, shallower hierarchies, provided the groups are well organized and labeled.
- Starting points: 5-9 top-level groups for a marketing site; up to 10-12 sidebar destinations in an app when grouped under headings; 3 levels or fewer for sites under about 500 pages.
- The "three-click rule" is a myth: UIE's testing (Porter, 2003) found people did not give up more often on paths with more clicks, as long as each click carried strong information scent.
- Information scent (Pirolli and Card, 1999): each label must let people predict what is behind it. Weak scent, not click count, causes abandonment.

## Labeling

- Use users' words, verified in card sorts and search logs. "Pricing" beats "Plans and solutions"; "Contact us" beats "Connect".
- Front-load the distinguishing word: "Billing settings", "Billing history", not "Settings for billing".
- Keep labels mutually exclusive at each level. If people cannot say which of two groups holds an item, merge or rename them.
- 1-3 words per label. No invented brand terms in navigation unless users already know them.
- The page H1 matches the navigation label that leads to it.
- Avoid catch-alls ("Resources", "More", "Other") at the top level unless testing shows people use them.

## Navigation systems

| System | Purpose |
| --- | --- |
| Global | Top-level destinations on every page |
| Local | Siblings and children within a section |
| Contextual | Related content inside the body ("See also", inline links) |
| Utility | Sign in, account, language, search, cart, help |
| Breadcrumbs | Location in a hierarchy 3+ levels deep |
| Footer | Secondary destinations, legal pages, contact, sitemap |
| Supplementary | Index, A-Z, guides, site search |

Interaction patterns for each are in `ui-design` [navigation](../../ui-design/references/navigation.md).

## Taxonomy and metadata

- Define a controlled vocabulary per facet, with preferred terms and synonyms ("sofa" = "couch" = "settee") so search and filters agree.
- Each content type gets a model: fields, required metadata, relationships (an Article has an Author, Topics and Related products).
- Polyhierarchy (one item in two categories) is fine for products; give each item one canonical URL.
- Keep facet values short and sortable; show counts; hide facets that would return zero results.

## Search as part of IA

- Sites with more than about 100 pages, or any catalog, need site search. Review search logs monthly: top queries, zero-result queries and queries followed by exits.
- Zero-result queries reveal missing content or missing synonyms; fix the vocabulary before the ranking.
- Search does not excuse weak navigation; many people browse first.

## Deliverables

**Sitemap** as a table (and a diagram for presentation):

| ID | Page | Parent | Template | Primary task served | URL |
| --- | --- | --- | --- | --- | --- |
| 1.0 | Home | none | home | Orient, route to top tasks | `/` |
| 2.0 | Products | 1.0 | listing | Compare products | `/products/` |
| 2.1 | Product detail | 2.0 | product | Evaluate and buy | `/products/{slug}/` |
| 3.0 | Pricing | 1.0 | pricing | Choose a plan | `/pricing/` |

Also deliver: content model (types, fields, relationships), taxonomy (facets, values, synonyms), navigation spec (global, local, utility, footer, mobile), URL scheme (lowercase, hyphens, stable, no dates unless content is dated), labeling glossary.

## Validate before visual design

1. **Open card sort** (15-20 people per audience) to learn groups and words.
2. **Draft 2 candidate hierarchies** from the sort and the top tasks.
3. **Tree test both** (about 50 people per tree, 8-10 tasks covering top tasks and known problem areas). Flag tasks under about 70% success or with scattered first clicks.
4. **Revise and re-test** the weak branches only.
5. **First-click test** the designed navigation and **usability test** the full flows.

## Apps and mobile

- Native apps: 3-5 top-level destinations in a tab bar; deeper structure in hubs and lists.
- Put frequent objects (projects, conversations, orders) one level from home; put settings and admin in utility navigation.
- Global search or a command palette replaces deep menus for expert users with many objects.
