// Version-Timestamp: 2026-10-23 20:10:44 UTC
// FICTIONAL PLACEHOLDER CONTENT. "Northwind Field Ops" and every name, number, quote and price below are invented
// teaching material. Replace all of it with approved client facts before any deck leaves the studio.
export const PLACEHOLDER_NOTE = 'Fictional placeholder content. Replace every name, number, quote and price with approved facts before use.';

export const deck = {
  company: 'Northwind Field Ops',
  footer: 'Northwind Field Ops (fictional placeholder)',
  title: {
    kicker: 'Proposal for [Client name]',
    headline: 'Fewer site visits, faster fixes',
    sub: 'Remote diagnostics for regional maintenance teams',
    meta: '[Month YYYY] · Placeholder deck',
  },
  agenda: ['The problem we heard', 'What we propose', 'Proof from three pilots', 'Results in numbers', 'Case study', 'Team, pricing and next steps'],
  problem: {
    title: 'Half of truck rolls end with no fix on the first visit',
    points: [
      'Technicians arrive without the part or the history of the asset.',
      'Dispatch learns about faults from customer calls, not from the equipment.',
      'Every repeat visit costs a day of capacity in the busiest season.',
    ],
    stat: '1 in 2',
    statLabel: 'first visits without a fix (placeholder figure)',
  },
  solution: {
    title: 'Diagnose remotely, dispatch once',
    steps: [
      { label: 'Sense', text: 'Read fault codes from installed controllers every 15 minutes.' },
      { label: 'Decide', text: 'Rank faults by impact and match them to the right part and skill.' },
      { label: 'Dispatch', text: 'Send one technician with the part, the history and a checklist.' },
    ],
  },
  proof: {
    title: 'Three pilots, three regions',
    columns: [
      { head: 'Coastal utility', metric: '-38%', label: 'repeat visits in 6 months', note: 'Placeholder pilot A' },
      { head: 'Hospital estates', metric: '4.1 h', label: 'faster mean time to repair', note: 'Placeholder pilot B' },
      { head: 'Retail chain', metric: '92%', label: 'first-time fix rate', note: 'Placeholder pilot C' },
    ],
  },
  metric: {
    title: 'Hours returned to each team per month',
    labels: ['Q1', 'Q2', 'Q3', 'Q4'],
    values: [12, 19, 27, 34],
    max: 40,
    headline: '34 h',
    caption: 'per team per month by Q4 (fictional pilot data)',
  },
  caseStudy: {
    title: 'Case study: a regional water operator (fictional)',
    quote: '"We stopped sending two vans to every alarm." [Placeholder quote, Operations lead]',
    rows: [
      ['Measure', 'Before', 'After 6 months'],
      ['Repeat visits per month', '210', '130'],
      ['Mean time to repair', '9.6 h', '5.5 h'],
      ['Overtime hours', '640', '410'],
    ],
  },
  team: {
    title: 'The team you would work with',
    people: [
      { initials: 'EL', name: '[Name]', role: 'Engagement lead' },
      { initials: 'SA', name: '[Name]', role: 'Solutions architect' },
      { initials: 'FT', name: '[Name]', role: 'Field trainer' },
      { initials: 'DA', name: '[Name]', role: 'Data analyst' },
    ],
  },
  pricing: {
    title: 'Pricing and next steps',
    tiers: [
      { name: 'Pilot', price: '[$ amount]', detail: '1 region, 90 days, up to 200 assets' },
      { name: 'Rollout', price: '[$ amount] / month', detail: 'All regions, onboarding, monthly review' },
      { name: 'Partnership', price: 'Custom', detail: 'Integration with your work-order system' },
    ],
    next: ['Agree pilot region and asset list', 'Sign pilot order form', 'Kick-off within 2 weeks'],
  },
  closing: {
    headline: 'Let us pick the pilot region together',
    contact: '[name@example.com] · [+00 000 000 000]',
  },
};
