# Corpus Nova — branding & style guide

**Identity:** minimal · precise · alien-technology clarity · open source  
**License:** MIT (see `/LICENSE`). Third-party anatomy meshes keep their own licenses (CC BY / CC BY-SA) — attribute separately.

## Logo
- Wordmark: **CORPUS NOVA** in Inter / system sans, tracking slightly open
- Mark: hollow circle with a single offset inner arc (orbit / cell / field) — one stroke, no fill noise
- Formats: transparent **PNG** + simple **GIF** (soft pulse of the arc only)
- Clear space: ≥ height of the “N” around the mark
- Do not add gradients, drop shadows, 3D bevels, or busy UI chrome

## Color palette (minimal)
| Token | Hex | Use |
|-------|-----|-----|
| `ink` | `#0B0F14` | Primary text |
| `paper` | `#F7F5F2` | Page background |
| `mute` | `#6B7280` | Secondary text |
| `line` | `#E5E2DC` | Rules / hairlines |
| `signal` | `#2F6F6A` | Accent (links, active map) |
| `signal-soft` | `#DCEEEB` | Soft highlight panels |
| `alert` | `#8B3A3A` | Rare warnings only |

Dark map UI may invert `ink`/`paper` but keep `signal` unchanged.

## Typography
- UI / papers: **Inter** (or system UI sans) — 16–18 px body, 1.55 line-height
- Titles: same family, weight 600, never all-caps except the logo wordmark
- Mono for IDs / gene names: **JetBrains Mono** or system mono
- No decorative display faces

## White paper presentation (“Nova Sheet”)
1. Thin top rule in `signal`
2. Title + one-line dek
3. Meta line: theme · audience · MIT · date
4. Abstract in a soft `signal-soft` panel (no border radius > 4 px conceptually; keep flat)
5. Body: short sections, hairline `line` dividers
6. Figures: transparent PNG / GIF only; captions in `mute`
7. Closing: Sources + License one-liner
8. Map callout boxes: left bar `signal`, title “Map panel”

Template: `templates/NOVA-SHEET.md`

## Body map / GitHub / Page
- Same palette and wordmark everywhere
- Map chrome: hairlines + `signal` active region only
- README hero: wordmark PNG + one sentence mission + MIT badge text
