# Accessory glands & penis — card

**One-liner:** sperm are only a few percent of semen; three glands supply the rest — fuel, fluid, and lubrication — and erectile tissue does the delivery.

Map: `pelvis.seminal-vesicle` · `pelvis.prostate` · `pelvis.bulbourethral` · `pelvis.penis` · `male_layer`

## Glands
| Gland | Where | Contribution | Hormone dependence |
|---|---|---|---|
| **Seminal vesicles** (paired) | behind bladder, beside ampulla of vas | largest share of semen volume (often quoted ~60–70%): fructose (sperm fuel), prostaglandins, semenogelin (clotting protein) [7] | androgen-dependent |
| **Prostate** (single, walnut-sized) | below bladder, wraps the prostatic urethra | ~20–30% of volume: citrate, zinc, PSA (liquefies the semen clot) [7] | growth driven by **DHT** made locally by 5α-reductase type 2 (SRD5A2) [19]; zones: peripheral (most cancers), transition (benign enlargement), central [4] |
| **Bulbourethral (Cowper's) glands** (paired, pea-sized) | in the deep perineal pouch | clear mucus that lubricates and neutralizes the urethra before ejaculation [4] | — |

## Penis
- **Erectile bodies:** two **corpora cavernosa** (dorsal) + one **corpus spongiosum** (ventral, carries the urethra, expands into the **glans**) [4].
- **Erection:** parasympathetic pelvic splanchnic nerves (S2–S4) → nitric oxide → cGMP → smooth-muscle relaxation → blood fills the cavernous spaces and compresses outflow veins [7].
- **Emission/ejaculation:** sympathetic outflow (T12–L2) contracts vas, vesicles, and prostate; then rhythmic contraction of bulbospongiosus muscle [7].
- Mnemonic: **"Point and Shoot"** — parasympathetic points, sympathetic shoots.

## Hover payloads
```yaml
- id: pelvis.seminal-vesicle
  layer: male_layer
  atlas_mesh: {male_body: [FJ3137 Left seminal vesicle, FJ3143 Right seminal vesicle]}
- id: pelvis.prostate
  layer: male_layer
  receptor_pointers: [AR, SRD5A2]
  atlas_mesh: {male_body: [FJ3139 Prostate]}
- id: pelvis.bulbourethral
  layer: male_layer
  atlas_mesh: {male_body: []}   # hotspot marker
- id: pelvis.penis
  layer: male_layer
  atlas_mesh: {male_body: [FJ3132 Corpus cavernosum of penis, FJ3133 Corpus spongiosum of penis, FJ3134 Glans penis]}
```
