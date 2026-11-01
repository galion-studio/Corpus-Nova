# Map / library payload extract — Crowded Cell (paper 01)

**Pipeline:** white-papers/cell-physics-01-crowded-cell.md → these cards → inject into open-source atlas panels (see notes/github-anatomy-landscape.md). Do not invent a new 3D viewer.

## Universal hover facts (any tissue cell)

| id | short_label | hover_one_liner | panel_blurb |
|----|-------------|-----------------|-------------|
| cp.crowding | Crowding | Inside cells, big molecules take ~20–30% of the volume — not dilute water. | Soft-matter packing (excluded volume) speeds binding/folding and slows travel for large cargos. |
| cp.subdiffusion | Odd diffusion | Crowding can make molecules rattle in cages, then hop — not a simple random walk. | Mean squared displacement can grow slower than time (subdiffusion); size matters. |
| cp.viscoelastic | Soft gel | Cytoplasm feels like jelly or honey depending on size and how fast you poke it. | Viscoelastic / poroelastic: short times push back; fluid seeps on longer times. |
| cp.kt | Heat vs motors | Heat jiggle (~4.3 pN·nm) sits on the same scale as molecular motors (few pN). | Motors work inside thermal noise, not above it. |
| cp.condensates | Droplets | Crowding helps push proteins into membrane-free droplets (condensates). | Osmotic shrink → more crowding → fast droplet assembly; links to stress and some disease physics. |

## Region bindings (BodyParts3D / atlas mesh ids TBD by map lead)

| region_hint | payload_ids | note |
|-------------|-------------|------|
| heart / cardiac muscle | cp.kt, heart-cardiomyocyte.md | Force lattice |
| brain / peripheral nerve axon | cp.subdiffusion, cp.crowding, brain-axon-transport.md | Transport vs diffusion |
| blood / erythrocyte | blood-rbc-membrane.md, cp.kt | Soft shell |
| vessel endothelium | vessel-endothelium.md, cp.kt | Shear as force |
| testis / ovary (sex layers) | see sex-biology notes below | Physics only; full repro content owned elsewhere |

## Asset refs
- figures/cell-physics/cell-physics-crowding-scale.png
- figures/cell-physics/cell-physics-diffusion-paths.png
