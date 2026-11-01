# Whole-Body theme — handoff note (2026-11-01)

**Paper:** `white-papers/whole-body-anatomy-overview.md` (**draft v3**: map-first + sex biology; 4,421 words, up from 3,011)
**Figures:** `figures/whole-body/whole-body-scale-ladder.png`, `whole-body-systems-map.png` (transparent PNG), `whole-body-homeostasis-loop.gif` (transparent GIF, 48 frames, loops)
**Sources:** `sources/whole-body-overview-sources.md`

## What this paper covers
- The body as an open flow system with four jobs: wall, move, swap, talk
- Scale ladder: molecule → cell → tissue → organ → system → organism (with cell counts)
- Overview tour of the systems in seven job-based groups
- Coordination trio (nervous × endocrine × immune) at the "who talks to whom" level
- Homeostasis as the design principle (feedback, layered redundancy, allostasis)
- How the paper maps onto the interactive body map regions and the library's whole-body shelf
- Open questions (multi-scale models, newly found anatomy, "reference human" bias, set points, microbiome)

## What it deliberately leaves to sibling themes
| Theme | Left to them |
|---|---|
| **BioChem Papers** | In-vivo chemistry, metabolic pathways, buffers, ATP/redox detail |
| **Cell Physics** | Why cells are the size they are, crowding, diffusion, forces inside cells |
| **Receptors** | Which receptor carries each signal, binding and signalling detail (paper only says "right receiver") |
| **Bone Metrics** | Bone volumes by sector and left/right side (paper only gives ~206 bones and bone's roles) |
| **Adipose** | How fat is built and stored, depots, adipogenesis (paper only lists fat as a hormone-making connective tissue) |

## Library / map
- **Whole Body owns map structure + the sex-layer overview.** Receptors still owns receptor deep-dives; BioChem owns hormone chemistry zoom cards; Adipose, Bone, Cell Physics own their overlays.
- Map extracts (v3): `body-map/panels/whole-body-panels.json` (6 regions + 8 global panels), `body-map/overlays/sex-layers.json` (25 ♂/♀/shared structures), index `body-map/panels/README.md`, rebuild scripts in `body-map/panels/`.
- Docs: `body-map/README.md` (atlas recommendation: slorksmo/Human-Atlas primary), `body-map/sex-layers.md`, `body-map/integration.md` (adipose, receptors, bone, cell-physics overlays wired by reference, not rewritten).
- Library shelves seeded: `library/hormones/` overview cards (overview, testosterone, estrogen-progesterone, hpg-axis — README is BioChem's combined index, do not overwrite), `library/male-reproductive/`, `library/female-reproductive/`.
- Region IDs in paper §6 mirror `body-map/regions/index.md` and the panels JSON; if regions are renamed, update all three and re-run the build scripts.
- Vein-pressure numbers are NOT given in this paper; they live in `library/pressures/vein-pressures.md`.
