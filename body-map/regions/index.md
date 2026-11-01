# Body-map regions — index

| Region ID | File | Primary reveals |
|-----------|------|-----------------|
| head-neck | `head-neck.md` | brain, sensory organs, carotids/jugulars |
| thorax | `thorax.md` | heart (pump), lungs, great vessels, pressures |
| abdomen | `abdomen.md` | GI organs, liver/portal, kidneys |
| pelvis | `pelvis.md` | reproductive/urinary overview |
| blood-vessels-chemistry | `blood-vessels-chemistry.md` | Biology & chemistry overlay: plasma ions, pH buffer, O₂/CO₂, glucose |
| heart-metabolic-chemistry | `heart-metabolic-chemistry.md` | Biology & chemistry overlay: heart fuel, ATP turnover, phosphocreatine |
| pelvis.testis (male_layer) | `gonads-male-chemistry.md` | Biology & chemistry overlay: testosterone pathway, levels, LH loop |
| pelvis.ovary (female_layer) | `gonads-female-chemistry.md` | Biology & chemistry overlay: two-cell estradiol, progesterone, cycle loop |
| upper-limb | `upper-limb.md` | muscles/bones overview, peripheral veins |
| lower-limb | `lower-limb.md` | same pattern; venous return |

Each region file lists: organs[], vessels[], receptor_pointers[], heart_pump (bool/notes), vein_pressures_ref.

Chemistry overlay files (`*-chemistry.md`) add a hover payload block (one_liner, key_numbers, pathway_steps, loop, library, cross_links, sources, do_not). They come from white paper 01.

## Layers and payload files (Whole Body, v3)
- Every region has `layers{shared, male_layer, female_layer}`; only `pelvis` (and `thorax.breast`) differ by sex in anatomy. Scheme: `../sex-layers.md`.
- Machine-readable region payloads: `../panels/whole-body-panels.json` (index `../panels/README.md`); sex-layer child IDs (`pelvis.testis`, `pelvis.ovary`, `head-neck.pituitary`, …): `../overlays/sex-layers.json`.
- Overlay IDs (adipose depots, receptors, bone bands) per region: `../integration.md` §4.
