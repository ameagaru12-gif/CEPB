# Choosing a use case

[日本語](../ja/USE_CASES.md) | [Home](../../README.md)

Classes select the capabilities being evaluated. They do not rank a character's worth by budget, company size, or avatar format.

| Development or use case | Start with | Detailed evaluation | Conditions to retain |
|---|---|---|---|
| Independent developer, prototype, model migration | Quick | Core | Character definition, model/prompt version, actual question, output, missingness |
| Text chat, game dialogue, canon-bound character | Quick | Core / CANON | Canon versus operational experience, immutable core, current constraints, anonymous settings |
| Characters with changing relationships and states | Quick | Core / BOUNDED | Allowed variation, mood versus disposition, reasons for change and stability |
| Experience reinterpretation under RST | Quick | Core / RST plus separate specialist analysis | Storage → retrieval → actual input → semantic use → later judgment → new outcome; do not score change frequency |
| Voice characters or bidirectional speech | Core | Voice: 60 items / 660 points | Actual playback, input, and interruption in I; output-only systems retain unsupported I5 or other required items as 0 |
| Still images, sprites, Live2D, or 3D display | Core | Avatar: 60 / 660 | Actual display, identity, appropriate expression, load; format names earn no points |
| Apps coordinating avatar and voice | Core | Multimodal: 72 / 790 | H/I/J, subtitle–speech meaning, gaze, lip movement, timing, interruptions |
| Virtual worlds, external tools, or robots | Core | World: 66 / 720 | K/L, world tags, sensors, commands, receipts, stopping, partial outcomes |
| Research on experienced character presence | Raw ratings separate from functional grades | Integrated's O | Target population, at least 12 participants per condition stratum, allocation, raw 1–7 ratings, separate repair observations |
| Integrated product maturity and long-term lineage | Core and focused classes | Integrated: 96 / 1000 | All capabilities, O, P, certified scope, real calendar time, missingness, components |
| Public comparison, papers, commercial performance claims | Matching class above | Add Verified review | Independence, rerun scope, conflicts, attributable reviewers, unverified claims |

## Fixed denominators

| Class | Domains | Items | Maximum |
|---|---|---:|---:|
| Core | A–G, M, N | 54 | 590 |
| Voice | Core + I | 60 | 660 |
| Avatar | Core + H | 60 | 660 |
| Multimodal | Core + H, I, J | 72 | 790 |
| World | Core + K, L | 66 | 720 |
| Integrated | A–P | 96 | 1000 |

World's virtual, digital, and physical tags are not assumed to have interchangeable difficulty. Match environments, action scope, and stopping contracts for direct comparison. A narrower output-only voice or avatar-only class must declare its own name, version, and fixed denominator in advance; do not mix it with completed default Voice or Integrated scores.

## Accessibility

Declare usable input, display, language, and controls for the target population. Record subtitles, modes without speech, and assistive input, and compare experiences within that population. A participant's inability to use a medium is different from an unsupported system capability. If required conditions change, record a corresponding extension version.
