# Website practice fixture

Version-Timestamp: 2026-09-11T20:58:31-04:00

Parent: website checks (historical evidence not included). Related: [workflow](../../WEBSITE-WORKFLOW.md).

Bench & Grain is a fictional repair studio. The audience hypothesis is a furniture owner deciding whether to ask about repair. No customer research, real service, credentials or performance claims are implied.

The opening explains the proposition; services explain scope; the editorial section explains an approach; the form demonstrates safe recovery. Long content and a missing image exercise a second editorial variant. The chair drawing is an original schematic, not photography of completed work.

## Reproduce

Run `python3 scripts/website_fixture.py /absolute/new/output-directory` from the repository. The destination must not exist. Serve that directory locally with Python's HTTP server on port 17660. Run `node --test examples/website-practice/form-model.test.mjs` and `python3 -m unittest discover -s tests`.

Browser checks require an isolated Chrome debugging instance on port 17661 and `EVIDENCE_DIR` pointing to a private evidence directory. Run `node examples/website-practice/browser-checks.mjs`. Never connect this runner to a signed-in personal browser profile.

## Contracts and limits

Editorial records require status, title, body and image. Status is draft or published; image is a Boolean. Only published records enter generated HTML. Text is escaped, and absent images create no empty frame. The template and source records are excluded from the served output.

The form is a local simulation that sends nothing and collects no personal data. An uncertain response remains locked until simulated reconciliation. JavaScript failure leaves submission disabled. A real service needs authoritative reconciliation, validation, storage and a usable alternative contact route.

This exercises page structure, responsive layout and static CMS-style publication boundaries. It is not an installed CMS, booking system, commerce site or full accessibility audit. Independent review remains pending authentication.

## Observed lesson

Mobile screenshot inspection found adjacent sentences touching when a responsive rule hid a line break. Explicit whitespace now survives that change. Automated overflow checks alone would not catch this typography defect.
