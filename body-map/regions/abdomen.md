# Region: abdomen

**Hover reveals**

| Field | Seed content |
|-------|----------------|
| organs | Liver, stomach, intestines, pancreas, spleen, kidneys |
| vessels | Aorta branches, portal vein, IVC tributaries |
| receptor_pointers | GI & metabolic receptors (→ Receptors) |
| heart_pump | false |
| vein_pressures_ref | library/pressures/vein-pressures.md |

**Status:** structure seed — fill exact IDs, hit-areas, and cited pressure numbers before interactive Page build.

## Panel extract (Whole Body v3) → `../panels/whole-body-panels.json#abdomen`
- **Title:** Intake, processing, filtering (kidneys filter ~180 L plasma/day).
- **Child:** `abdomen.adrenal` (FJ3129/FJ3130 · female hotspot) — cortisol, aldosterone, DHEA/DHEA-S; ~⅓ of women's testosterone traces back to adrenal precursors.
- **Vessels note:** gonadal arteries leave the aorta here; left gonadal vein drains to the left renal vein (both sexes).
- **Adipose overlay:** `depot.subcutaneous.abdominal`, `depot.visceral.omental_mesenteric`, `depot.perirenal` (owner: Adipose, `../overlays/adipose-depots.json`).
- **Bone overlay:** `bone.vertebra.body`.
