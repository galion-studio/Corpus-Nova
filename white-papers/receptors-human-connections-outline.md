# Outline — Receptor connections → map overlays (map-first)

**Theme:** 3 · Receptor-level human connections  
**Pipeline:** white-paper prose → `body-map/` panel/hover copy + `library/receptors/` cards  
**Audience:** universal · **Depth:** PhD-worthy · **Voice:** abstract, easy, fun, simple  
**Atlases:** overlay onto ashemag/human-atlas / BodyParts3D + slorksmo/Human-Atlas (♂/♀) — do not reinvent viewers  
**Status:** outline v3 · 2026-11-01 (map-first + sex biology)

---

## Thesis
Human connection (social + sexual + parental) is a receptor-shaped conversation across brain and gonads. Ligands knock; subtypes, density, and sex-steroid receptors rewrite the script.

## Content blocks (feed map + library)

### A. Affiliation cast (brain + periphery)
OXTR · AVPR1A/1B · MOR · DRD2/D3 · brief 5-HT — existing draft core.

### B. Sex-steroid receptors (CRITICAL)
- **AR** (androgen receptor, NR3C4) — genomic / non-genomic; ♂♀ distribution  
- **ERα / ESR1**, **ERβ / ESR2**, **GPER1** — estrogen pathways  
- **PGR** — progesterone receptor  
Panel copy + library cards + figure `receptors-sex-steroid-cast.png`

### C. HPG axis receptors & testosterone production
- **GNRHR**, **FSHR**, **LHCGR**  
- Leydig-cell testosterone production context (LH → LHCGR → steroidogenesis)  
- Levels as map annotations (not a separate endocrinology textbook)  
Figure `receptors-hpg-axis.png`

### D. Male reproductive receptor map
Testes, epididymis, prostate, seminal vesicles, erectile tissue — receptor tags for atlas meshes; `sex: male` overlay layer.

### E. Female reproductive receptor map
Ovary/follicle, uterus, cervix, vagina, breast — OXTR + steroid + gonadotropin receptors; `sex: female` overlay layer.

### F. Sex differences in social receptors
Where literature supports OXTR/AVPR/MOR differences — careful, cited.

### G. Recreating / measuring / open edges
Same as before; add sex-layer ethics.

---

## Deliverable files
| Path | Role |
|------|------|
| `white-papers/receptors-human-connections.md` | Content source (expanded) |
| `body-map/overlays/receptors-overlays.json` | Hover JSON + atlas_targets + sex layers |
| `body-map/overlays/receptors-sex-hormones-panel.md` | Map panel prose |
| `library/receptors/*.md` | Cards (affiliation + sex-steroid + HPG) |
| `figures/receptors/*.png|gif` | Transparent assets |
| `sources/receptors-sources.md` | Citations |

## Region ID hints
Align with `body-map/regions/` (pelvis, etc.) and atlas mesh/system names; fields: `sex`, `atlas_targets[{project, hint}]`.
