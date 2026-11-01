# Sex layers — one blueprint, two builds

**Owner:** Whole Body (map structure + sex-layer overview). Receptor depth stays with Receptors; organ depth lives in `library/male-reproductive/` and `library/female-reproductive/`; hormone depth in `library/hormones/`.
**Data:** [overlays/sex-layers.json](overlays/sex-layers.json) (25 structures) · region-level layers inside [panels/whole-body-panels.json](panels/whole-body-panels.json).

## The idea in one breath
Most of the body is the same in everyone. The pelvis (and the breast) is where the two builds differ, and the hormone *doses* differ everywhere. So the map has a **shared** base and two swappable layers. Both get equal depth.

## Layer IDs (canonical)

| ID | Shown on | Body / mesh source | Examples |
|---|---|---|---|
| `shared` | both bodies | both manifests | hypothalamus, pituitary, adrenal, bladder, iliac vessels |
| `male_layer` | male body | BodyParts3D 4.0 (`FJ####`) | testis, epididymis, vas deferens, seminal vesicle, prostate, penis, male urethra, testicular vessels |
| `female_layer` | female body | HRA female v1.10 (`HRAF####`) | ovary, uterine tube, uterus, cervix, vagina, breast, uterine vessels |

**Aliases:** sibling overlays use `male` / `female` / `both` (adipose, receptors, bone). Treat them as `male_layer` / `female_layer` / `shared`. Do not rename sibling files.

## Toggle behaviour
1. **Body switch** (Male / Female) swaps the atlas manifest *and* the visible layer: male = `shared + male_layer`; female = `shared + female_layer`.
2. **Reproductive system** is off by default in slorksmo/Human-Atlas. Turning on the "Sex layers" overlay should switch it on for the current body.
3. **Compare** button on any structure with a `homolog` jumps to its counterpart on the other body.
4. Sibling overlays (adipose, receptors, bone) filter by the same switch using their own `sex`/`sex_layer` field.

## Homologue pairs (same embryonic origin)
| male_layer | female_layer | Shared origin |
|---|---|---|
| `pelvis.testis` | `pelvis.ovary` | gonadal ridge |
| `pelvis.penis` | `pelvis.clitoris` | genital tubercle |
| `pelvis.scrotum` | `pelvis.vulva` (labia majora) | labioscrotal folds |
| `pelvis.prostate` | `pelvis.paraurethral` (Skene's) | urogenital sinus |
| `pelvis.bulbourethral` | `pelvis.vestibular-glands` (Bartholin's) | urogenital sinus |

Ducts are *not* homologues: the male ducts come from the Wolffian duct, the female tubes/uterus from the Müllerian duct (each sex keeps one and loses the other). See `library/female-reproductive/tracts.md`.

## Rules
- **Never borrow an opposite-sex mesh unlabelled.** If the female (or male) body lacks a mesh, show a **hotspot** pin (`hotspot_only: true` / `female_hotspot`). Current gaps: female pituitary, female adrenal, ovarian artery, vulva, clitoris, vestibular glands; male ejaculatory duct, bulbourethral glands, scrotum.
- slorksmo's female gap-fills (borrowed male bones, Andreassen leg muscles) stay in their own off-by-default systems; never mix them into `female_layer`.
- **Dose, not presence.** Both bodies carry the same hormone receptors and make all three sex steroids. Layer panels state amounts: testosterone ~7 mg/day in men vs ~0.3 mg/day in women; serum 7.7–29.4 vs 0–1.7 nmol/L [18].
- **Ranges, not boxes.** Panels describe typical adult anatomy. Variation (intersex traits, surgery, age, pregnancy) gets a short note, not a third hard-coded body.
- Every number carries an integer cite → `sources/whole-body-overview-sources.md`.

## HPG arrows (overlay `hormones.hpg`)
`head-neck.hypothalamus` → `head-neck.pituitary` → `pelvis.testis` (male_layer) or `pelvis.ovary` (female_layer), with feedback arrows back up. Male = steady loop (thermostat); female = monthly loop with a positive-feedback LH surge (clock). Copy: `library/hormones/hpg-axis.md`.
