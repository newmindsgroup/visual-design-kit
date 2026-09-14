# C-038 Data table: filled specification example

Version-Timestamp: 2026-09-10 20:21:45 AST

## Identity and scope

Record TBL-EX-01, candidate 1.0; inventory [C-038 Data table](../../inventory/ui.md#c-038), family [data](../../inventory/families.md#data). Owner Codex; document review checks (historical source-version evidence, not bundled or inherited); criterion authority [WORK-EX-01](work-record.md). Optional item selected to teach comparison of a small, read-only dataset on web. Sorting controls are interactive; cells are not an editable grid. Native phone/tablet adoption is a separate representation decision.

Use when people need row/column comparison. Prefer a list/detail view when one record at a time is the real task. Cell editing, selection, virtualization, pagination, grouped headers and spreadsheet key navigation are excluded. C-039 Editable data grid requires its own interaction contract.

## Select core and task behavior

This table owns applicability. The full remote/sort fixture below is optional; a static table still needs semantic relationships and honest data.

| Section | Activation condition and dependencies | Included states and criteria | Omission or hold |
| --- | --- | --- | --- |
| TBL-CORE | Every read-only table: caption, headers, row identity, values, missing-value meaning and readable layout | TBL-S2; S4 for zero rows; S5 invalid-data branch if data can be malformed. TBL-01 relationships branch, TBL-02 static-data branch; SH-01/SH-02 | Essential relationships are never optional. No sort buttons/aria-sort, remote request adapter or Retry is required for fixed valid local data |
| TBL-SORT | People need ordering controls; depends on TBL-CORE and complete-batch comparator/locale | TBL-S3; TBL-01 sorting branch. With TBL-REMOTE also use TBL-02 sort-focus clauses | Omit when source order is sufficient. This example sorts a complete batch locally. Server-side sorting/pagination is held for its actual ordering/identity/partial-data contract, not inferred from these rules |
| TBL-REMOTE | Dataset arrives or refreshes asynchronously; depends on TBL-CORE and data/freshness/permission policy | TBL-S1/S5 fetch-error/S6/S7; TBL-02 remote-data branch; sort-control clauses only with TBL-SORT | Omit for fixed local data. When selected, loading/error/stale/partial semantics and recovery are required, even without sorting |
| TBL-ALTERNATE | A list representation is appropriate for the task and DEC-04 resolves comparison needs | TBL-V2/TBL-S8 and TBL-03 | Optional alternate, not optional reflow. Core table overflow and surrounding reflow remain required if alternate is omitted. Native mapping remains held for actual platform scope |

Core invalid-data handling does not imply a network Retry button: reject unsafe/malformed input and expose a truthful configuration/data problem through the containing context. With remote loading selected, the fetch/retry state applies. A static local table uses the same row/header/data meanings without the remote fixture machinery.

## Anatomy, variants and data contract

TBL-V1 contains caption “Reference items,” column headers Name, Quantity and Updated, each Name cell also a row header with its stable ID visibly appended as a secondary identifier, rows keyed by stable ID, Name/Quantity header buttons and sort indicator only with TBL-SORT, adjacent result/freshness status only when the selected data task needs it and a bounded overflow region. TBL-V2 is a narrow record-list representation, only adopted if DEC-04 approves loss of simultaneous column comparison. Every record retains labeled fields and the same data identity. Never infer the alternate is appropriate from viewport width alone.

Illustrative roles: surface.table, text.cell, text.header, border.row, space.cell, type.numeric, focus.indicator and status.stale. Values and density come from the project token authority. F-001/F-002/F-003/F-009, C-001 sort/retry actions and existing data-family guidance are dependencies; no new inventory component is introduced.

### Core data and bounded fixtures

The teaching dataset is a complete small batch, not a server-paginated collection. Each row has unique nonempty id, nonempty name string, quantity as nonnegative integer or explicit null, and updatedAt as valid ISO timestamp or explicit null. Null displays “Not provided,” never zero. Repeated names are disambiguated by the visible stable ID in each row header (for example, “Beta, r2” versus “Beta, r3”); sorting still uses the original name field, not the presentation string. Duplicate IDs and malformed values produce a data error before replacing the displayed batch. Labels/text are rendered as text. Column units must be supplied if quantity represents a physical measure; none are inferred.

Fixtures: r1/“Alpha”/0/null; r2/“Beta”/12/2026-09-01T12:00:00Z; r3/“Beta”/null/2026-09-02T12:00:00Z. Also empty batch, one row, long name of 200 repeated letters, RTL name, malformed timestamp, duplicate ID, delayed response, failed refresh and partial=true. These are artificial test data, not user findings.

### TBL-SORT: only for selected ordering controls

Initial order is source order. Without TBL-SORT, keep that order and omit the rest of this section. First activation of a sortable header requests ascending; repeat toggles descending. Sorting Quantity compares numbers, keeps null last in either direction and breaks ties by stable ID ascending. Name uses the explicitly selected locale collator and the same ID tie-break; locale is unresolved until adoption. Date display uses explicit locale/time zone and exposes enough text to distinguish dates. Sort occurs over the whole complete batch, not just an unseen page. Partial data is labeled and sorting is disabled in this example until the adapter supplies the complete set.

## State catalog for selected sections

| State ID | Trigger and visible result | Input/focus/assistive result | Recovery and criterion |
| --- | --- | --- | --- |
| TBL-S1 loading | First fetch pending; caption plus “Loading items,” no invented rows | Status announced without focusing it; decorative skeletons, if any, hidden from semantics | Data to S2; error to S5. TBL-02 |
| TBL-S2 populated/default | Complete valid batch replaces pending display | Native table/header relationships; cell browsing uses assistive table commands, not custom arrow-key grid behavior | TBL-SORT enables S3; TBL-REMOTE enables refresh to S6. Core-only stays S2 until its source data changes. TBL-01 |
| TBL-S3 sorted/focused | Header button changes ordering and one active sort indicator | Keep focus on activated header button; expose aria-sort on the sorted header, announce updated sort/result once | Repeat toggles direction, other column replaces active sort. TBL-01 |
| TBL-S4 empty | Successful complete batch of zero rows | “No items available” readable with caption; headers are not proof of data; sort controls unavailable only if TBL-SORT is selected | Core-only: remain empty until the containing source supplies a new valid batch, then S2; no refresh control. Only TBL-REMOTE offers refresh through S1/S2. TBL-02 |
| TBL-S5 invalid-data/fetch error | Core: invalid local data. TBL-REMOTE: failed fetch/validation without prior good batch | Core: truthful data/configuration error with no implied fetch or Retry. TBL-REMOTE: visible fetch error and Retry button; no false empty-success state | Core: owner/source supplies corrected data, then S2 or S4. Only TBL-REMOTE Retry goes to S1. TBL-02 |
| TBL-S6 refreshing/stale | Prior rows remain while refresh pending or fails, clearly marked previous data | Keep existing focus; do not announce a success; sort disabled during pending replacement only with TBL-SORT | New valid batch to S2; failed refresh retains rows plus Retry. TBL-02 |
| TBL-S7 partial | Adapter marks incomplete batch; explicitly label partial, avoid a total count claim | Sort controls unavailable with adjacent reason only with TBL-SORT; preserve row/header relationships | Complete retrieval replaces partial batch. TBL-02 |
| TBL-S8 alternate representation | Approved narrow/list mode chosen under DEC-04 | Same record IDs/values and labels, only one representation exposed; preserve focused logical action when present | Return to table restores context. TBL-03 |

### Conditional sort-control behavior

Only with TBL-SORT, keep sort controls mounted and focusable with aria-disabled=true plus handler suppression while sorting is unavailable. Empty/invalid data may cause this without a fetch; loading/partial/refreshing states apply only with TBL-REMOTE. This reuses C-001's focus-preserving busy semantics rather than its native-disabled precondition variant. Show the reason and suppress activation. Re-enabling preserves focus and stable control identity. With TBL-REMOTE also selected, a failed refresh of a prior complete valid batch permits sorting retained rows while the stale label stays visible; it does not claim fresh results.

### Conditional remote-data behavior

Only with TBL-REMOTE, malformed or duplicate-ID refresh data never replaces the good batch, and out-of-order replies never replace a newer batch. Use request identity. Offline with prior data is stale; with none it is an error. Any Retry control uses ordinary C-001 activation behavior. These clauses do not introduce a fetch or Retry into core-only use.

### Core safety and exclusions

Passive rows have no disabled/pressed state. Read-only is the scope, not an input attribute on a table. Selected/mixed/edited-row/success-toast states are excluded. Core data validation and honest empty/invalid handling remain required for applicable inputs, with no invented network action. Any protected dataset, including local data, needs its own access/retention contract before reuse; an authorization failure must not expose protected content.


## Platform, layout and handoff

Web uses native table structure, caption, column headers with scope=col on column headers, scope=row on each Name row header, and buttons inside sortable column headers. Do not add role=grid for sorting alone. Noninteractive cells do not enter the tab sequence. Sources SRC-TABLE/SRC-TABLE-HEADERS guide relationships. A horizontally overflowing comparison table may use a labeled keyboard-reachable scroll region when needed; its surrounding caption/status/actions must still reflow. Keep individual cell content readable and wrap long names. A table exception does not exempt the page from reflow.

For an approved V2 list, keep field labels, missing values, record order, sort controls and freshness visible. Hidden duplicate representations must not create duplicate accessible content or IDs. No automatic column dropping. Native list/detail or platform table mapping needs selected OS/window sizes, accessibility grouping and record navigation. Web scope/aria-sort attributes cannot define that native behavior. DEC-04 holds the choice if comparison is essential but the brief also demands no horizontal scroll.

Use locale-aware dates/numbers, logical alignment, isolated mixed-direction strings, and meaningful column order in RTL. Do not reverse an ordinal or date string by hand. Zoom, long content and reduced motion must preserve values and controls. SH-01/SH-02 apply; no virtualized performance claim is made.

Handoff: TBL-01 to TBL-03, TBL-SP-01 and DEC-04. Real batch limits, locale/time zone, freshness/permission policy and native representation belong to product/data/platform owners before adoption. This teaching specification has no implementation or measured behavior evidence.
