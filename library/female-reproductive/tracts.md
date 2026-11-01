# Female tracts & external genitalia — card

**One-liner:** a two-way corridor — tubes that catch the egg and host fertilization, a vagina that is both birth canal and entry route, and a vulva whose structures mirror the male ones they share an embryonic origin with.

Map: `pelvis.uterine-tube` · `pelvis.vagina` · `pelvis.vulva` · `pelvis.clitoris` · `thorax.breast` · `female_layer`

## Uterine (fallopian) tubes, ~10–12 cm each [4]
| Segment | Job |
|---|---|
| **Fimbriae / infundibulum** | finger-like fringe sweeps the released egg in (the tube is open to the peritoneal cavity — a real gap in the "wall") |
| **Ampulla** | widest part; usual site of **fertilization** |
| **Isthmus** | narrow; sperm storage and transport |
| **Intramural part** | passes through the uterine wall |

## Vagina
Fibromuscular canal from cervix to vestibule; stretchy folded wall (*rugae*); acidic environment maintained largely by *Lactobacillus* bacteria [4, 7].

## Vulva (external)
Mons pubis, labia majora, labia minora, vestibule (urethral + vaginal openings), **greater vestibular (Bartholin) glands**, paraurethral (Skene's) glands [4].

## Clitoris
Much larger than its visible glans: glans + body + two **crura** along the pubic arch + two **vestibular bulbs**; erectile tissue with the same NO-driven mechanism as the penis [4, 7].

## Homology — one blueprint, two builds [4]
| Female | Male | Shared origin |
|---|---|---|
| Ovary | Testis | gonadal ridge |
| Labia majora | Scrotum | labioscrotal swellings |
| Clitoris glans/body/crura | Glans / corpora cavernosa | genital tubercle |
| Vestibular bulbs | Corpus spongiosum (bulb) | — |
| Greater vestibular (Bartholin) glands | Bulbourethral (Cowper's) glands | urogenital sinus |
| Paraurethral (Skene's) glands | Prostate | urogenital sinus |
| Round + ovarian ligaments | Gubernaculum testis | gubernaculum |

Testosterone → DHT (SRD5A2) pushes the shared tubercle and swellings toward the male build; without it they form the female build [19].

## Breast (pointer)
Mammary glands are skin-derived glands in the thorax; growth driven by estradiol + progesterone, milk by prolactin, let-down by oxytocin. Region `thorax.breast` (female_layer; male_layer shows rudimentary tissue).

## Hover payloads
```yaml
- id: pelvis.uterine-tube
  layer: female_layer
  atlas_mesh: {female_body: [HRAF0408-0415 (ampulla/isthmus/fimbriae/infundibulum L+R), HRAF0434 Abdominal ostium, HRAF0428/0429 Mesosalpinx]}
- id: pelvis.vagina
  layer: female_layer
  atlas_mesh: {female_body: [HRAF0406 Vagina]}
- id: pelvis.vulva
  layer: female_layer
  atlas_mesh: {female_body: []}   # not in HRA v1.10 → hotspot marker
- id: pelvis.clitoris
  layer: female_layer
  atlas_mesh: {female_body: []}   # not in HRA v1.10 → hotspot marker
- id: thorax.breast
  layer: female_layer
  atlas_mesh: {female_body: [HRAF0008 Mammary lobes L, HRAF0018 Mammary lobes R]}
```
