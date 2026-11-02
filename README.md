# Corpus Nova

![Corpus Nova](figures/branding/cn-lockup.png)

Open-source human-organism explorer: interactive 3D body map, VR-ready environment, universal body library, and white-paper streams that feed the map — anatomy, biology, chemistry, physics, and energy systems in one premium stack.

**License:** [MIT](LICENSE) · © 2026 Corpus Nova contributors  
Third-party anatomy meshes (e.g. BodyParts3D, HRA) keep their own licenses — attribute separately.

## Branding

Minimal identity — hollow orbit mark, open tracking wordmark, paper/ink/teal palette.  
Style guide: [`notes/branding/STYLE.md`](notes/branding/STYLE.md) · Assets: [`figures/branding/`](figures/branding/)

| Token | Hex | Use |
|-------|-----|-----|
| ink | `#0B0F14` | Text |
| paper | `#F7F5F2` | Background |
| mute | `#6B7280` | Secondary |
| line | `#E5E2DC` | Hairlines |
| signal | `#2F6F6A` | Accent / active map |
| signal-soft | `#DCEEEB` | Soft panels |

White papers use the **Nova Sheet** layout: [`templates/NOVA-SHEET.md`](templates/NOVA-SHEET.md).

![Mark pulse](figures/branding/cn-mark-pulse.gif)

## Mission — open source, real value to humanity

Give everyone free, accurate, beautiful access to how the human body works — not locked behind paywalls, not dumbed down, not stuck in dense PDFs.

- **Open source** by default: code, map payloads, library cards, and paper drafts the world can fork, audit, and improve (MIT).
- **Real value to humanity:** education, curiosity, clinical literacy, research scaffolding, and a shared public map of the organism we all live inside.
- Prefer existing open atlases (meshes/viewers) over reinventing them; add what they lack.

## Voice

PhD-worthy depth · universal readers · abstract, easy, fun, simple — **alien-technology** premium: precise, specific, non-boring, unlike textbook prose.

## What we are building

| Surface | Role |
|---------|------|
| Interactive body map | Hover organs, receptors, vessels, heart, pressures, sex layers |
| VR-ready 3D environment | Premium, power-efficient; anatomy + biology + chemistry + physics |
| Universal body library | DNA, diseases, pressures, disorders, hormones, reproduction, gut/energy, … |
| White papers (Nova Sheets) | Content sources for map/library (map-first) |

### Sex biology (required)
Hormones & chemistry; receptors; testosterone levels & testicular production; full male and female reproductive systems; dual-layer map views.

### Food & energy systems
Gut, stomach, acids, microbiome, intestine segments, sphincters, digestion, lactose intolerance, fermented reintroduction, microbiome ↔ immunity/mood, evolutionary base of *Homo sapiens*.

### Technical foundation
- **Rust** core (3D environments, rendering integration, systems)
- **NVIDIA** path: CUDA / RTX / DLSS where they earn speed and quality
- **Vector-ready** pipelines and assets
- **Lightning-fast** image generation and display
- Paper assets: transparent **PNG**, **GIF**, pictures — branding kit in `figures/branding/`

## Workspace

```
LICENSE           # MIT
white-papers/     # Nova Sheet drafts → map content
library/          # universal knowledge cards
body-map/         # region/overlay payloads + branding.md
figures/branding/ # mark, wordmark, lockup, palette, GIFs
templates/        # NOVA-SHEET.md
sources/          # citations
notes/            # SCOPE, visuals, branding/STYLE.md, sectors/
```

Sector briefs: `notes/sectors/`  
Name shortlist archive: `notes/archive/name-shortlist-2026-11-01.md`

## Repository

GitHub: [galion-studio/Corpus-Nova](https://github.com/galion-studio/Corpus-Nova)
