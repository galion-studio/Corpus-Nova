# Region payload: blood vessels (chemistry overlay)

*Biology & chemistry hover payload. Vessel anatomy and pressures belong to Whole Body (`library/pressures/vein-pressures.md`). Source: white paper 01 §2.2–2.3, §6.*

```yaml
id: vessels.blood.chem
layer: shared
title: "Liquid that refuses to settle"
one_liner: "Blood is a buffered, ion-balanced chemical fluid, held far from equilibrium by lungs, kidneys, and pumps."
key_numbers:
  - "Arterial pH 7.35–7.45; HCO₃⁻ ≈ 24 mM vs CO₂ ≈ 1.2 mM (20:1) → pH ≈ 7.4 — Boron & Boulpaep 2017"
  - "Plasma Na⁺ ~140 mM vs ~10–15 mM inside cells; K⁺ ~4 mM vs ~140 mM inside"
  - "Free Ca²⁺ ~1.2 mM outside vs ~100 nM inside, a ~10,000× gap — Clapham 2007"
  - "Only ~4 g of glucose in all the blood (≈ a teaspoon, 4–6 mM fasting) — Wasserman 2009"
  - "Carries sex steroids mostly bound: testosterone ~1–3% free; estradiol ~2% free — Dunn 1981"
loop:
  type: "two-speed negative feedback"
  path: "acid ↑ → CO₂ ↑ → brainstem/carotid sensors → breathe more (minutes); kidneys reset HCO₃⁻ (hours to days)"
glance_animation: "figures/biology-chemistry/biology-chemistry-buffer-loop.gif"
library: [library/biology-chemistry/blood-buffers.md, library/hormones/testosterone-levels.md]
cross_links:
  pressures: library/pressures/vein-pressures.md     # Whole Body
  cell_physics: body-map/cell-physics/blood-rbc-membrane.md
sources: sources/biology-chemistry-paper1-sources.md
do_not: "No vessel anatomy, no pressure numbers (Whole Body), no receptor maps (Receptors)."
```
