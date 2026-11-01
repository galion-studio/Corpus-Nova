# Hormones — overview card

**One-liner:** a hormone is a chemical letter mailed through the blood; the receptor is the mailbox that decides who reads it.

## Three chemical families
| Family | Built from | Travels | Receptor location | Examples |
|---|---|---|---|---|
| **Peptides / proteins** | amino-acid chains | dissolved in plasma | cell surface | insulin, GnRH, LH, FSH, oxytocin |
| **Amines** | single amino acids (tyrosine, tryptophan) | mostly dissolved (thyroid hormone bound) | surface (adrenaline) or nuclear (T3/T4) | adrenaline, thyroid hormone, melatonin |
| **Steroids** | cholesterol | mostly bound to carrier proteins | inside the cell (nuclear receptors) | testosterone, estradiol, progesterone, cortisol, aldosterone |

Steroids are greasy, so they slip through membranes and act on DNA directly via nuclear receptors — slower (hours) but long-lasting. Peptides cannot cross membranes, so they knock on surface receptors and trigger fast second-messenger cascades [7, 19].

## Main glands (map pointers)
| Gland | Region ID | Key outputs |
|---|---|---|
| Hypothalamus | `head-neck.hypothalamus` | GnRH, CRH, TRH, GHRH, oxytocin & vasopressin (via posterior pituitary) |
| Pituitary | `head-neck.pituitary` | LH, FSH, ACTH, TSH, GH, prolactin |
| Thyroid | `head-neck.thyroid` | T4, T3, calcitonin |
| Adrenals | `abdomen.adrenal` | cortisol, aldosterone, adrenaline, DHEA/DHEA-S (adrenal androgen precursors) |
| Pancreatic islets | `abdomen.pancreas` | insulin, glucagon |
| **Testes** (♂) | `pelvis.testis` | testosterone, inhibin B, AMH (fetal), small estradiol |
| **Ovaries** (♀) | `pelvis.ovary` | estradiol, progesterone, inhibins A/B, AMH, androgens |
| "Non-gland" makers | various | heart (ANP), gut (GLP-1, ghrelin), kidney (EPO, renin), bone (FGF23), fat (leptin) |

## Transport: bound vs free
Sex steroids ride in blood mostly bound to **SHBG** (sex hormone–binding globulin, tight grip) and **albumin** (loose grip); only about **2%** of testosterone is free in normal men [21]. Free + loosely bound = "bioavailable" hormone. That is why a lab "total testosterone" can mislead if SHBG is unusually high or low [16].

## Sex differences at a glance
- Both sexes make **all** the sex steroids; the difference is **dose and source** [18].
- Men: circulating testosterone ~15-fold higher than women after puberty; almost all of it from testicular Leydig cells [18].
- Women: testosterone comes from ovary, adrenal, and peripheral conversion in roughly equal thirds [18]; estradiol and progesterone swing through a ~monthly cycle [24].
- Men make estradiol too, mostly by aromatase (CYP19A1) converting testosterone in fat, bone, brain, and testis [19].

## Links
- Deeper: [`testosterone.md`](testosterone.md) · [`estrogen-progesterone.md`](estrogen-progesterone.md) · [`hpg-axis.md`](hpg-axis.md)
- Receptors: `library/receptors/` (Receptors theme)
- Paper: `white-papers/whole-body-anatomy-overview.md` §3.6, §6
