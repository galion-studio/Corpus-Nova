# Steroidogenesis: how the body turns cholesterol into sex hormones

**One-liner:** Every sex hormone, in every body, comes off one shared assembly line that starts with cholesterol. Tissues just set the dials differently.

**In plain words**
- A *steroid* is four fused carbon rings. Cholesterol is the raw material.
- **The gate:** **StAR** ferries cholesterol into the mitochondria, and **CYP11A1** cuts off its tail to make **pregnenolone**. This is the rate-limiting step, so whatever opens the gate sets the output.
- **After the gate:**
  - **CYP17A1** (two jobs: hydroxylase, then lyase) → DHEA
  - **3β-HSD2** → androstenedione (or progesterone)
  - **17β-HSD3/AKR1C3** → testosterone
  - **aromatase (CYP19A1)** → estrogens
  - **5α-reductase** → DHT
- Steroid cells can't store their product, because it leaks straight through membranes. So they make it **on demand**.

**Same line, both sexes**

| | Male layer | Female layer |
|---|---|---|
| Main factory | Leydig cells (testis) | Theca + granulosa cells, then the corpus luteum (ovary) |
| Gate opener | LH | LH (theca), with FSH turning on aromatase in granulosa |
| Main products | Testosterone ~5–7 mg/day | Estradiol 36–380 µg/day; progesterone up to ~25 mg/day (mid-luteal) |
| Also makes | Estradiol (mostly via fat aromatase) | Testosterone ~0.1–0.4 mg/day |
| Adrenal share | Small (DHEA/DHEA-S) | ~25–33% of testosterone; most DHEA |

**Watch-out:** "Male hormone" and "female hormone" are shorthand. Both sexes make all of them, in different amounts.

**Map hooks:** testis → `body-map/regions/gonads-male-chemistry.md` · ovary → `body-map/regions/gonads-female-chemistry.md` · adrenal (abdomen region; Whole Body owns the anatomy).

**Sources:** Miller & Auchus 2011 (10.1210/er.2010-0013); Burger 2002 (10.1016/S0015-0282(02)02985-0); Simpson et al. 2002 (10.1146/annurev.physiol.64.081601.142703); Handelsman, Endotext 2026; Reed & Carr, Endotext 2018.
**Deep dive:** White paper 01 §7 and Fig 5 (`figures/biology-chemistry/biology-chemistry-steroid-pathway.png`).
**Physics angle:** `body-map/cell-physics/sex-steroidogenic-packing.md` (Cell Physics) · **Receptors:** AR/ER/PR → `library/receptors/` (Theme 3).
