# Leydig-cell steroidogenesis (cell-level chemistry)

**One-liner:** A Leydig cell is a cholesterol refinery wired to one doorbell, LH. Each ring pushes more cholesterol through a single mitochondrial door.

**Where it sits:** in the gaps between the sperm-making tubules of the testis (the interstitium), close to capillaries. There are ~500 million of these cells. Anatomy: [testes.md](testes.md).

**Inside the cell, step by step**

| # | Where | Protein | What happens | Speed |
|---|---|---|---|---|
| 0 | membrane | **LHCGR** → Gs → **cAMP** → PKA | LH rings the doorbell | seconds |
| 1 | lipid droplets, LDL/HDL uptake, de novo synthesis | (HSL, SR-BI) | free up a cholesterol supply | minutes |
| 2 | outer → inner mitochondrial membrane | **StAR** (with TSPO/transduceosome partners) | **rate-limiting** cholesterol transfer | minutes (acute) |
| 3 | inner mitochondrial membrane | **CYP11A1** (P450scc) | cut the side chain → **pregnenolone** | — |
| 4 | smooth ER | **CYP17A1** + cytochrome b5 | 17α-hydroxylation, then the 17,20-lyase cut → **DHEA** (Δ5 route) | — |
| 5 | smooth ER | **HSD3B2** | DHEA → **androstenedione** | — |
| 6 | smooth ER | **HSD17B3** (testis-specific) | androstenedione → **testosterone** | — |
| 7 | leaves by diffusion | no storage granules | made on demand; ~5–7 mg/day leaves the testis | — |

**Two time scales**
- **Acute (minutes):** cAMP raises StAR, so the door opens wider.
- **Chronic (hours to days):** LH keeps the enzyme genes (CYP11A1, CYP17A1, HSD3B2, HSD17B3) switched on and maintains the Leydig cells themselves.

**Local vs systemic:** testosterone inside the testis is ~40–100× serum, which Sertoli cells need. Outside testosterone shuts off LH and collapses this local pool.

**Aging note:** older Leydig cells make less testosterone per cell, partly because the StAR/CYP11A1 front end weakens (Zirkin & Papadopoulos 2018; the evidence is mostly from rats).

**Watch-out:** Leydig cells also make **INSL3** and a little estradiol. Most male estradiol, though, is made in fat (see `../adipose-metabolism/sex-hormones-and-fat.md`).

**Sources:** Zirkin & Papadopoulos 2018 (10.1093/biolre/ioy059); Miller & Auchus 2011 (10.1210/er.2010-0013); Jarow & Zirkin 2005 (10.1196/annals.1336.023); Coviello et al. 2004 (10.1002/j.1939-4640.2004.tb03164.x); Handelsman, Endotext 2026.

**Links**
- Hormone cards: `../hormones/testicular-testosterone-production.md`, `../hormones/steroidogenesis-overview.md`
- Map: `../../body-map/regions/gonads-male-chemistry.md` (`pelvis.testis`, male_layer)
- Physics of packing: `../../body-map/cell-physics/sex-steroidogenic-packing.md`
- Receptors (LHCGR, AR): `../receptors/`
- Equal-depth twin: `../female-reproductive/ovarian-steroidogenesis.md`
