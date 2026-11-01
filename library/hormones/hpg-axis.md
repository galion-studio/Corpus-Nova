# HPG axis — hypothalamus → pituitary → gonads

**One-liner:** a three-floor chain of command where the top floor whispers in pulses, the middle floor shouts into the blood, and the bottom floor talks back.

Map wiring: `head-neck.hypothalamus` → `head-neck.pituitary` → `pelvis.testis` (male_layer) / `pelvis.ovary` (female_layer). Draw as an animated arrow layer (`layer: hormones.hpg`).

## Floors
| Floor | Structure | Signal | Detail |
|---|---|---|---|
| 0 (gate) | **Kisspeptin** neurons (arcuate / preoptic hypothalamus) | kisspeptin → KISS1R (GPR54) | Loss-of-function GPR54 mutations block puberty — kisspeptin is the ignition key [28] |
| 1 | Hypothalamus — GnRH neurons | **GnRH**, released in **pulses** into the portal blood of the pituitary stalk | Pulse *frequency* matters: faster favours LH, slower favours FSH; continuous GnRH *shuts the axis down* (used clinically) [7] |
| 2 | Anterior pituitary — gonadotrophs | **LH** and **FSH** into general circulation | same cells, two hormones |
| 3 | Gonads | sex steroids + inhibins | see below |

## Male loop (♂)
- **LH → Leydig cells → testosterone** (3–10 mg/day) [18].
- **FSH + high local testosterone → Sertoli cells → spermatogenesis** (~64 days per wave, possibly ~6 days off — Amann argues it needs re-measuring) [29, 30].
- **Feedback:** testosterone (and its aromatized product estradiol) brakes GnRH/LH; Sertoli-cell **inhibin B** brakes FSH [7, 19].
- **Result:** a fairly steady output with a daily rhythm (morning high) [22].

## Female loop (♀)
- **FSH → granulosa cells → follicle growth + aromatase → estradiol**; **LH → theca cells → androgen substrate** [7].
- **Feedback flips sign:** most of the cycle estradiol/progesterone are *negative* feedback; but sustained high estradiol from a dominant follicle switches to **positive feedback** → **LH surge** → ovulation [7].
- After ovulation, LH supports the **corpus luteum** → progesterone + estradiol → negative feedback until it regresses.
- **Result:** a ~monthly oscillator (mean ~29 days in a 600k-cycle dataset) [24].

## Why it matters on the map
Same three floors, same hormones, **opposite output styles**: ♂ = thermostat (steady), ♀ = clock (cyclic). The dual-layer view keeps floors 0–2 in `shared` and splits floor 3 into `male_layer` / `female_layer`.

Receptor details (KISS1R, GnRHR, LHCGR, FSHR, AR, ESR1/2, PGR) → Receptors theme.
