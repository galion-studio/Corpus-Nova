# Interactive body map

Hover a region → see organs, receptors (pointers), blood vessels, heart pumping, and vein pressures.

- Region data: `regions/`  
- Presentation: project Page / interactive surface (not paper figure GIFs alone)  
- Natural overview owner: Whole Body theme; Receptors / Bone / Adipose supply depth via links  

Start at [regions/index.md](regions/index.md).

---

## Map-first: how this folder is organised

The papers feed the map. Every white paper section that describes a place in the body ends up here as a **payload**: small, cited, machine-readable data a viewer shows on hover or in a side panel. We do **not** build our own 3D meshes or viewer.

| Layer | File(s) | Owner |
|---|---|---|
| Region skeleton (6 regions + sub-IDs) | [regions/index.md](regions/index.md), `regions/*.md` | Whole Body |
| **Region + global panel payloads** (extracted from the Whole Body paper) | [panels/whole-body-panels.json](panels/whole-body-panels.json) · index [panels/README.md](panels/README.md) | Whole Body |
| **Sex layers** (shared / male_layer / female_layer) | [sex-layers.md](sex-layers.md) · [overlays/sex-layers.json](overlays/sex-layers.json) | Whole Body (overview); depth in `library/male-reproductive/`, `library/female-reproductive/`, `library/hormones/` |
| Receptor overlay | [overlays/receptors-overlays.json](overlays/receptors-overlays.json), [overlays/receptors-sex-hormones-panel.md](overlays/receptors-sex-hormones-panel.md) | Receptors |
| Adipose depot overlay | [overlays/adipose-depots.json](overlays/adipose-depots.json), [adipose-regions.md](adipose-regions.md) | Adipose |
| Bone volume overlay | [overlays/bone-volume-overlays.json](overlays/bone-volume-overlays.json), [bone-volume-hover-notes.md](bone-volume-hover-notes.md) | Bone |
| Cell-physics zoom panels | [cell-physics/](cell-physics/) | Cell physics |
| **How it all wires together** | [integration.md](integration.md) | Whole Body |

---

## Which open-source atlas we build on (evaluated 2026-11-01)

**One-liner:** Use **slorksmo/Human-Atlas** as the primary viewer (MIT, the only one with *both* a male and a female body including reproductive meshes, all with stable mesh IDs), keep **ashemag/human-atlas** as its upstream/male-only fallback, borrow **open-anatomy-studio**'s lesson/hotspot content pattern, and treat **Z-Anatomy** as reference only (ShareAlike, male only).

| Project | What it is | Bodies | Licence (code / data) | Fit for us |
|---|---|---|---|---|
| [slorksmo/Human-Atlas](https://github.com/slorksmo/Human-Atlas) (demo: atlas.taim.best) | Static React + Three.js explorer, extends ashemag's codebase | **Male** (BodyParts3D 4.0) **+ female** (HRA female v1.10: 1,220 structures, 1,439 concepts, 18 systems) | MIT / CC BY 4.0 (BodyParts3D, HRA, Andreassen 2023 leg muscles); Wikidata CC0 | **Primary.** Only option that meets the equal ♂/♀ requirement with real reproductive meshes. Manifests `public/models/atlas.json` + `atlas-female.json` give per-mesh IDs (`FJ####` male, `HRAF####` female) we can key payloads to. Gap fills (180 borrowed male bones, 76 Andreassen leg muscles) are already labelled as separate, off-by-default systems. Small community (17★) → pin a commit. |
| [ashemag/human-atlas](https://github.com/ashemag/human-atlas) (demo: human-atlas-seven.vercel.app) | Same stack; the original | Male only (2,234 meshes, 3,432 concepts, 15 systems) | MIT / CC BY 4.0 (BodyParts3D) | **Upstream + fallback.** More mature and popular (≈4.4k★, active Sept 2026). Same male mesh IDs as slorksmo, so male payloads work in both. Fails the female-layer requirement alone. |
| [HongChao6/open-anatomy-studio](https://github.com/HongChao6/open-anatomy-studio) | Next.js + React Three Fiber learning studio | 12 HRA VH-male organ models | MIT / CC BY 4.0 (HRA) | **Pattern donor.** Too few meshes to be the atlas, but its content contract (`topics → lessons → scenes → hotspots → sources`) is the right shape for paper → panel binding. We copy the idea, not the app. |
| [Z-Anatomy/Models-of-human-anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy) | Blender atlas template (+ Unity app, browser port) | Male only | **CC BY-SA 4.0** (some sub-models CC BY-NC(-SA)) | **Reference only.** Rich labels, but ShareAlike would bind derivatives and some parts forbid commercial use. No female body. |

### How we inject payloads (no fork of the meshes)

1. **Load** the atlas as-is (slorksmo build, pinned commit). Male = `atlas.json`, female = `atlas-female.json`.
2. **Load our overlays** alongside: `panels/whole-body-panels.json` (regions + global panels), `overlays/sex-layers.json`, plus sibling overlays (receptors, adipose, bone).
3. **Bind by ID.** Each payload lists `atlas.male_body` (`FJ####`) and `atlas.female_body` (`HRAF####`) mesh IDs. Hover/click on a mesh → look up which payload lists that ID → show its `hover` fields in the detail panel.
4. **Sex toggle** = switch manifest *and* switch layer: male body shows `shared` + `male_layer`; female body shows `shared` + `female_layer`. Homologues (testis ↔ ovary, penis ↔ clitoris…) carry a `homolog` field for a "compare" button.
5. **Missing meshes → hotspots** (`hotspot_only: true` or `female_hotspot`): a labelled pin, never a borrowed opposite-sex mesh.
6. **Overlays are toggles**, not new geometry: adipose depots, receptors, bone bands, HPG arrows.

### Attribution we must ship (in the viewer's About panel)

- BodyParts3D © Database Center for Life Science (DBCLS), **CC BY 4.0** (DBCLS licence page, updated 2025-02-27; older OBJ headers say CC BY-SA 2.1 JP — the current page governs). Mitsuhashi et al., *NAR* 2009;37:D782–D785.
- Human Reference Atlas (HuBMAP / CNS Indiana), female 3D reference organs v1.10, **CC BY 4.0** — cite humanatlas.io (the HRA DOI quoted by slorksmo did not resolve when checked).
- Andreassen et al. 2023, *Sci Data* 10 (VHF leg muscles, gap fill), **CC BY 4.0**.
- Wikidata labels **CC0**. Viewer code: slorksmo/Human-Atlas & ashemag/human-atlas, **MIT**.
- If any Z-Anatomy asset is ever used: **CC BY-SA 4.0** and the derivative must stay ShareAlike.

Full evaluation notes: `../notes/github-anatomy-landscape.md`.
