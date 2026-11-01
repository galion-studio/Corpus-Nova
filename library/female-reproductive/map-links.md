# Female reproductive — map region links

Mesh IDs verified 2026-11-01 against `public/models/atlas-female.json` in **slorksmo/Human-Atlas** (female body = Human Reference Atlas *3D Reference Organ Set for Female* v1.10, CC BY 4.0).

| Region ID | Label | Atlas mesh (HRA female) | Card | Hormone / receptor pointers |
|---|---|---|---|---|
| `pelvis.ovary` | Ovary L / R | HRAF0432 / HRAF0433 | `ovaries.md` | E2, P4, inhibins, AMH · FSHR, LHCGR, ESR1/2, PGR |
| `pelvis.ovary` (supports) | Suspensory lig. R/L · ovarian lig. L/R · mesovarium R/L | HRAF0423/0424 · HRAF0425/0426 · HRAF0430/0431 | `ovaries.md` | — |
| `pelvis.uterine-tube` | Ampulla, isthmus, fimbriae, infundibulum (R: 0408–0411, L: 0412–0415) · abdominal ostium · mesosalpinx | HRAF0408–0415 · HRAF0434 · HRAF0428/0429 | `tracts.md` | ESR1, PGR (ciliary/muscle tone) |
| `pelvis.uterus` | Body, fundus, cornua, lower segment, walls | HRAF0435–0440 | `uterus.md` | ESR1, PGR, **OXTR** (→ `overlays/receptors-overlays.json#uterus`) |
| `pelvis.uterus` (supports) | Broad · round L/R · uterosacral L/R · cardinal L/R · uterovesical pouch | HRAF0427 · HRAF0417/0418 · HRAF0419/0420 · HRAF0421/0422 · HRAF0416 | `uterus.md` | — |
| `pelvis.cervix` | Cervix · internal os · external os · cervicovaginal junction | HRAF0441 · HRAF0442 · HRAF0443 · HRAF0407 | `uterus.md` | ESR1, PGR |
| `pelvis.vagina` | Vagina | HRAF0406 | `tracts.md` | ESR1 |
| `pelvis.vulva` | Vulva | *not in HRA v1.10* → hotspot | `tracts.md` | AR, ESR1 |
| `pelvis.clitoris` | Clitoris | *not in HRA v1.10* → hotspot | `tracts.md` | AR, ESR1 |
| `thorax.breast` | Mammary lobes L / R | HRAF0008 / HRAF0018 | `tracts.md` | ESR1, PGR, PRLR, OXTR |
| pelvic vessels | Uterine artery L / R · uterine vein L / R | HRAF0629 / HRAF0630 · HRAF0631 / HRAF0632 | `uterus.md` | — |
| shared pelvic vessels | Internal iliac vein L / R · internal pudendal vein L / R | HRAF0661 / 0662 · HRAF0663 / 0664 | `body-map/regions/pelvis.md` | — |
| HPG top floor (shared) | Hypothalamus L / R | HRAF0338 / HRAF0339 | `../hormones/hpg-axis.md` | GnRH |

Gaps in the female source (no pituitary/adrenal mesh found by name; no ovarian artery mesh; no vulva/clitoris) are filled with **hotspot markers** — never by borrowing male meshes (see `body-map/sex-layers.md`).
