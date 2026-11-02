# Outline — Whole-Body Human Anatomy Overview (Theme 6)

**Status:** outline v3 (map-first + sex biology) · draft v3 landed  
**Audience:** **universal** — science, biology, anyone learning the real human body (not PhD-only)  
**Voice:** abstract, easy, fun, simple — high accuracy without stiff paper tone; gloss jargon on first use  
**Lane:** systems-level whole body + **lead for body-map region structure, integration, and the sex-layer overview**; not adipose metabolism, bone volume metrics, receptor deep-dives, cell physics, or detailed biochem

---

## Working title
**The Body as One Map: Nested Systems from Skin to Signal**

## Abstract angle (2–3 sentences)
The human body is a nested stack of compartments that stay alive by trading matter, energy, and information. This paper is a friendly flyover of that stack — systems, scales, and the three big coordinators (nervous, endocrine, immune) — Written **map-first**: every place it names becomes a region payload on the interactive body map, with a shared base and equal-depth male and female layers.

## Sections
1. **Opening frame** — organism as a closed-ish thermodynamic actor with open exchanges  
2. **Scale ladder** — molecule → cell → tissue → organ → system → organism (one tight pass)  
3. **Systems tour** (overview depth only)  
   - Integument (boundary & sensor)  
   - Musculoskeletal (scaffold & actuators)  
   - Nervous (fast wiring)  
   - Cardiovascular + pulmonary (flow & gas)  
   - Gastrointestinal (intake & transformation)  
   - Renal + endocrine (filtration & chemical broadcast)  
   - Immune + reproductive (defense & lineage; one plan, two builds)  
4. **Coordination trio** — nervous × endocrine × immune as the body’s chat layer (pointers to Receptors theme)  
5. **Homeostasis as design principle** — set points, feedback, allostasis; ♂ HPG = thermostat, ♀ HPG = clock with a positive-feedback trigger  
6. **Into the map & library** — region-ID table (`head-neck`, `thorax`, `abdomen`, `pelvis`, `upper-limb`, `lower-limb`) → `body-map/panels/whole-body-panels.json`; overlays (receptors, adipose, bone, cell physics)  
   - 6.1 **Sex layers** — shared / male_layer / female_layer; homologues; hotspot rule → `body-map/overlays/sex-layers.json`  
   - 6.2 **Hormones: dose and source** — testicular testosterone production + levels, female sources, cycle, ovarian reserve, kisspeptin ignition → `pelvis`, `head-neck`, `abdomen` payloads; `library/hormones/`, `library/male-reproductive/`, `library/female-reproductive/`  
7. **Why the map still matters** — open questions (multi-scale models, imaging, systems physiology) for curious readers at every level  
8. **Figures** · **References**

## Deliberate handoffs (do not rewrite)
- BioChem Papers → in-vivo chemistry depth  
- Cell Physics → intracellular biophysics  
- Receptors → exact receptor-level connections  
- Bone Metrics → metric volume / laterality of bone sectors  
- Adipose → how fat is built / fat metabolism (wired as an overlay, not rewritten)  
- Hormone chemistry zooms (steroidogenesis, levels detail) → BioChem cards in `library/hormones/`  

## Paper → map panel IDs
| Paper § | Payload |
|---|---|
| 1 | `panel.wb.flow-machine` |
| 2 | `panel.wb.scale-ladder` |
| 3 | `panel.wb.systems` + region payloads |
| 4 | `panel.wb.coordination-trio` |
| 5 | `panel.wb.homeostasis` |
| 6 / 6.1 / 6.2 | regions, `panel.wb.sex-layers`, `panel.wb.hormones` |
| 7 | `panel.wb.open-questions` |

Full wiring: `body-map/integration.md`.

## Figure list (papers; reused as map global-panel art)
| ID | File | Format | Role |
|----|------|--------|------|
| F1 | `figures/whole-body/whole-body-scale-ladder.png` | transparent PNG | Nested scales molecule→organism |
| F2 | `figures/whole-body/whole-body-systems-map.png` | transparent PNG | Simple labeled systems schematic |
| F3 | `figures/whole-body/whole-body-homeostasis-loop.gif` | GIF | One clear feedback-loop cycle (optional) |

## Also seeding
- `library/index.md` + whole-body entries  
- `body-map/regions/` structure for hover: organs, receptors, vessels, heart, vein pressures  
- `body-map/panels/`, `body-map/sex-layers.md`, `body-map/integration.md`, atlas recommendation in `body-map/README.md`  
- `library/hormones/` overview cards, `library/male-reproductive/`, `library/female-reproductive/`  

## Deliverables path
- Paper draft → `white-papers/whole-body-anatomy-overview.md`  
- Citations → `sources/whole-body-overview-sources.md`  
- Handoff note → `notes/whole-body-handoff.md`  

## Next
Keep payload files in sync when the paper changes (rebuild scripts in `body-map/panels/`). No new figures needed for v3; the map carries the sex-layer visuals.

---
**License:** MIT — © 2026 Corpus Nova contributors. See `/LICENSE`. Third-party atlas meshes retain their own licenses.
