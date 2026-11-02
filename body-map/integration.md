# Integration — paper sections → region payloads → viewer panels

**Owner:** Whole Body (Theme 6) leads the region structure and wiring. Each theme keeps ownership of its own files; this page only points to them.

```
white-papers/*.md ──extract──▶ body-map/panels/*.json + overlays/*.json ──bind by mesh ID──▶ viewer (slorksmo/Human-Atlas)
        │                              ▲                                                │
        └──── library/*/ cards ────────┘ (panel "dig deeper" links)                    └─ detail panel shows hover fields
```

## 1. Pipeline (same for every theme)
1. **Write** the paper section (cited).
2. **Extract** each place-based claim into a payload: region ID, layer, `hover` fields, integer cites, mesh IDs.
3. **Link** a library card for depth (`library: [...]`).
4. **Bind** to the atlas: `atlas.male_body` = `FJ####` (BodyParts3D 4.0), `atlas.female_body` = `HRAF####` (HRA female v1.10). No mesh → hotspot.
5. **Show:** hover = title + one-line summary; click = panel with facts, layer tabs, overlay chips, library links.

## 2. Region IDs (the shared spine)
Top level: `head-neck`, `thorax`, `abdomen`, `pelvis`, `upper-limb`, `lower-limb` (see `regions/index.md`).
Children use dot paths: `pelvis.testis`, `pelvis.ovary`, `head-neck.pituitary`, `thorax.breast` … (full list in `overlays/sex-layers.json`).
Sibling overlays may use their own IDs (`brain.pvn`, `testis.leydig`, `depot.gluteofemoral`, `bone.femur.neck`). Whole Body region payloads **reference** those IDs in `overlays{}`; we never rename them.

## 3. Whole Body paper → payload map

| Paper section | Payload(s) | Viewer panel |
|---|---|---|
| §1 Opening (four jobs) | `panel.wb.flow-machine`; `hover.jobs` on every region | job badges |
| §2 Scale ladder | `panel.wb.scale-ladder` | global panel + figure |
| §3.1 Integument | (whole-body skin layer; no region payload yet) | system toggle |
| §3.2 Musculoskeletal | `upper-limb`, `lower-limb` (+ bone overlay bands) | limb panels |
| §3.3 Nervous & senses | `head-neck` | command-deck panel |
| §3.4 Cardio-pulmonary | `thorax` (`heart_pump: true` → `regions/heart-pump.md`) | pump panel |
| §3.5 Digestive | `abdomen` | intake panel |
| §3.6 Renal & endocrine | `abdomen` (kidney, adrenal), `pelvis` (bladder), `head-neck` (pituitary) | endocrine chips |
| §3.7 Immune & reproductive | `pelvis.layers.male_layer` / `female_layer`; `thorax.breast` | sex-layer panels |
| §4 Coordination trio | `panel.wb.coordination-trio` | global |
| §5 Homeostasis | `panel.wb.homeostasis`; HPG arrows | global + arrow overlay |
| §6 Into the map | region table → `panels/whole-body-panels.json` | all regions |
| §6.1 Sex layers | `panel.wb.sex-layers`, `overlays/sex-layers.json` | body switch + compare |
| §6.2 Hormones | `panel.wb.hormones`; `layers.*.hormones`; testosterone facts | hormone chips |
| §7 Open questions | `panel.wb.open-questions` | global |

## 4. Overlay layers (all toggles, no new geometry)

| Overlay layer | File | Owner | Region links from Whole Body payloads |
|---|---|---|---|
| **Sex layers** (`shared` / `male_layer` / `female_layer`) | `overlays/sex-layers.json`, `sex-layers.md` | Whole Body | pelvis (children), thorax.breast, head-neck HPG floors, abdomen.adrenal |
| **HPG arrows** (`hormones.hpg`) | `library/hormones/hpg-axis.md` (copy); arrows drawn between region IDs | Whole Body + hormones shelf | head-neck → pelvis |
| **Receptors** (`receptors.connection`, `receptors.sex-steroid`, `receptors.hpg-axis`) | `overlays/receptors-overlays.json`, `overlays/receptors-sex-hormones-panel.md` | Receptors | head-neck (brain.*, pituitary.anterior), thorax (heart, breast), pelvis (testis.*, ovary.*, uterus.* …) |
| **Adipose depots** (`sex_toggle`, gynoid/android) | `overlays/adipose-depots.json`, `adipose-regions.md`; depth `library/adipose-metabolism/`; paper `white-papers/adipose-01-how-fat-is-built.md` | Adipose | see table below |
| **Bone volume** (sector bands, laterality, sex) | `overlays/bone-volume-overlays.json`, `bone-volume-hover-notes.md` | Bone | limbs, vertebra, femur neck |
| **Cell physics** (zoom-in panels) | `cell-physics/` (incl. `sex-sperm-flagellar.md`, `sex-oocyte-crowding.md`, `sex-steroidogenic-packing.md`) | Cell physics | testis, ovary, heart, vessels, brain |
| **Chemistry notes** | `regions/blood-vessels-chemistry.md`, `regions/heart-metabolic-chemistry.md`; hormone chemistry cards in `library/hormones/` | Biology & chemistry | vessels, heart, gonads |

### Adipose depot IDs per region (referenced, not rewritten)
| Region | Depot IDs (from `overlays/adipose-depots.json`) |
|---|---|
| `head-neck` | `depot.brown.supraclavicular` |
| `thorax` | `depot.brown.supraclavicular`, `depot.epicardial` |
| `abdomen` | `depot.subcutaneous.abdominal`, `depot.visceral.omental_mesenteric`, `depot.perirenal` |
| `pelvis` | `depot.gluteofemoral` |
| `lower-limb` | `depot.gluteofemoral` |
The adipose overlay's `male`/`female`/`shared` sex keys line up with our `male_layer`/`female_layer`/`shared` (alias table in `sex-layers.md`). Sex-hormone ↔ fat links: `library/adipose-metabolism/sex-hormones-and-fat.md` ↔ `library/hormones/estrogen-progesterone.md`, `library/hormones/testosterone.md`.

## 5. Viewer binding (slorksmo/Human-Atlas)
- Load `atlas.json` (male) or `atlas-female.json` (female) unchanged.
- Build a lookup `meshId → [payload IDs]` from `panels/whole-body-panels.json` + `overlays/sex-layers.json` (+ sibling overlays via their `atlas_binding` / `mesh_binding` fields).
- On hover: top-level region title + summary. On click: panel with layer tabs (shared / ♂ / ♀), facts with cites, overlay chips (adipose, receptors, bone, cell physics), library links.
- Hotspots: payloads with `hotspot_only` or `female_hotspot` get a pin placed near the named anchor.
- Attribution panel: see `README.md`.

## 6. Checks before a Page build
- Every mesh ID resolves in the pinned manifests (the build scripts in `panels/` were checked 2026-11-01).
- Every overlay ID referenced exists in its sibling file.
- Every number has an integer cite in the theme's sources file.
- No opposite-sex mesh appears in a layer without a label.
