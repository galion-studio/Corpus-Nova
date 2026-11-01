# Male reproductive — map region links

Mesh IDs verified 2026-11-01 against `public/models/atlas.json` in **slorksmo/Human-Atlas** (male body = BodyParts3D 4.0; same IDs as **ashemag/human-atlas**). FMA = Foundational Model of Anatomy concept ID.

| Region ID | Label | Atlas mesh (BodyParts3D) | FMA | Card | Hormone / receptor pointers |
|---|---|---|---|---|---|
| `pelvis.testis` | Testis L / R | FJ3138 / FJ3142 | FMA7212 / FMA7211 | `testes.md` | testosterone, inhibin B · LHCGR, FSHR, AR |
| `pelvis.epididymis` | Epididymis L / R | FJ3136 / FJ3141 | FMA18257 / FMA18256 | `ducts.md` | AR (androgen-dependent function) |
| `pelvis.vas-deferens` | Deferent duct L / R | FJ3135 / FJ3140 | FMA19236 / FMA19235 | `ducts.md` | α1-adrenergic (emission) |
| `pelvis.seminal-vesicle` | Seminal vesicle L / R | FJ3137 / FJ3143 | FMA19388 / FMA19387 | `accessory-glands.md` | AR |
| `pelvis.prostate` | Prostate | FJ3139 | FMA9600 | `accessory-glands.md` | DHT · AR, SRD5A2 |
| `pelvis.penis` | Corpora cavernosa / spongiosum / glans | FJ3132 / FJ3133 / FJ3134 | FMA19618 / FMA19617 / FMA18247 | `accessory-glands.md` | NO–cGMP (PDE5) |
| `pelvis.urethra-male` | Urethra | FJ3148 | (urinary system mesh) | `ducts.md` | — |
| `pelvis.ejaculatory-duct` | Ejaculatory duct | *no separate mesh* → hotspot | — | `ducts.md` | — |
| `pelvis.bulbourethral` | Bulbourethral gland | *no separate mesh* → hotspot | — | `accessory-glands.md` | — |
| `pelvis.scrotum` | Scrotum | *no separate mesh* → hotspot | — | `testes.md` | — |
| `pelvis.spermatic-cord` vessels | Testicular artery L / R · testicular vein L / R | FJ3532 / FJ3617 · FJ3533 / FJ3618 | FMA14760 / FMA14759 · FMA14345 / FMA14341 | `testes.md` | — |
| shared pelvic vessels | Internal iliac artery L / R | FJ3468 / FJ3569 | FMA18810 / FMA18809 | `body-map/regions/pelvis.md` | — |
| HPG top floors (shared) | Hypothalamus · Pituitary | FJ1760 / FJ1808 · FJ1796 | FMA62008 · FMA13889 | `../hormones/hpg-axis.md` | GnRH, LH, FSH |
| Adrenal (shared) | Adrenal L / R | FJ3129 / FJ3130 | FMA15630 / FMA15629 | `../hormones/overview.md` | DHEA (minor ♂ androgen source) |
