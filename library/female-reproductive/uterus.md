# Uterus — card

**One-liner:** a pear-sized muscle with a lining that rebuilds itself every month, ready to host a pregnancy and, at birth, to push one out.

Map: `pelvis.uterus` · `pelvis.cervix` · `female_layer`

## Parts
| Part | Gloss |
|---|---|
| **Fundus** | dome above where the tubes enter (the *cornua*) |
| **Body** | main chamber |
| **Lower uterine segment / isthmus** | narrow waist; thins in late pregnancy |
| **Cervix** | 2–3 cm neck; *internal os* (into uterus) and *external os* (into vagina); mucus changes with the cycle [4, 7] |

## Wall layers
- **Endometrium** — lining. *Functional layer* grows under estradiol, turns secretory under progesterone, and sheds at menstruation; *basal layer* stays and regrows it [7].
- **Myometrium** — thick smooth muscle; contractions in labor are amplified by oxytocin via OXTR (positive feedback) → see Receptors overlay `uterus`.
- **Perimetrium** — outer peritoneal skin.

## Supports
Broad ligament (sheet), **round ligament** (to labia majora via inguinal canal — remnant of the gubernaculum, the same cord that guides testicular descent), **cardinal** and **uterosacral** ligaments (main cervix supports) [4].

## Blood supply
**Uterine artery** from the internal iliac; crosses **over** the ureter near the cervix ("water under the bridge") — the female mirror of the vas deferens crossing [4]. Anastomoses with the ovarian artery.

## Hover payloads
```yaml
- id: pelvis.uterus
  layer: female_layer
  title: "Uterus — the self-rebuilding room"
  summary: "Muscle wall + monthly lining; estradiol builds it, progesterone readies it, oxytocin contracts it."
  hormones: [estradiol, progesterone, oxytocin]
  receptor_pointers: [ESR1, PGR, OXTR]
  overlays: [receptors-overlays.json#uterus]
  vessels: [uterine artery L/R, uterine vein L/R]
  atlas_mesh: {female_body: [HRAF0435 Body of uterus, HRAF0436 Fundus of uterus, HRAF0437 Cornua, HRAF0438 Lower uterine segment, HRAF0439 Posterior wall, HRAF0440 Anterior wall, HRAF0427 Broad ligament, HRAF0417/0418 Round ligaments, HRAF0419/0420 Uterosacral, HRAF0421/0422 Cardinal]}
- id: pelvis.cervix
  layer: female_layer
  title: "Cervix — the gatekeeper"
  summary: "Mucus thin and stretchy near ovulation, thick under progesterone."
  atlas_mesh: {female_body: [HRAF0441 Cervix, HRAF0442 Internal os, HRAF0443 External os, HRAF0407 Cervicovaginal junction]}
```
