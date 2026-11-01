# Outline — Human biology & chemistry in vivo (map-first)

**Theme:** 1 — Real-life human biology and chemistry  
**Paper:** `01-human-biology-chemistry-in-vivo.md`  
**Status:** Draft v1 exists · expanding sex-chemistry depth + map/library extracts  
**Audience:** Universal · PhD-worthy depth · voice abstract / easy / fun / simple  
**Architecture:** Map-first — paper feeds `body-map/` + `library/` panels; do not reinvent anatomy viewers (see `notes/github-anatomy-landscape.md`)

---

## Thesis
Alive = holding chemical gradients on purpose. Textbook reactions are real; in vivo they run in compartments, at finite rates, with noise — and sex steroid chemistry is a first-class control layer for both male and female bodies.

## Section arc
1. Abstract  
2. Factory that never finishes (gradients ≠ equilibrium)  
3. Core chemistry in vivo (water, pH/buffers, electrolytes, redox, O₂)  
4. Energy currency (ATP / PCr / glycolysis vs OxPhos)  
5. Macromolecules at work  
6. Signaling chemistry (brief) + **Sex steroid chemistry (deep, both sexes)**  
   - Steroidogenesis overview  
   - Testicular testosterone production (Leydig; LH; key enzymes)  
   - Circulating testosterone levels (male/female ranges; free vs bound)  
   - Ovarian estradiol/progesterone chemistry & cycle as control loop  
   - Aromatase / peripheral conversion  
7. Homeostasis loops (glucose; CO₂/pH)  
8. Real life vs textbook  
9. Closing — map/library hooks; reuse open-source atlases (human-atlas, Z-Anatomy, …)  
10. Sources  

## Figures (`figures/biology-chemistry/`)
- gradient-not-equilibrium.png ✅  
- atp-energy-flow.png ✅  
- compartments.png ✅  
- buffer-loop.gif ✅  
- *(add)* steroidogenesis or Leydig production PNG if it clarifies  

## Map / library extracts (required)
- `library/hormones/` — levels, production, estradiol/progesterone, steroidogenesis  
- `library/male-reproductive/` — Leydig steroidogenesis (chemistry)  
- `library/female-reproductive/` — ovarian steroidogenesis (chemistry)  
- `body-map/regions/` — gonads male/female chemistry hover payloads  
- Existing: blood-buffers, atp-energy, redox; vessel/heart chemistry notes  

## Out of scope
Full anatomy viewers; Whole Body structure; Receptors deep-dive; Adipose build; Bone metrics; Cell crowding physics.
