# Male ducts — card

**One-liner:** a one-way conveyor that collects sperm, matures them for about two weeks, and then fires them through the prostate into the urethra.

Map: `pelvis.epididymis` · `pelvis.vas-deferens` · `pelvis.ejaculatory-duct` · `pelvis.urethra-male` · `male_layer`

## The route (in order)
| # | Segment | Gloss | Notes |
|---|---|---|---|
| 1 | Seminiferous tubules | where sperm are made | inside testis |
| 2 | Straight tubules → **rete testis** | collecting network | in mediastinum testis |
| 3 | **Efferent ductules** | ~12–20 small exits | reabsorb fluid, concentrating sperm [4] |
| 4 | **Epididymis** (head → body → tail) | finishing school; a single duct about 6 m long when uncoiled | sperm gain motility and fertilizing ability here; tail stores them [4, 7] |
| 5 | **Vas (ductus) deferens** | muscular pipe, ~30–45 cm | runs in the spermatic cord, through the inguinal canal, **over the ureter**, behind the bladder; widens into the ampulla [4] |
| 6 | **Ejaculatory duct** | vas + seminal-vesicle duct joined | ~2 cm, passes *through* the prostate [4] |
| 7 | **Urethra** (prostatic → membranous → spongy) | shared exit for urine and semen | ~18–20 cm in total [4] |

Anatomy echo: the vas deferens crosses **over** the ureter; in the female layer the **uterine artery** crosses over the ureter at nearly the same spot — the classic "water under the bridge" landmark [4].

## Hover payloads
```yaml
- id: pelvis.epididymis
  layer: male_layer
  title: "Epididymis — sperm finishing school"
  summary: "A ~6 m coiled tube where sperm learn to swim."
  atlas_mesh: {male_body: [FJ3136 Left epididymis, FJ3141 Right epididymis]}
- id: pelvis.vas-deferens
  layer: male_layer
  title: "Vas deferens — the express pipe"
  summary: "Carries sperm from scrotum, through the groin, over the ureter, to the prostate."
  atlas_mesh: {male_body: [FJ3135 Left deferent duct, FJ3140 Right deferent duct]}
- id: pelvis.ejaculatory-duct
  layer: male_layer
  title: "Ejaculatory duct"
  summary: "Where vas meets seminal vesicle; tunnels through the prostate."
  atlas_mesh: {male_body: []}   # not a separate BodyParts3D mesh → hotspot marker
- id: pelvis.urethra-male
  layer: male_layer
  title: "Male urethra — shared exit"
  summary: "Urine and semen share it, never at the same time (sphincters + reflexes)."
  atlas_mesh: {male_body: [FJ3148 Urethra]}
```
