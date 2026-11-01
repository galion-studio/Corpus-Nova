# Ovarian steroidogenesis (cell-level chemistry)

**One-liner:** The ovary splits the assembly line between two neighboring cells and then rebuilds it every month. Theca cells make androgen, granulosa cells finish it into estradiol, and after ovulation both become a progesterone factory.

**Where it sits:** in the walls of the growing follicles, then in the corpus luteum (the "yellow body" left behind after ovulation). Anatomy: [ovaries.md](ovaries.md).

**Two cells, two gonadotropins (follicular phase)**

| | Theca cell (outer layer, has blood supply) | Granulosa cell (inner layer, no blood vessels) |
|---|---|---|
| Doorbell | **LH** → LHCGR → cAMP | **FSH** → FSHR → cAMP (LHCGR added late) |
| Has | StAR, CYP11A1, **CYP17A1**, HSD3B2 | **CYP19A1 (aromatase)**, **HSD17B1** |
| Lacks | aromatase | CYP17A1 (can't make androgen) |
| Makes | **androstenedione** (+ some testosterone) | **estrone → estradiol** |
| Hand-off | androgen diffuses inward through the basement membrane | ← receives it and aromatizes it |

Neither cell can make estradiol alone. That's why an LH or FSH defect, or a missing aromatase, leaves the cycle without its estrogen peak.

**After ovulation (luteal phase)**
- LH turns both cell types into **luteal cells**, and blood vessels grow into the old granulosa layer, bringing LDL cholesterol.
- StAR, CYP11A1, and HSD3B2 run flat out, so the line **stops at progesterone**: ~25 mg/day at mid-luteal, against ~1 mg/day in the follicular phase.
- Aromatase stays on, so estradiol stays at ~250 µg/day.
- The corpus luteum lasts **~14 days** unless hCG from a pregnancy rescues it.

**Output across the cycle** (ovary + periphery; Baird & Fraser 1974, tabulated in Reed & Carr 2018)
- **E2:** 36 → 380 → 250 µg/day
- **P4:** 1 → 4 → 25 mg/day
- **Testosterone:** ~0.1–0.4 mg/day in total. About a quarter to a third comes from the ovary, mostly theca and stroma.

**Control loop:** most of the time this is a negative brake. When E2 stays above ~200 pg/mL for ~50 h, the loop flips to positive feedback, triggering the **LH surge**, and ovulation follows ~34–36 h later. Details: `../hormones/estradiol-progesterone.md`, `cycle.md`.

**Sources:** Reed & Carr, Endotext 2018; Hillier, Whitelaw & Smyth 1994 (10.1016/0303-7207(94)90278-X); Miller & Auchus 2011 (10.1210/er.2010-0013); Simpson et al. 2002 (10.1146/annurev.physiol.64.081601.142703); Baird & Fraser 1974 (10.1210/jcem-38-6-1009); Burger 2002 (10.1016/S0015-0282(02)02985-0).

**Links**
- Map: `../../body-map/regions/gonads-female-chemistry.md` (`pelvis.ovary`, female_layer)
- Physics: `../../body-map/cell-physics/sex-steroidogenic-packing.md`, `sex-oocyte-crowding.md`
- Receptors (FSHR, LHCGR, ESR1/2, PGR): `../receptors/`
- Equal-depth twin: `../male-reproductive/leydig-steroidogenesis.md`
