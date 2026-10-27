# Licensed asset stack for client work

Version-Timestamp: 2026-10-27 12:00:00 UTC

Use when a deliverable needs icons, fonts, sound effects, music or provenance metadata that the client does not already own. The default stack below is cleared for commercial client work under the conditions in each row. Anything outside it needs its license read and recorded before it enters a file.

All sources were accessed on 2026-10-23 (research record for the 0.8.0 production layer). Status tells you how the claim was checked:

- **verified**: read from the license file or registry entry itself.
- **search summary**: only a search-engine summary of the official page was reachable. Read the live page before relying on the detail.
- **unverified**: not confirmed. Treat it as an open question.

Licenses and site terms change. Re-read the source when a project starts and record what you read in the provenance record.

## Default stack

| Asset | Default source | License | Commercial client use | Keep with the files | Source (accessed 2026-10-23) | Status |
| --- | --- | --- | --- | --- | --- | --- |
| UI and editorial icons | Lucide 1.61.0 | ISC, plus MIT for icons derived from Feather | Yes | Both notices (ISC and the Feather MIT notice) in the project's license folder | https://raw.githubusercontent.com/lucide-icons/lucide/main/LICENSE | verified |
| Icons, multiple weights | Phosphor (`@phosphor-icons/core` 2.1.1) | MIT, "Copyright (c) 2023 Phosphor Icons" | Yes | MIT notice | https://raw.githubusercontent.com/phosphor-icons/core/main/LICENSE | verified |
| Icons, large outline set | Tabler Icons 3.49.0 | MIT | Yes | MIT notice | https://raw.githubusercontent.com/tabler/tabler-icons/main/LICENSE | verified |
| Fonts | Google Fonts families under SIL OFL 1.1 | OFL 1.1 per family; some families are Apache-2.0 or UFL | Yes, including print, PDF embedding and video | The family's own `OFL.txt` (or other license file) next to every bundled font file | https://raw.githubusercontent.com/google/fonts/main/ofl/inter/OFL.txt; commercial use per https://developers.google.com/fonts/faq | OFL text verified; FAQ search summary |
| Sound effects | Freesound, **CC0 filter only** | CC0 1.0 | Yes, with the limits below | Saved CC0 deed, sound URL, uploader name | https://raw.githubusercontent.com/creativecommons/cc-legal-tools-data/main/docs/publicdomain/zero/1.0/legalcode.en.html | CC0 text verified; Freesound FAQ unverified |
| Music and sound effects | Pixabay | Pixabay Content License | Yes, inside a new work, with the prohibited uses below | The track's license `.txt` or certificate download, track URL, retrieval date | https://pixabay.com/service/license/, https://pixabay.com/service/terms/ | search summary |
| Content credentials | `c2patool` 0.28.2 (optional) | MIT OR Apache-2.0 | Yes | Nothing extra; record the manifest and signing certificate used | https://github.com/contentauth/c2pa-rs (crates.io registry entry) | verified (registry) |

## Tools that are not MIT

- **Remotion** (used by `library/examples/motion-remotion`) is source-available under the Remotion License, not MIT: https://github.com/remotion-dev/remotion/blob/main/LICENSE.md. The Free License covers individuals and companies of up to 3 people; contractors and agencies on the same project count toward the total. At 4 or more, buy a Company License (https://www.remotion.dev/docs/license). Under the v5.0 terms, CLI and `renderMedia()` renders are metered as Automators use (verify which terms apply to your version). Each user of this kit is responsible for their own license.
- **FFmpeg** bundled in `@remotion/compositor-*` is a GPL-2.0+ build. Running it is fine; do not redistribute the binaries.
- **Ghostscript** is AGPL-3.0 or commercial. Document it as an optional, user-installed tool; never bundle it or expose it as a network service.

## Conditions per source

### Icons

- Pick one icon family per product or brand. Mixing Lucide's 2px stroke with Phosphor's fill weights reads as two systems.
- Lucide: ship both notices. Icons that came from Feather stay under MIT; the rest are ISC. One combined license file with both texts is the simplest default.
- Modified icons stay under the same license. Record the modification in the provenance record.
- An icon license does not clear a trademark. Brand logos inside icon sets (social networks, payment schemes) follow each owner's brand guidelines, not the icon license.

### Fonts

- OFL 1.1 lets fonts "be bundled, embedded, redistributed and/or sold with any software", but not "sold by itself" (OFL.txt, verified).
- "The requirement for fonts to remain under this license does not apply to any document created using the Font Software" (OFL.txt, verified). PDFs, printed pieces, videos and images made with the font are not bound by the OFL.
- Check each family's license file before bundling it. Google Fonts hosts some families under Apache-2.0 or the Ubuntu Font License; the folder name in `google/fonts` (`ofl/`, `apache/`, `ufl/`) tells you which.
- Reserved Font Names: if you modify an OFL font (subset with renamed glyphs, add glyphs, change metrics) and the family declares a Reserved Font Name, rename your version. Whether plain subsetting for web delivery counts as modification is debated (unverified here); check the family's statement or keep the original name only when the family's FAQ allows it.
- Commercial (non-OFL) fonts: the client's license must cover each use separately (desktop, web, app embedding, broadcast, logo use). Record the license tier and seat count; never bundle them into the kit or a shared template without the license allowing it.

### Freesound (CC0 only)

