# Region payload: male gonad chemistry (`pelvis.testis`, male_layer)

*Biology & chemistry hover payload. It sits on top of the Whole Body anatomy card (`library/male-reproductive/testes.md`) and the Receptors panel (`body-map/overlays/receptors-sex-hormones-panel.md`, block `testis.leydig`), without repeating them. Long-form source: white paper 01 §7.1–7.3, §7.6–7.7. Fields match `gonads-female-chemistry.md` one for one.*

| Field | Payload |
|---|---|
| region_id | `pelvis.testis` (chemistry sublayer `biochem.sex-steroid`) |
| layer | `male_layer` |
| organs | testis → Leydig cells (interstitium) |
| vessels | testicular artery / pampiniform plexus (the anatomy is Whole Body's) |
| receptor_pointers | LHCGR, AR → `library/receptors/` |
| heart_pump | false |
| vein_pressures_ref | `library/pressures/vein-pressures.md` |

## Hover payload
```yaml
id: pelvis.testis.chem
layer: male_layer
title: "Testosterone refinery"
one_liner: "Cholesterol in, ~5–7 mg testosterone out per day, through one LH-controlled mitochondrial door."
key_numbers:
  - "Output ~5–7 mg/day (3–10) — Handelsman, Endotext 2026"
  - "Blood range 264–916 ng/dL (9.2–31.8 nmol/L), men 19–39 — Travison 2017"
  - "Inside the testis ≈ 40–100× blood — Jarow & Zirkin 2005"
  - "8 a.m. > 4 p.m. by 20–25% (age 30–40) — Brambilla 2009"
  - "In blood: ~44% SHBG, ~50% albumin, ~1–3% free — Dunn 1981; Goldman 2017"
pathway_steps:   # same keys as the female payload
  gate: "StAR → CYP11A1: cholesterol → pregnenolone (rate-limiting)"
  branch: "CYP17A1 (+ b5): → 17-OH-pregnenolone → DHEA"
  middle: "HSD3B2: DHEA → androstenedione"
  finish: "HSD17B3 (testis-specific): → testosterone"
  downstream: "~4% → DHT (5α-reductase type 2, prostate/genital skin); ~0.2% → estradiol (aromatase; most male E2 is made in fat)"
loop:
  type: "negative feedback (thermostat)"
  path: "GnRH pulses → LH → Leydig cAMP → T (+ E2) → brakes GnRH/LH"
  rhythm: "pulsatile LH; morning peak"
glance_animation: "cholesterol beads stream into a mitochondrion; gate glows on each LH pulse"
figure: "figures/biology-chemistry/biology-chemistry-steroid-pathway.png (blue = male route)"
library:
  - library/hormones/testicular-testosterone-production.md
  - library/hormones/testosterone-levels.md
  - library/male-reproductive/leydig-steroidogenesis.md
  - library/hormones/steroidogenesis-overview.md
cross_links:
  anatomy: library/male-reproductive/testes.md            # Whole Body
  receptors: library/receptors/ar.md                       # Receptors
  cell_physics: body-map/cell-physics/sex-steroidogenic-packing.md
  adipose: library/adipose-metabolism/sex-hormones-and-fat.md
twin: body-map/regions/gonads-female-chemistry.md
sources: sources/biology-chemistry-paper1-sources.md#d-sex-steroid-chemistry-7-male-and-female-payloads
do_not: "No receptor mechanics (Receptors), no anatomy meshes (Whole Body), no dosing or medical advice."
```

**Short hover (three lines, for small screens):**
> **Testosterone refinery.** LH opens one door (StAR), and cholesterol becomes about 6 mg of testosterone a day.
> Inside the testis it's ~100× blood level, which is what sperm production needs.
> In blood, only ~2% rides free. Most is on SHBG and albumin.
