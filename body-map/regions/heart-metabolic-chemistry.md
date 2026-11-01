# Region payload: heart (metabolic chemistry overlay)

*Biology & chemistry hover payload. Pump mechanics and anatomy belong to Whole Body (`heart-pump.md`). Source: white paper 01 §3.*

```yaml
id: thorax.heart.chem
layer: shared
title: "Engine with no fuel tank"
one_liner: "The heart keeps only seconds of ATP on hand and rebuilds it nonstop from fat, glucose, and lactate, using oxygen."
key_numbers:
  - "Cycles ~6 kg ATP/day, 20–30× its own weight — Neubauer 2007"
  - "Normal adult heart: ~60–90% of ATP from fatty acids, ~10–40% from glucose (plus lactate) — Neubauer 2007"
  - "Creatine phosphate + creatine kinase buffer ATP between beats — Wallimann 1992"
  - "Mitochondria: ~30–32 ATP per glucose vs 2 from glycolysis alone — Hinkle 2005"
  - "Lactate from working muscle is burned as fuel by the heart — Brooks 2018"
pathway_steps:
  fuel_in: "fatty acids, glucose, lactate, ketones"
  engine: "TCA cycle → NADH → electron chain (inner membrane ~150–180 mV) → ATP synthase"
  backup: "PCr ⇄ ATP via creatine kinase"
  spend: "myosin motors, Ca²⁺ pumps (SERCA), Na⁺/K⁺-ATPase"
glance_animation: "figures/biology-chemistry/biology-chemistry-atp-energy-flow.png (static)"
library: [library/biology-chemistry/atp-energy.md, library/biology-chemistry/redox.md]
cross_links:
  pump: body-map/regions/heart-pump.md              # Whole Body
  cell_physics: body-map/cell-physics/heart-cardiomyocyte.md
sources: sources/biology-chemistry-paper1-sources.md
do_not: "No cardiac anatomy or pressure/flow mechanics (Whole Body), no clinical advice."
```
