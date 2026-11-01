# Outline — Bone Volume Metrics: Sectors & Laterality

**Theme 4** · Human Anatomy & Biology  
**Status:** outline locked 2026-11-01 · full draft in progress  
**Audience:** universal (science, biology, anyone learning the body) — accurate, not PhD-only  
**Voice:** abstract, easy, fun, simple  
**Figures:** transparent PNG / GIF / pictures only → `figures/bone-volume/`  
**Architecture:** MAP-FIRST — paper feeds skeletal overlays + library cards  
**Also feeds:** `body-map/overlays/bone-volume-overlays.json` · hover notes · `library/bone-metrics/`  
**Atlas:** reuse BodyParts3D / Z-Anatomy / human-atlas meshes (see notes/github-anatomy-landscape.md)  
**Sex biology:** bone metric differences only (peak mass, geometry); do not own reproductive systems

---

## 1. Hook
Bone is not one lump of “hard stuff.” Volume lives in different *rooms* of the same bone, and the left and right rooms rarely match. This paper compares those volumes by sector and by side.

## 2. What “volume” means here
- Total bone volume (TV) vs bone volume (BV)
- Cortical volume (Ct.V) vs trabecular volume (Tb.V)
- Cross-sectional area (CSA) and cortical thickness as cousins of volume
- Brief glosses; no stiff nomenclature dump

## 3. Sector comparisons (same bone, different places)
- Proximal / midshaft / distal thirds (long bones: femur, tibia, humerus, radius)
- Epiphysis / metaphysis / diaphysis
- Cortical shell vs trabecular core (compartments as “sectors” of tissue type)
- Periosteal vs endosteal envelopes (where volume is added or lost)
- Typical human ranges / ratios from primary literature (QCT, μCT, histomorphometry) — cite, do not invent

## 4. Side / laterality comparisons
- Left–right asymmetry of volume, CSA, cortical geometry
- Handedness and habitual loading as drivers
- Bones with clearer laterality signals (humerus, radius, metacarpals) vs more symmetric ones (some lower-limb sites)
- Magnitude of asymmetry when literature reports it

## 5. How volume is measured (light methods)
- DXA (areal proxy — what it misses)
- QCT / pQCT (true volumetric)
- μCT and clinical CT
- MRI for marrow / trabecular estimates where relevant
- One concrete “why the number changes with the tool” example

## 5b. Sex differences in bone metrics
- Peak bone mass timing/amount (averages + overlap)
- Geometry / CSA / cortical area differences
- Aging curves (incl. post-menopausal patterns as bone metrics, not gyno deep-dive)
- Map: dual-layer notes; library: sex-differences.md

## 6. Why the differences matter
- Loading history written into sector volumes
- Fracture risk and where bone is thin
- Interpreting bilateral scans without mistaking asymmetry for pathology
- Keep playful; no clinical protocol lecture

## 7. Closing
One idea to leave with: volume is local and often lopsided — compare sectors and sides before treating a bone as a single number.

## 8. References
Primary papers + DOIs/stable URLs in `sources/bone-volume-sources.md` (filled during draft).

---

## Figure list (planned → `figures/bone-volume/`)

| # | File | Type | What it shows |
|---|------|------|----------------|
| F1 | `bone-volume-sector-map.png` | transparent PNG | Long-bone cartoon: proximal / midshaft / distal sectors labeled |
| F2 | `bone-volume-cortical-trabecular.png` | transparent PNG | Cross-section: cortical shell volume vs trabecular core volume |
| F3 | `bone-volume-left-right.png` | transparent PNG | Left vs right schematic with volume / CSA asymmetry callouts |
| F4 | *(optional)* `bone-volume-envelopes.gif` | simple GIF | Periosteal expansion vs endosteal change over a short loop |

All graphics: simple, clean, no UI chrome, transparent backgrounds for PNGs.

---


## Cross-surfaces (brief update 2026-11-01)
- **Body map (primary):** sector/laterality overlays in `body-map/overlays/bone-volume-overlays.json` + hover notes; bind to BodyParts3D/human-atlas mesh names.
- **Sex:** bone-geometry dual-layer notes; no reproductive-system ownership.
- **Library:** seed bone-metric entries under `library/` (volume terms, asymmetry, measurement modes, related disorders as pointers only — do not own other themes’ disease deep-dives).
- Paper figures stay PNG/GIF/pictures; map UI is separate.

## Next step
Full draft: `white-papers/bone-volume-sectors-laterality.md` + figures + sources.
