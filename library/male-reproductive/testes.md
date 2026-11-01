# Testes — card

**One-liner:** two egg-sized organs that run two factories at once — sperm in the tubules, testosterone in the gaps between them.

Map: `pelvis.testis` (L/R) · `male_layer`

## Structure
- **Size:** roughly 4–5 cm long each; adult volume commonly ~15–25 mL [4].
- **Capsule:** tough *tunica albuginea*; septa divide each testis into ~250 lobules, each packed with 1–4 coiled **seminiferous tubules** [4].
- **Inside the tubules:** **Sertoli cells** ("nurse cells") wrap developing germ cells and form the **blood–testis barrier** via tight junctions, hiding later-stage germ cells from the immune system [4, 7].
- **Between the tubules (interstitium):** **Leydig cells**, ~500 million in total, make testosterone under LH [18].

## Two factories
| Factory | Cells | Driver | Product |
|---|---|---|---|
| Sperm | germ cells + Sertoli cells | FSH + very high local testosterone | spermatozoa (one wave takes ~64 days; Amann argues this may be off by ~6 days) [29, 30] |
| Hormone | Leydig cells | LH | testosterone, 3–10 mg/day (mean ~7 mg) [18] |

Local testosterone inside the testis is ~**100× the blood level** [17] — see `library/hormones/testosterone.md`.

## Cooling and plumbing
- The **scrotum** keeps the testes a few °C below core temperature; spermatogenesis is heat-sensitive [7].
- **Pampiniform venous plexus** wraps the testicular artery as a counter-current heat exchanger [4].
- **Testicular arteries** arise from the abdominal aorta (near L2) because the testes develop high in the abdomen and descend through the **inguinal canal**, dragging their vessels with them [4].
- **Venous asymmetry:** right testicular vein → inferior vena cava; **left → left renal vein** (a longer, right-angled path — one reason varicoceles are mostly left-sided) [4]. The ovarian veins share exactly this pattern.

## Hover payload
```yaml
id: pelvis.testis
layer: male_layer
title: "Testis — sperm + testosterone factory"
summary: "Tubules make sperm; Leydig cells between them make ~7 mg testosterone a day."
organs: [testis, seminiferous tubules, Sertoli cells, Leydig cells, tunica albuginea]
vessels: [testicular artery (aorta), pampiniform plexus, testicular vein (R→IVC, L→renal)]
hormones: [testosterone, inhibin B, estradiol (small)]
receptor_pointers: [LHCGR (Leydig), FSHR (Sertoli), AR (Sertoli, peritubular)]
atlas_mesh: {male_body: [FJ3138 Left testis, FJ3142 Right testis]}
library: [library/male-reproductive/testes.md, library/hormones/testosterone.md]
```
