# Female reproductive system — library shelf

**One-liner:** two ovaries that release one egg (usually) per cycle and run a monthly hormone clock, plus a muscular uterus and a tract built to receive sperm, host a pregnancy, and deliver a baby.

Equal-depth twin of [`../male-reproductive/`](../male-reproductive/README.md). Map layer: **`female_layer`** of region `pelvis` (see `body-map/sex-layers.md`).

| Card | File | Covers | Map region IDs |
|------|------|--------|----------------|
| Ovaries | [`ovaries.md`](ovaries.md) | follicles, theca/granulosa, corpus luteum, ovarian reserve, ligaments, vessels | `pelvis.ovary` |
| Uterus | [`uterus.md`](uterus.md) | fundus/body/cervix, endometrium/myometrium, ligaments, uterine artery | `pelvis.uterus` · `pelvis.cervix` |
| Tracts & external genitalia | [`tracts.md`](tracts.md) | uterine tubes, vagina, vulva, clitoris, vestibular glands, breast pointer | `pelvis.uterine-tube` · `pelvis.vagina` · `pelvis.vulva` · `pelvis.clitoris` · `thorax.breast` |
| Cycle overview | [`cycle.md`](cycle.md) | menstrual / follicular / ovulation / luteal phases with real-world numbers | `pelvis.ovary` + `pelvis.uterus` (animated state) |
| Ovarian steroidogenesis | [`ovarian-steroidogenesis.md`](ovarian-steroidogenesis.md) | cell-level chemistry: two-cell model, luteal progesterone line, output across the cycle (Biology & chemistry, paper 01 §7.4) | `pelvis.ovary` |
| Map region links | [`map-links.md`](map-links.md) | region ID ↔ atlas mesh ID ↔ card ↔ hormone pointers | all of the above |

Hormones: [`../hormones/estrogen-progesterone.md`](../hormones/estrogen-progesterone.md) · [`../hormones/hpg-axis.md`](../hormones/hpg-axis.md) · [`../hormones/testosterone.md`](../hormones/testosterone.md) (§4, female sources)
Receptor-level detail (ESR1/2, PGR, OXTR, FSHR, LHCGR): **Receptors** theme. Fat-pattern effects of estrogen: **Adipose**.
