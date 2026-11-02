# Region: pelvis

**Hover reveals**

| Field | Seed content |
|-------|----------------|
| organs | Bladder, reproductive organs, rectum |
| vessels | Iliac vessels |
| receptor_pointers | Hormonal receptors (→ Receptors) |
| heart_pump | false |
| vein_pressures_ref | library/pressures/vein-pressures.md |

**Status:** structure seed — fill exact IDs, hit-areas, and cited pressure numbers before interactive Page build.

**Chemistry sublayer (`biochem.sex-steroid`):** male → [`gonads-male-chemistry.md`](gonads-male-chemistry.md) (`pelvis.testis`) · female → [`gonads-female-chemistry.md`](gonads-female-chemistry.md) (`pelvis.ovary`). Source: white paper 01 §7.

## Panel extract (Whole Body v3) → `../panels/whole-body-panels.json#pelvis` + `../overlays/sex-layers.json`

**Title:** Filter exit + lineage — same blueprint, two builds.

| Layer | Structures (region IDs) | Vessels | Hormones | Receptor pointers (→ Receptors) |
|---|---|---|---|---|
| shared | `pelvis.bladder` (FJ3149 · HRAF0609–0612), rectum, pelvic floor | internal iliac a. (FJ3468/FJ3569), internal iliac v. (HRAF0661/0662), internal pudendal v. (HRAF0663/0664) | — | — |
| male_layer | `pelvis.testis`, `.epididymis`, `.vas-deferens`, `.seminal-vesicle`, `.prostate`, `.penis`, `.urethra-male`, `.spermatic-cord`; hotspots `.ejaculatory-duct`, `.bulbourethral`, `.scrotum` | testicular a. (aorta), pampiniform plexus, testicular v. (R→IVC, L→left renal) | testosterone, DHT, inhibin B, estradiol (aromatized) | AR, LHCGR, FSHR, SRD5A2, CYP19A1 |
| female_layer | `pelvis.ovary`, `.uterine-tube`, `.uterus`, `.cervix`, `.vagina`; hotspots `.vulva`, `.clitoris`, `.vestibular-glands`, `.paraurethral` | ovarian a. (aorta), ovarian v. (R→IVC, L→left renal), uterine a./v. (HRAF0629–0632) | estradiol, progesterone, inhibin A/B, AMH, testosterone | ESR1, ESR2, PGR, OXTR, FSHR, LHCGR, AR |

**Testosterone facts (male_layer, cited in `sources/whole-body-overview-sources.md`):** ~500 M Leydig cells make 3–10 mg/day, mean ~7 [18] · LH → LHCGR → cAMP → StAR → CYP11A1 → CYP17A1 → HSD3B2 → HSD17B3 [19, 20] · intratesticular ≈ 100× serum [17] · 264–916 ng/dL, men 19–39 y [16] · 08:00 > 16:00 by 20–25% (30–40 y) [22] · −1.6%/yr mid-life [23].
**Female facts:** cycle 29.3 d (follicular 16.9, luteal 12.4) [24] · ~12% follicle reserve at 30 y, ~3% at 40 y [27] · testosterone 0–1.7 nmol/L [18].
**Overlays:** adipose `depot.gluteofemoral`; bone `bone.femur.neck`; receptors `testis.*`, `ovary.*`, `uterus.*`, `prostate`, `cervix`, `vagina` …; chemistry `gonads-male-chemistry.md` / `gonads-female-chemistry.md` (BioChem); cell physics `../cell-physics/sex-*.md`.
**Library:** `library/male-reproductive/`, `library/female-reproductive/`, `library/hormones/`.
