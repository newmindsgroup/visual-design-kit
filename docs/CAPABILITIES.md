# Complete capability catalog

Version-Timestamp: 2026-09-14T15:19:22.465999-04:00

Generated from the actual catalog. These are 130 reference workflows, not 130 independently production-certified tools. Dependencies specify required input contracts; accepted work may be reused.

| ID | Instruction | Dependencies |
| --- | --- | --- |
| `research` | [design-evidence-research](../plugins/visual-design-studio/library/draft-skills/design-evidence-research/SKILL.md) | None declared |
| `persona` | [design-persona-build](../plugins/visual-design-studio/library/draft-skills/design-persona-build/SKILL.md) | `research` |
| `handoff` | [design-stage-handoff](../plugins/visual-design-studio/library/draft-skills/design-stage-handoff/SKILL.md) | None declared |
| `reference-direction` | [design-reference-direction](../plugins/visual-design-studio/library/draft-skills/design-reference-direction/SKILL.md) | `research` |
| `brand-strategy` | [design-brand-strategy](../plugins/visual-design-studio/library/draft-skills/design-brand-strategy/SKILL.md) | `research`, `persona` |
| `identity` | [design-identity-system](../plugins/visual-design-studio/library/draft-skills/design-identity-system/SKILL.md) | `brand-strategy` |
| `ux` | [design-ux-architecture](../plugins/visual-design-studio/library/draft-skills/design-ux-architecture/SKILL.md) | `research`, `persona` |
| `prototype` | [design-prototype-evaluation](../plugins/visual-design-studio/library/draft-skills/design-prototype-evaluation/SKILL.md) | `ux` |
| `ui` | [design-ui-system](../plugins/visual-design-studio/library/draft-skills/design-ui-system/SKILL.md) | `ux`, `identity` |
| `production` | [design-production-interface](../plugins/visual-design-studio/library/draft-skills/design-production-interface/SKILL.md) | `handoff` |
| `delivery` | [design-quality-delivery](../plugins/visual-design-studio/library/draft-skills/design-quality-delivery/SKILL.md) | `production` |
| `content` | [design-content-writing](../plugins/visual-design-studio/library/draft-skills/design-content-writing/SKILL.md) | `research`, `handoff` |
| `infographics` | [design-infographics](../plugins/visual-design-studio/library/draft-skills/design-infographics/SKILL.md) | `content`, `production` |
| `higgsfield-cli` | [design-higgsfield-cli](../plugins/visual-design-studio/library/draft-skills/design-higgsfield-cli/SKILL.md) | `production`, `media-route-selection` |
| `openart-cli` | [design-openart-cli](../plugins/visual-design-studio/library/draft-skills/design-openart-cli/SKILL.md) | `production`, `media-route-selection` |
| `foundations` | [design-foundations](../plugins/visual-design-studio/library/draft-skills/design-foundations/SKILL.md) | `reference-direction`, `handoff` |
| `typography` | [design-typography](../plugins/visual-design-studio/library/draft-skills/design-typography/SKILL.md) | `foundations` |
| `color` | [design-color-system](../plugins/visual-design-studio/library/draft-skills/design-color-system/SKILL.md) | `foundations` |
| `motion` | [design-motion-effects](../plugins/visual-design-studio/library/draft-skills/design-motion-effects/SKILL.md) | `foundations`, `production` |
| `display-discovery` | [design-display-discovery](../plugins/visual-design-studio/library/draft-skills/design-display-discovery/SKILL.md) | `research`, `handoff` |
| `display-art-direction` | [design-display-art-direction](../plugins/visual-design-studio/library/draft-skills/design-display-art-direction/SKILL.md) | `display-discovery`, `reference-direction` |
| `display-content` | [design-display-content](../plugins/visual-design-studio/library/draft-skills/design-display-content/SKILL.md) | `display-discovery`, `content` |
| `display-campaigns` | [design-display-campaigns](../plugins/visual-design-studio/library/draft-skills/design-display-campaigns/SKILL.md) | `display-content` |
| `touchscreen-design` | [design-touchscreen-design](../plugins/visual-design-studio/library/draft-skills/design-touchscreen-design/SKILL.md) | `display-discovery`, `ux` |
| `display-production` | [design-display-production](../plugins/visual-design-studio/library/draft-skills/design-display-production/SKILL.md) | `display-discovery`, `production` |
| `display-evaluation` | [design-display-evaluation](../plugins/visual-design-studio/library/draft-skills/design-display-evaluation/SKILL.md) | `display-discovery`, `delivery` |
| `brand-naming` | [design-brand-naming](../plugins/visual-design-studio/library/draft-skills/design-brand-naming/SKILL.md) | `brand-strategy` |
| `logo-concepts` | [design-logo-concepts](../plugins/visual-design-studio/library/draft-skills/design-logo-concepts/SKILL.md) | `identity` |
| `logo-refinement` | [design-logo-refinement](../plugins/visual-design-studio/library/draft-skills/design-logo-refinement/SKILL.md) | `logo-concepts`, `typography` |
| `logo-variants` | [design-logo-variants](../plugins/visual-design-studio/library/draft-skills/design-logo-variants/SKILL.md) | `logo-refinement` |
| `logo-evaluation` | [design-logo-evaluation](../plugins/visual-design-studio/library/draft-skills/design-logo-evaluation/SKILL.md) | `identity`, `delivery` |
| `identity-refresh` | [design-identity-refresh](../plugins/visual-design-studio/library/draft-skills/design-identity-refresh/SKILL.md) | `identity` |
| `brand-guidelines` | [design-brand-guidelines](../plugins/visual-design-studio/library/draft-skills/design-brand-guidelines/SKILL.md) | `identity` |
| `identity-delivery` | [design-identity-delivery](../plugins/visual-design-studio/library/draft-skills/design-identity-delivery/SKILL.md) | `production`, `identity` |
| `design-taste` | [design-taste](../plugins/visual-design-studio/library/draft-skills/design-taste/SKILL.md) | `reference-direction` |
| `screen-assets` | [design-screen-assets](../plugins/visual-design-studio/library/draft-skills/design-screen-assets/SKILL.md) | `display-discovery` |
| `screen-compositing` | [design-screen-compositing](../plugins/visual-design-studio/library/draft-skills/design-screen-compositing/SKILL.md) | `screen-assets` |
| `screen-original-assets` | [design-screen-original-assets](../plugins/visual-design-studio/library/draft-skills/design-screen-original-assets/SKILL.md) | `display-art-direction` |
| `screen-reconstruction` | [design-screen-reconstruction](../plugins/visual-design-studio/library/draft-skills/design-screen-reconstruction/SKILL.md) | `screen-assets` |
| `screen-dimensional` | [design-screen-dimensional](../plugins/visual-design-studio/library/draft-skills/design-screen-dimensional/SKILL.md) | `screen-assets` |
| `screen-adaptation` | [design-screen-adaptation](../plugins/visual-design-studio/library/draft-skills/design-screen-adaptation/SKILL.md) | `display-art-direction` |
| `screen-formats` | [design-screen-formats](../plugins/visual-design-studio/library/draft-skills/design-screen-formats/SKILL.md) | `display-discovery` |
| `screen-storyboard` | [design-screen-storyboard](../plugins/visual-design-studio/library/draft-skills/design-screen-storyboard/SKILL.md) | `display-content` |
| `screen-animation` | [design-screen-animation](../plugins/visual-design-studio/library/draft-skills/design-screen-animation/SKILL.md) | `screen-storyboard` |
| `screen-kinetic-type` | [design-screen-kinetic-type](../plugins/visual-design-studio/library/draft-skills/design-screen-kinetic-type/SKILL.md) | `screen-storyboard` |
| `screen-video` | [design-screen-video](../plugins/visual-design-studio/library/draft-skills/design-screen-video/SKILL.md) | `screen-assets` |
| `screen-effects` | [design-screen-effects](../plugins/visual-design-studio/library/draft-skills/design-screen-effects/SKILL.md) | `screen-storyboard` |
| `screen-loops` | [design-screen-loops](../plugins/visual-design-studio/library/draft-skills/design-screen-loops/SKILL.md) | `screen-storyboard` |
| `screen-multiscreen` | [design-screen-multiscreen](../plugins/visual-design-studio/library/draft-skills/design-screen-multiscreen/SKILL.md) | `display-discovery` |
| `screen-revisions` | [design-screen-revisions](../plugins/visual-design-studio/library/draft-skills/design-screen-revisions/SKILL.md) | `handoff` |
| `screen-localization` | [design-screen-localization](../plugins/visual-design-studio/library/draft-skills/design-screen-localization/SKILL.md) | `display-content` |
| `screen-templates` | [design-screen-templates](../plugins/visual-design-studio/library/draft-skills/design-screen-templates/SKILL.md) | `display-campaigns` |
| `touch-product-discovery` | [design-touch-product-discovery](../plugins/visual-design-studio/library/draft-skills/design-touch-product-discovery/SKILL.md) | `touchscreen-design` |
| `touch-states-copy` | [design-touch-states-copy](../plugins/visual-design-studio/library/draft-skills/design-touch-states-copy/SKILL.md) | `touchscreen-design` |
| `touch-media` | [design-touch-media](../plugins/visual-design-studio/library/draft-skills/design-touch-media/SKILL.md) | `touchscreen-design` |
| `touch-handoffs` | [design-touch-handoffs](../plugins/visual-design-studio/library/draft-skills/design-touch-handoffs/SKILL.md) | `touchscreen-design` |
| `touch-device-validation` | [design-touch-device-validation](../plugins/visual-design-studio/library/draft-skills/design-touch-device-validation/SKILL.md) | `touchscreen-design` |
| `touch-information-architecture` | [design-touch-information-architecture](../plugins/visual-design-studio/library/draft-skills/design-touch-information-architecture/SKILL.md) | `touchscreen-design` |
| `touch-interaction-patterns` | [design-touch-interaction-patterns](../plugins/visual-design-studio/library/draft-skills/design-touch-interaction-patterns/SKILL.md) | `touchscreen-design` |
| `touch-configurators` | [design-touch-configurators](../plugins/visual-design-studio/library/draft-skills/design-touch-configurators/SKILL.md) | `touch-product-discovery` |
| `touch-forms` | [design-touch-forms](../plugins/visual-design-studio/library/draft-skills/design-touch-forms/SKILL.md) | `touchscreen-design` |
| `touch-product-education` | [design-touch-product-education](../plugins/visual-design-studio/library/draft-skills/design-touch-product-education/SKILL.md) | `touch-product-discovery` |
| `touch-offline` | [design-touch-offline](../plugins/visual-design-studio/library/draft-skills/design-touch-offline/SKILL.md) | `touchscreen-design` |
| `touch-action-reliability` | [design-touch-action-reliability](../plugins/visual-design-studio/library/draft-skills/design-touch-action-reliability/SKILL.md) | `touchscreen-design` |
| `touch-usability-testing` | [design-touch-usability-testing](../plugins/visual-design-studio/library/draft-skills/design-touch-usability-testing/SKILL.md) | `touch-device-validation` |
| `screen-attention` | [design-screen-attention](../plugins/visual-design-studio/library/draft-skills/design-screen-attention/SKILL.md) | `display-content` |
| `screen-assortment` | [design-screen-assortment](../plugins/visual-design-studio/library/draft-skills/design-screen-assortment/SKILL.md) | `display-content` |
| `screen-offers` | [design-screen-offers](../plugins/visual-design-studio/library/draft-skills/design-screen-offers/SKILL.md) | `display-content` |
| `screen-data-content` | [design-screen-data-content](../plugins/visual-design-studio/library/draft-skills/design-screen-data-content/SKILL.md) | `display-campaigns` |
| `screen-playlists` | [design-screen-playlists](../plugins/visual-design-studio/library/draft-skills/design-screen-playlists/SKILL.md) | `screen-loops` |
| `screen-shelf-edge` | [design-screen-shelf-edge](../plugins/visual-design-studio/library/draft-skills/design-screen-shelf-edge/SKILL.md) | `screen-formats` |
| `screen-still-motion` | [design-screen-still-motion](../plugins/visual-design-studio/library/draft-skills/design-screen-still-motion/SKILL.md) | `screen-reconstruction` |
| `screen-finishing` | [design-screen-finishing](../plugins/visual-design-studio/library/draft-skills/design-screen-finishing/SKILL.md) | `display-production` |
| `screen-performance-learning` | [design-screen-performance-learning](../plugins/visual-design-studio/library/draft-skills/design-screen-performance-learning/SKILL.md) | `display-evaluation` |
| `screen-acceptance-records` | [design-screen-acceptance-records](../plugins/visual-design-studio/library/draft-skills/design-screen-acceptance-records/SKILL.md) | `handoff` |
| `screen-executable-tests` | [design-screen-executable-tests](../plugins/visual-design-studio/library/draft-skills/design-screen-executable-tests/SKILL.md) | `display-evaluation` |
| `screen-evaluation-examples` | [design-screen-evaluation-examples](../plugins/visual-design-studio/library/draft-skills/design-screen-evaluation-examples/SKILL.md) | `display-evaluation` |
| `screen-html-development` | [design-screen-html-development](../plugins/visual-design-studio/library/draft-skills/design-screen-html-development/SKILL.md) | `screen-data-content` |
| `screen-playback-performance` | [design-screen-playback-performance](../plugins/visual-design-studio/library/draft-skills/design-screen-playback-performance/SKILL.md) | `display-production` |
| `screen-cms-integration` | [design-screen-cms-integration](../plugins/visual-design-studio/library/draft-skills/design-screen-cms-integration/SKILL.md) | `display-production` |
| `screen-batch-rendering` | [design-screen-batch-rendering](../plugins/visual-design-studio/library/draft-skills/design-screen-batch-rendering/SKILL.md) | `screen-templates` |
| `screen-native-projects` | [design-screen-native-projects](../plugins/visual-design-studio/library/draft-skills/design-screen-native-projects/SKILL.md) | `display-production` |
| `screen-product-fidelity` | [design-screen-product-fidelity](../plugins/visual-design-studio/library/draft-skills/design-screen-product-fidelity/SKILL.md) | `screen-compositing` |
| `screen-release-verification` | [design-screen-release-verification](../plugins/visual-design-studio/library/draft-skills/design-screen-release-verification/SKILL.md) | `screen-acceptance-records` |
| `screen-troubleshooting` | [design-screen-troubleshooting](../plugins/visual-design-studio/library/draft-skills/design-screen-troubleshooting/SKILL.md) | `display-evaluation` |
| `screen-audio-captions` | [design-screen-audio-captions](../plugins/visual-design-studio/library/draft-skills/design-screen-audio-captions/SKILL.md) | `screen-video` |
| `screen-event-content` | [design-screen-event-content](../plugins/visual-design-studio/library/draft-skills/design-screen-event-content/SKILL.md) | `screen-playlists` |
| `web-discovery` | [design-web-discovery](../plugins/visual-design-studio/library/draft-skills/design-web-discovery/SKILL.md) | `research` |
| `web-audit` | [design-web-audit](../plugins/visual-design-studio/library/draft-skills/design-web-audit/SKILL.md) | `research` |
| `web-content-strategy` | [design-web-content-strategy](../plugins/visual-design-studio/library/draft-skills/design-web-content-strategy/SKILL.md) | `content` |
| `web-migration` | [design-web-migration](../plugins/visual-design-studio/library/draft-skills/design-web-migration/SKILL.md) | `web-audit` |
| `web-information-architecture` | [design-web-information-architecture](../plugins/visual-design-studio/library/draft-skills/design-web-information-architecture/SKILL.md) | `ux` |
| `web-page-architecture` | [design-web-page-architecture](../plugins/visual-design-studio/library/draft-skills/design-web-page-architecture/SKILL.md) | `ux` |
| `web-page-templates` | [design-web-page-templates](../plugins/visual-design-studio/library/draft-skills/design-web-page-templates/SKILL.md) | `web-page-architecture` |
| `web-search` | [design-web-search](../plugins/visual-design-studio/library/draft-skills/design-web-search/SKILL.md) | `web-information-architecture` |
| `web-art-direction` | [design-web-art-direction](../plugins/visual-design-studio/library/draft-skills/design-web-art-direction/SKILL.md) | `reference-direction` |
| `web-responsive` | [design-web-responsive](../plugins/visual-design-studio/library/draft-skills/design-web-responsive/SKILL.md) | `ui` |
| `web-media` | [design-web-media](../plugins/visual-design-studio/library/draft-skills/design-web-media/SKILL.md) | `reference-direction` |
| `web-system-assembly` | [design-web-system-assembly](../plugins/visual-design-studio/library/draft-skills/design-web-system-assembly/SKILL.md) | `ui` |
| `web-visual-review` | [design-web-visual-review](../plugins/visual-design-studio/library/draft-skills/design-web-visual-review/SKILL.md) | `design-taste` |
| `web-conversion` | [design-web-conversion](../plugins/visual-design-studio/library/draft-skills/design-web-conversion/SKILL.md) | `content` |
| `web-forms` | [design-web-forms](../plugins/visual-design-studio/library/draft-skills/design-web-forms/SKILL.md) | `ui` |
| `web-copy-fit` | [design-web-copy-fit](../plugins/visual-design-studio/library/draft-skills/design-web-copy-fit/SKILL.md) | `typography` |
| `web-fidelity` | [design-web-fidelity](../plugins/visual-design-studio/library/draft-skills/design-web-fidelity/SKILL.md) | `ui` |
| `web-frontend` | [design-web-frontend](../plugins/visual-design-studio/library/draft-skills/design-web-frontend/SKILL.md) | `ui` |
| `web-cms` | [design-web-cms](../plugins/visual-design-studio/library/draft-skills/design-web-cms/SKILL.md) | `web-page-templates` |
| `web-platform-adapters` | [design-web-platform-adapters](../plugins/visual-design-studio/library/draft-skills/design-web-platform-adapters/SKILL.md) | `production` |
| `web-integrations` | [design-web-integrations](../plugins/visual-design-studio/library/draft-skills/design-web-integrations/SKILL.md) | `web-forms` |
| `web-accessibility` | [design-web-accessibility](../plugins/visual-design-studio/library/draft-skills/design-web-accessibility/SKILL.md) | `prototype` |
| `web-performance` | [design-web-performance](../plugins/visual-design-studio/library/draft-skills/design-web-performance/SKILL.md) | `web-frontend` |
| `web-seo` | [design-web-seo](../plugins/visual-design-studio/library/draft-skills/design-web-seo/SKILL.md) | `web-information-architecture` |
| `web-browser-qa` | [design-web-browser-qa](../plugins/visual-design-studio/library/draft-skills/design-web-browser-qa/SKILL.md) | `prototype` |
| `web-privacy` | [design-web-privacy](../plugins/visual-design-studio/library/draft-skills/design-web-privacy/SKILL.md) | `web-discovery` |
| `web-analytics` | [design-web-analytics](../plugins/visual-design-studio/library/draft-skills/design-web-analytics/SKILL.md) | `web-discovery` |
| `web-release` | [design-web-release](../plugins/visual-design-studio/library/draft-skills/design-web-release/SKILL.md) | `delivery` |
| `web-maintenance` | [design-web-maintenance](../plugins/visual-design-studio/library/draft-skills/design-web-maintenance/SKILL.md) | `web-audit` |
| `web-commerce` | [design-web-commerce](../plugins/visual-design-studio/library/draft-skills/design-web-commerce/SKILL.md) | `web-page-templates` |
| `web-accounts` | [design-web-accounts](../plugins/visual-design-studio/library/draft-skills/design-web-accounts/SKILL.md) | `web-forms` |
| `web-localization` | [design-web-localization](../plugins/visual-design-studio/library/draft-skills/design-web-localization/SKILL.md) | `content` |
| `web-directory` | [design-web-directory](../plugins/visual-design-studio/library/draft-skills/design-web-directory/SKILL.md) | `web-search` |
| `web-editorial` | [design-web-editorial](../plugins/visual-design-studio/library/draft-skills/design-web-editorial/SKILL.md) | `web-content-strategy` |
| `web-booking` | [design-web-booking](../plugins/visual-design-studio/library/draft-skills/design-web-booking/SKILL.md) | `web-integrations` |
| `web-storytelling` | [design-web-storytelling](../plugins/visual-design-studio/library/draft-skills/design-web-storytelling/SKILL.md) | `motion` |
| `media-art-direction` | [design-media-art-direction](../plugins/visual-design-studio/library/draft-skills/design-media-art-direction/SKILL.md) | `reference-direction`, `production` |
| `chatgpt-images` | [design-chatgpt-images](../plugins/visual-design-studio/library/draft-skills/design-chatgpt-images/SKILL.md) | `production`, `media-route-selection` |
| `media-route-selection` | [design-media-route-selection](../plugins/visual-design-studio/library/draft-skills/design-media-route-selection/SKILL.md) | `media-reference-control` |
| `media-reference-control` | [design-media-reference-control](../plugins/visual-design-studio/library/draft-skills/design-media-reference-control/SKILL.md) | `media-art-direction` |
| `media-image-repair` | [design-media-image-repair](../plugins/visual-design-studio/library/draft-skills/design-media-image-repair/SKILL.md) | `media-reference-control`, `production` |
| `media-quality-evaluation` | [design-media-quality-evaluation](../plugins/visual-design-studio/library/draft-skills/design-media-quality-evaluation/SKILL.md) | `media-art-direction` |
| `media-production-recipes` | [design-media-production-recipes](../plugins/visual-design-studio/library/draft-skills/design-media-production-recipes/SKILL.md) | `media-quality-evaluation` |
