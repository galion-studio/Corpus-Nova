# Ovaries — card

**One-liner:** two almond-sized organs that hold a lifetime's egg supply from before birth and turn a few of them, one cycle at a time, into hormone-making follicles.

Map: `pelvis.ovary` (L/R) · `female_layer`

## Structure
- **Size:** about 3 × 2 × 1 cm each in reproductive years [4].
- **Cortex** holds follicles; **medulla** holds vessels and nerves [4].
- **Hangers:** *suspensory ligament of the ovary* (carries the ovarian artery & vein), *ovarian ligament* (to the uterus), *mesovarium* (fold of the broad ligament) [4].
- **Vessels:** ovarian arteries arise from the abdominal aorta (the ovaries, like testes, start high and descend — less far); right ovarian vein → IVC, **left → left renal vein**, the same asymmetry as the testicular veins [4].

## Follicle life story
| Stage | What it is | Driver |
|---|---|---|
| Primordial | egg + one flat cell layer; the "savings account" | none (dormant) |
| Primary / secondary | egg + growing granulosa layers; theca recruited | local factors, then FSH |
| Antral | fluid cavity forms; makes estradiol | FSH (granulosa aromatase) + LH (theca androgens) |
| Dominant / pre-ovulatory | one follicle wins, ~2 cm | rising estradiol → positive feedback → **LH surge** |
| Ovulation | follicle ruptures, egg released to tube | LH surge |
| Corpus luteum | collapsed follicle becomes a gland | LH; makes progesterone + estradiol for ~12 days [24] |

"Two cells, two gonadotropins": theca cells (LH) make androgen; granulosa cells (FSH) aromatize it to estradiol [7, 19].

## Ovarian reserve (non-growing follicles)
- Fixed before birth and falls with age; menopause at ~**50–51 years** [27].
- By age **30**, on average only **~12%** of the peak pre-birth pool remains; by **40**, **~3%** [27].
- Age alone explains ~81% of the variation between women [27].
- Recruitment rate rises from birth to ~14 years, then declines [27].

## Ovarian androgen (often forgotten)
The ovary also secretes testosterone and androstenedione; in women circulating testosterone comes ~⅓ ovary, ~⅓ adrenal, ~⅓ peripheral conversion [18, 26].

## Hover payload
```yaml
id: pelvis.ovary
layer: female_layer
title: "Ovary — egg bank + hormone clock"
summary: "Holds the lifetime egg supply; each cycle one follicle matures and makes estradiol, then progesterone."
organs: [ovary, follicles, corpus luteum, theca cells, granulosa cells]
vessels: [ovarian artery (aorta), ovarian vein (R→IVC, L→renal)]
hormones: [estradiol, progesterone, inhibin A/B, AMH, testosterone, androstenedione]
receptor_pointers: [FSHR (granulosa), LHCGR (theca, luteal), ESR1/ESR2, PGR]
atlas_mesh: {female_body: [HRAF0432 Left ovary, HRAF0433 Right ovary]}
library: [library/female-reproductive/ovaries.md, library/hormones/estrogen-progesterone.md]
```