- Filter search results to CC0 before listening. Freesound also hosts CC BY and CC BY-NC sounds; CC BY-NC cannot be used in commercial client work [search summary, Freesound forum]. CC BY is usable only with the required attribution, so it stays off the default list.
- CC0 waives copyright, but "No trademark or patent rights held by Affirmer are waived" (section 4a) and the user is responsible for clearing other people's rights, such as publicity or privacy (section 4b). A recorded voice, a branded jingle or an identifiable person still needs clearance.
- Save the sound page URL, the uploader name and the CC0 deed with the file, even though CC0 needs no attribution. The record proves the license at the time you downloaded it.

### Pixabay Content License

- Grants a worldwide, royalty-free, irrevocable right to use and modify content for commercial purposes without attribution [search summary].
- Prohibited [search summary]:
  - selling or distributing content "on a Standalone basis", that is, with no creative effort applied (a stock clip re-uploaded as is, a track sold as a ringtone);
  - commercial use of content that shows trademarks, logos or brands;
  - immoral or illegal uses.
- Combining the content into a new work (a video, an ad, a deck) is not standalone use.
- Pixabay music sometimes triggers YouTube Content ID claims [search summary, third-party reports]. Download and keep the license `.txt` or certificate for every track, and give it to whoever uploads the video so they can dispute a claim.

### C2PA content credentials (optional)

- `c2patool` 0.28.2 (MIT OR Apache-2.0, updated 2026-10-08) reads and writes C2PA manifests. The `c2pa` Rust crate 0.91.4 implements "a subset" of C2PA 2.4. All implementations are pre-1.0 (verified on crates.io and npm/PyPI registries).
- Use it as an external step after export, never as a dependency of the kit's Python helpers (standard library only).
- Signing for public trust needs a real certificate from a certificate authority the verifier trusts. Self-signed or test certificates are not on validators' trust lists, so expect an untrusted-signer warning (verify with the validator you target).
- Recommended when a client publishes AI-assisted imagery or needs an audit trail for edits. Not required for ordinary deliverables.

## Never use

| Do not use | Why | Use instead |
| --- | --- | --- |
| NC (NonCommercial) licensed assets in client work (CC BY-NC, BY-NC-SA, BY-NC-ND) | Client work is commercial use | CC0, Pixabay Content License, or a paid license recorded per project |
| ND (NoDerivatives) assets you will crop, recolor, remix or edit | Edits create a derivative | An asset whose license allows modification |
| Unlicensed scraped imagery: search-engine results, Pinterest, social posts, competitor sites, "free wallpaper" sites without a license page | No license, no chain of title | Licensed stock, commissioned photography, or the client's own library with written rights |
| Prompts naming a living artist, illustrator or photographer ("in the style of [living artist]") for client deliverables | Reputational and legal risk; the client cannot defend the work as original | Describe the visual qualities (medium, palette, line weight, lighting, composition) instead of the person |
| Third-party logos, mascots or characters in mockups or icons, beyond nominative reference with the owner's guidelines | Trademark and copyright | Neutral placeholders; the owner's official asset kit when the client has a partnership |
| Fonts copied from a client machine, a design file or a website's CSS | Desktop and web font licenses rarely allow redistribution | The foundry license the client owns, or an OFL alternative |
| Audio ripped from YouTube, TikTok, Spotify or a film | No license for reuse | CC0, Pixabay, or a licensed library track |
| Assets whose license you cannot find or save | You cannot prove the license later | Skip the asset |

## Provenance record

Keep one record per third-party asset in the project (not in this kit), for example `licenses/ASSETS.md`, with license files saved beside it as `licenses/<asset-id>.txt`. Fill it when the asset is downloaded, not at delivery.

```markdown
## <asset-id>  (e.g. sfx-door-close-01)
- File in project: assets/audio/sfx-door-close-01.wav
- Asset type: sound effect | music | icon set | font | image | video
- Title and creator: <title>, by <author or uploader>
- Source URL: <exact page the file came from>
- License: <name and version, e.g. CC0 1.0 / Pixabay Content License / OFL 1.1>
- License URL: <deed or license page>
- Retrieved: <YYYY-MM-DD> by <person>
- License file saved: licenses/<asset-id>.txt  (copy of the license or download certificate as shown on the retrieval date)
- Modifications: <none | trimmed 0:00-0:04, pitched -2 st, recolored, subset>
- Used in: <project> / <deliverable and version>
- Restrictions noted: <trademark visible, people visible, Content ID risk, attribution text required>
- Approved by: <name, role> on <YYYY-MM-DD>
```

Defaults for the record:

- **Approver**: the project lead signs off third-party assets before the first client review; the client's legal or brand contact signs off anything with people, trademarks or a paid license.
- **Retention**: keep the records and license files with the project archive for as long as the client uses the deliverable.
- **Handoff**: include `licenses/` in the delivery package, so the client can answer a claim without calling you.

## When the default stack does not fit

- **Client already licenses a library** (Getty, Adobe Stock, Epidemic Sound, Artlist): use it, record the license tier and the account owner, and check whether the license transfers to the client or stays with the studio.
- **Broadcast, paid media or packaging**: confirm the license covers the media, territory, term and print run. Many free and subscription licenses exclude some of these; read the specific clause.
- **Regulated categories** (pharma, finance, children's products): route every asset with people or claims through the client's legal review. Confirm requirements with counsel for the specific product and jurisdiction.

Agent-Attribution: computer=vm; tool=Claude Code; version=2.1.309; timestamp=2026-10-23 20:10:44 UTC
