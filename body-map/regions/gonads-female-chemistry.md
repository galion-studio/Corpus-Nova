# Region payload: female gonad chemistry (`pelvis.ovary`, female_layer)

*Biology & chemistry hover payload. It sits on top of the Whole Body anatomy card (`library/female-reproductive/ovaries.md`) and the Receptors panel (`body-map/overlays/receptors-sex-hormones-panel.md`), without repeating them. Long-form source: white paper 01 §7.1–7.2, §7.4–7.7. Fields match `gonads-male-chemistry.md` one for one.*

| Field | Payload |
|---|---|
| region_id | `pelvis.ovary` (chemistry sublayer `biochem.sex-steroid`) |
| layer | `female_layer` |
| organs | ovary → follicle (theca + granulosa) → corpus luteum |
| vessels | ovarian artery / vein (the anatomy is Whole Body's) |
| receptor_pointers | FSHR, LHCGR, ESR1/2, PGR → `library/receptors/` |
| heart_pump | false |
| vein_pressures_ref | `library/pressures/vein-pressures.md` |

## Hover payload
```yaml
id: pelvis.ovary.chem
layer: female_layer
title: "Two-cell estrogen relay"
one_liner: "Theca cells make androgen, granulosa cells turn it into estradiol; after ovulation the same tissue becomes a progesterone factory."
key_numbers:
  - "Estradiol made per day: ~36 → 380 → 250 µg (early follicular → pre-ovulatory → mid-luteal) — Baird & Fraser 1974"
  - "Progesterone made per day: ~1 → 4 → 25 mg — Reed & Carr, Endotext 2018"
  - "Blood P4 <1 ng/mL before ovulation vs ~10–20 mid-luteal (assay-dependent)"
  - "LH surge after E2 >200 pg/mL for ~50 h; ovulation ~34–36 h after the surge starts"
  - "Testosterone ~20–70 ng/dL, ~0.1–0.4 mg/day (ovary + adrenal + periphery) — Burger 2002"
  - "E2 in blood: ~78% albumin, ~20% SHBG, ~2% free — Dunn 1981"
pathway_steps:   # same keys as the male payload
  gate: "StAR → CYP11A1: cholesterol → pregnenolone (rate-limiting; theca, then luteal cells)"
  branch: "theca CYP17A1: → DHEA (LH-driven)"
  middle: "HSD3B2: → androstenedione; luteal phase stops here → progesterone"
  finish: "granulosa CYP19A1 aromatase + HSD17B1: androstenedione → estrone → estradiol (FSH-driven)"
  downstream: "Peripheral aromatase in fat dominates after menopause (estrone)"
loop:
  type: "negative feedback that flips to positive once per cycle (clock)"
  path: "GnRH → FSH/LH → follicle E2 ↑ → (sustained high E2) → LH surge → ovulation → corpus luteum P4 + E2 → brake → luteolysis (~14 d) → FSH rises again"
  rhythm: "~28–29 day oscillator"
glance_animation: "androgen dots hop from the outer theca ring into the granulosa ring and turn pink (estradiol); after ovulation the follicle turns gold (progesterone)"
figure: "figures/biology-chemistry/biology-chemistry-steroid-pathway.png (pink = female route)"
library:
  - library/hormones/estradiol-progesterone.md
  - library/female-reproductive/ovarian-steroidogenesis.md
  - library/hormones/testosterone-levels.md
  - library/hormones/steroidogenesis-overview.md
cross_links:
  anatomy: library/female-reproductive/ovaries.md           # Whole Body
  cycle: library/female-reproductive/cycle.md
  receptors: library/receptors/esr1.md                       # Receptors
  cell_physics: body-map/cell-physics/sex-steroidogenic-packing.md
  adipose: library/adipose-metabolism/sex-hormones-and-fat.md
twin: body-map/regions/gonads-male-chemistry.md
sources: sources/biology-chemistry-paper1-sources.md#d-sex-steroid-chemistry-7-male-and-female-payloads
do_not: "No receptor mechanics (Receptors), no anatomy meshes (Whole Body), no fertility or dosing advice."
```

**Short hover (three lines, for small screens):**
> **Two-cell estrogen relay.** Theca cells make androgen, and granulosa cells (driven by FSH) turn it into estradiol.
> Once estradiol stays high for about 2 days, the brake flips to an accelerator, triggering the LH surge and ovulation.
> Afterwards the corpus luteum makes up to ~25 mg of progesterone a day for ~14 days.
