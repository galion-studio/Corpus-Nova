# Panels — payloads extracted from the Whole Body paper

**Source:** `white-papers/whole-body-anatomy-overview.md` (Draft v3) · cites → `sources/whole-body-overview-sources.md`
**Machine file:** [whole-body-panels.json](whole-body-panels.json) — rebuild with `python3 body-map/panels/build_whole_body_panels.py`
**Sex-layer child structures:** [../overlays/sex-layers.json](../overlays/sex-layers.json) — rebuild with `python3 body-map/panels/build_sex_layers.py`
All mesh IDs were checked against the slorksmo/Human-Atlas manifests (2026-11-01); all overlay IDs against the sibling overlay files.

## Region payloads (hover → panel)

| Region ID | Paper § | Panel title | Layers | Adipose depots | Receptor overlay IDs (sample) | Bone bands |
|---|---|---|---|---|---|---|
| `head-neck` | 3.3, 4, 6.2 | Command deck | shared (HPG floors) | `depot.brown.supraclavicular` | `brain.hypothalamus.kiss-gnrh`, `pituitary.anterior` | — |
| `thorax` | 3.4 | Two pumps and a gas swap | shared + female_layer (breast) | `depot.epicardial`, `depot.brown.supraclavicular` | `heart`, `breast` | — |
| `abdomen` | 3.5, 3.6 | Intake, processing, filtering | shared (+ adrenal androgen note per layer) | `depot.subcutaneous.abdominal`, `depot.visceral.omental_mesenteric`, `depot.perirenal` | — | `bone.vertebra.body` |
| `pelvis` | 3.6, 3.7, 6.1 | Filter exit + lineage | shared + **male_layer** + **female_layer** | `depot.gluteofemoral` | `testis.leydig`, `ovary.follicle.theca`, `uterus` … | `bone.femur.neck` |
| `upper-limb` | 3.2, 3.4 | Levers and return pipes | shared | — | — | humerus, radius bands |
| `lower-limb` | 3.2, 3.4 | Pillars and the calf pump | shared | `depot.gluteofemoral` | — | femur, tibia bands |

Each region carries the hover fields `title, summary, jobs, systems, organs, vessels, receptor_pointers, heart_pump, vein_pressures_ref, facts[{text, cite}]`, plus `layers{shared, male_layer, female_layer}`, `atlas{male_body, female_body}`, `overlays{receptors, adipose, bone}`, `library[]`.

## Pelvis ♂ / ♀ (child structures in `sex-layers.json`)

| male_layer | Mesh IDs | female_layer | Mesh IDs |
|---|---|---|---|
| `pelvis.testis` | FJ3138, FJ3142 | `pelvis.ovary` | HRAF0432/0433 (+ supports 0423–0426, 0430/0431) |
| `pelvis.epididymis` | FJ3136, FJ3141 | `pelvis.uterine-tube` | HRAF0408–0415, 0434, 0428/0429 |
| `pelvis.vas-deferens` | FJ3135, FJ3140 | `pelvis.uterus` | HRAF0435–0440, ligaments 0416–0422, 0427, vessels 0629–0632 |
| `pelvis.seminal-vesicle` | FJ3137, FJ3143 | `pelvis.cervix` | HRAF0441–0443, 0407 |
| `pelvis.prostate` | FJ3139 | `pelvis.vagina` | HRAF0406 |
| `pelvis.penis` | FJ3132–3134 | `pelvis.clitoris` | hotspot |
| `pelvis.urethra-male` | FJ3148 | `pelvis.vulva` | hotspot |
| `pelvis.spermatic-cord` (testicular a./v.) | FJ3532, FJ3617, FJ3533, FJ3618 | `thorax.breast` | HRAF0008, HRAF0018 |
| `pelvis.ejaculatory-duct`, `pelvis.bulbourethral`, `pelvis.scrotum` | hotspot | `pelvis.vestibular-glands`, `pelvis.paraurethral` | hotspot |

Shared: `head-neck.hypothalamus` (FJ1760/FJ1808 · HRAF0338/0339), `head-neck.pituitary` (FJ1796 · female hotspot), `abdomen.adrenal` (FJ3129/FJ3130 · female hotspot), `pelvis.bladder` (FJ3149 · HRAF0609–0612).

## Global panels (not tied to one region)

| Panel ID | Paper § | Shows |
|---|---|---|
| `panel.wb.flow-machine` | 1 | Four job badges: wall · move · swap · talk (+ lineage) |
| `panel.wb.scale-ladder` | 2 | Molecule → organism; cell counts ♂/♀/child |
| `panel.wb.systems` | 3 | System-layer toggles (seven teams) |
| `panel.wb.coordination-trio` | 4 | Nervous / endocrine / immune timing |
| `panel.wb.homeostasis` | 5 | Feedback loop; ♂ thermostat vs ♀ clock |
| `panel.wb.sex-layers` | 6.1 | Same blueprint, two builds |
| `panel.wb.hormones` | 6.2 | Dose and source; testosterone numbers |
| `panel.wb.open-questions` | 7 | Blank spots on the map |

## Testosterone facts carried by `pelvis.male_layer`
~500 million Leydig cells make 3–10 mg/day (mean ~7) [18] · LH → LHCGR → cAMP → StAR → CYP11A1 → CYP17A1 → HSD3B2 → HSD17B3 [19, 20] · intratesticular ≈ 100× serum [17] · 264–916 ng/dL in healthy non-obese men 19–39 y [16] · ~20–25% higher at 08:00 than 16:00 at age 30–40 [22] · total T falls ~1.6%/yr in mid-life [23].
