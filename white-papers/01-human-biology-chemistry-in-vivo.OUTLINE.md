# Outline — Human biology & chemistry in vivo (map-first)

**Theme:** 1 — Real-life human biology and chemistry  
**Paper:** `01-human-biology-chemistry-in-vivo.md`  
**Status:** Draft 2 complete (map-first + sex-steroid chemistry) · extracts written  
**Audience:** Universal · PhD-worthy depth · voice abstract / easy / fun / simple  
**Architecture:** Map-first — paper feeds `body-map/` + `library/` panels; do not reinvent anatomy viewers (see `notes/github-anatomy-landscape.md`)

---

## Thesis
Alive = holding chemical gradients on purpose. Textbook reactions are real; in vivo they run in compartments, at finite rates, with noise — and sex steroid chemistry is a first-class control layer for both male and female bodies.

## Section arc (as drafted: Draft 2, map-first + sex-steroid chemistry)
Abstract, then:
1. The factory that never finishes (gradients ≠ equilibrium). Fig 1
2. Core chemistry in vivo: 2.1 water · 2.2 pH/buffers (Fig 2 GIF) · 2.3 electrolytes · 2.4 redox (Fig 3) · 2.5 O₂/ROS
3. Energy currency: ATP / PCr / glycolysis vs OxPhos / lactate. Fig 4
4. Macromolecules at work
5. Signaling chemistry (brief)
6. Homeostasis loops (glucose; CO₂/pH)
7. **Sex-steroid chemistry, deep, equal ♂/♀ depth.** Fig 5
   - 7.1 gate: StAR + CYP11A1 (cholesterol → pregnenolone)
   - 7.2 branch points: CYP17A1 (+b5), 3β-HSD2, 17β-HSD3/AKR1C3, aromatase, 5α-reductase
   - 7.3 testicular testosterone: Leydig cells, LH, numbers, diurnal rhythm, intratesticular gradient
   - 7.4 ovarian E2/P4: two-cell model; production table; female testosterone
   - 7.5 cycle as a control loop that flips sign
   - 7.6 free vs bound (SHBG / albumin / free)
   - 7.7 aromatase and 5α-reductase in the periphery
8. Real life vs textbook
9. Why this lens matters: theme cross-links; **9.1 map-first payload table** plus a note on reusing open-source viewers (no viewer built here)
10. Sources, plus companion `sources/biology-chemistry-paper1-sources.md` (DOIs)

*Order note:* sex steroids come **after** homeostasis loops (not merged into §5 signaling), so the cycle can be told as a loop that flips sign once loops have been introduced. The content matches the locked outline; only the placement changed.

## Figures (`figures/biology-chemistry/`; scripts in `src/`)
- Fig 1 `biology-chemistry-gradient-not-equilibrium.png` ✅
- Fig 2 `biology-chemistry-buffer-loop.gif` ✅
- Fig 3 `biology-chemistry-compartments.png` ✅
- Fig 4 `biology-chemistry-atp-energy-flow.png` ✅
- Fig 5 `biology-chemistry-steroid-pathway.png` ✅ (male / female / both colour-coded; `src/make_steroid_figure.py`)

## Map / library extracts (done in Draft 2)
- `library/hormones/`: steroidogenesis-overview, testosterone-levels, testicular-testosterone-production, estradiol-progesterone (chemistry zoom cards next to the Whole Body overview cards; README is the shared index)
- `library/male-reproductive/leydig-steroidogenesis.md` · `library/female-reproductive/ovarian-steroidogenesis.md`
- `body-map/regions/gonads-male-chemistry.md` · `gonads-female-chemistry.md` (parallel YAML hover payloads; rows added to the regions index and a pelvis pointer)
- Expanded: `library/biology-chemistry/` (blood-buffers, atp-energy, redox, INDEX) · `body-map/regions/blood-vessels-chemistry.md`, `heart-metabolic-chemistry.md`
- Next: liver / muscle / kidney chemistry payloads; adrenal branch (cortisol/aldosterone)

## Out of scope
Full anatomy viewers; Whole Body structure; Receptors deep-dive; Adipose build; Bone metrics; Cell crowding physics.

---
**License:** MIT — © 2026 Corpus Nova contributors. See `/LICENSE`. Third-party atlas meshes retain their own licenses.
