# Open-source anatomy landscape (searched 2026-11-01)

Do **not** reinvent viewers or meshes. Prefer these existing projects/datasets.

## Strong build-on candidates

### [ashemag/human-atlas](https://github.com/ashemag/human-atlas)
- Interactive 3D explorer (React + Three.js), MIT app code
- BodyParts3D 4.0 adult male: 2,234 selectable meshes, 15 systems, search, exploded views
- Data: CC BY 4.0 — keep attribution
- Demo: https://human-atlas-seven.vercel.app
- **Fit:** strongest browser atlas for male mesh selection + system layers

### [slorksmo/Human-Atlas](https://github.com/slorksmo/Human-Atlas)
- Interactive 3D explorer with **male and female** reference bodies
- 3,400+ individually selectable structures (per description)
- **Fit:** sex-layer requirement; compare license/meshes before adopting

### [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy)
- Three.js interactive 3D human anatomy explorer
- **Fit:** alternate viewer stack; evaluate maturity vs human-atlas

### [Z-Anatomy/Models-of-human-anatomy](https://github.com/Z-Anatomy/Models-of-human-anatomy)
- Blender navigable atlas template; BodyParts3D-derived; CC BY-SA 4.0
- Sibling app: [LluisV/Z-Anatomy](https://github.com/LluisV/Z-Anatomy) (Unity)
- Browser port of model: [hpfrei/body-anatomy-3d-viewer](https://github.com/hpfrei/body-anatomy-3d-viewer) (GLB + click layers)
- **Fit:** mesh source + Blender/Unity paths; ShareAlike on derivatives

### [HongChao6/open-anatomy-studio](https://github.com/HongChao6/open-anatomy-studio)
- MIT studio: organs, layers, cross-sections, hotspots, bilingual
- Human Reference Atlas organ models (CC BY 4.0)
- **Fit:** lesson/hotspot pattern for map panels fed by our papers

### [biocat-ugent/Open-Anatomy-Explorer](https://github.com/biocat-ugent/Open-Anatomy-Explorer) (OPANEX)
- Apache-2.0 web atlas (Angular): upload/label 3D models, quizzes, share
- **Fit:** if we need authoring/labeling workflow for custom overlays

### [jixiangying/anatomy](https://github.com/jixiangying/anatomy)
- BodyParts3D-based interactive browser; 11 systems; bilingual labels + search
- **Fit:** another BodyParts3D UI to steal UX patterns from

### [FreedomIntelligence/BodyVista](https://github.com/FreedomIntelligence/BodyVista)
- Immersive anatomy exploration
- **Fit:** exploratory; check license before deep reuse

### [soroojshehryar/react-muscle-highlighter](https://github.com/soroojshehryar/react-muscle-highlighter)
- React 2D muscle highlighter component library
- **Fit:** simple 2D fallback / muscle layer if 3D is too heavy

## Datasets / atlases to cite
- **BodyParts3D** (DBCLS) — polygon anatomy; often CC BY; adult male reference in several viewers
- **Human Reference Atlas** — organ models used by open-anatomy-studio

## Working recommendation
1. Prototype map UI on **ashemag/human-atlas** (or **slorksmo/Human-Atlas** if female body quality is better).
2. Pull mesh/data attribution carefully (BodyParts3D / HRA / Z-Anatomy licenses).
3. Inject our `body-map/` + `library/` payloads (incl. sex hormones & reproductive systems) as panel content from white-paper streams.
4. Use **open-anatomy-studio** hotspot/lesson patterns for paper→map content binding.

## Decision (Whole Body, 2026-11-01)
Primary viewer: **slorksmo/Human-Atlas** (male BodyParts3D + female HRA, MIT, stable `FJ`/`HRAF` mesh IDs); **ashemag/human-atlas** = upstream/male-only fallback; **open-anatomy-studio** = content-contract pattern only; **Z-Anatomy** = reference only (CC BY-SA). Full table, injection steps, and attribution: `body-map/README.md`.
