# Outline — Receptor connections → map overlays (map-first)

**Theme:** 3 · Receptor-level human connections  
**Pipeline:** white-paper prose → `body-map/` panel/hover copy + `library/receptors/` cards  
**Audience:** universal · **Depth:** PhD-worthy · **Voice:** abstract, easy, fun, simple  
**Atlases:** overlay onto ashemag/human-atlas / BodyParts3D + slorksmo/Human-Atlas (♂/♀) — do not reinvent viewers  
**Status:** outline v4 · 2026-11-01 (map-first + sex biology; v3 blocks A–G kept, section map + region bindings added)

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

---

## v4 additions — paper section map (blocks → sections)

The long read is a **map-content source**: every section ends in map ids so editors can trace a hover back to a paragraph.

| § | Section | Block | Layer (`layers[].id`) | Figure |
|---|---|---|---|---|
| 1 | Opening — the conversation at the membrane | A | receptors.connection | `receptors-membrane-knock.png` |
| 2 | Core cast — OXTR, AVPR1A, MOR, DRD2, 5-HT | A | receptors.connection | `receptors-affiliation-cast.png` |
| 3 | Where they sit — body + brain map | A | receptors.connection | `receptors-social-circuits.png` |
| 4 | What "exact" means | A | — | — |
| 5 | Recreating connection at receptor resolution | G | — | — |
| 6 | Worked examples (pair bond, touch, social pain) | A | receptors.connection | — |
| 7 | Second cast — AR, ERα, ERβ, GPER1, PR | B | receptors.sex-steroid | `receptors-sex-steroid-cast.png` |
| 8 | Drumbeat — KISS1R, GNRHR, LHCGR, FSHR; Leydig testosterone | C | receptors.hpg-axis | `receptors-hpg-axis.png` |
| 9 | Male receptor map | D | sex-steroid + hpg-axis (`sex: male`) | — |
| 10 | Female receptor map | E | sex-steroid + hpg-axis (`sex: female`) | — |
| 11 | Sex differences in connection receptors | F | receptors.connection | — |
| 12 | Open edges (incl. atlas resolution, mouse→human, intersex/"typical", sex-layer ethics) | G | — | — |
| 13 | Sources (52, alphabetical) | — | — | — |

Motion (optional): `receptors-oxtr-path.gif`.

## v4 additions — region id ↔ section ↔ atlas

`sex`: ♂ male · ♀ female · ◎ both. ✱ = hotspot (sub-organ; pinned on parent mesh). Atlas hint: **A** = ashemag/human-atlas · **S♂** = slorksmo male (BodyParts3D 4.0) · **S♀** = slorksmo female (HRA female v1.10).

| Region id | sex | § | Key receptors | Atlas target hint |
|---|---|---|---|---|
| `brain.pvn` ✱ | ◎ | 3, 6 | OXTR, AVPR1A, AVPR1B | A nervous › brain; S♀ brain › hypothalamus |
| `brain.vta` ✱ | ◎ | 3, 6 | OXTR, MOR | A nervous; S♀ near substantia nigra |
| `brain.nacc` ✱ | ◎ | 3, 6, 11 | DRD2, DRD3, MOR, OXTR | A nervous; S♀ near putamen |
| `brain.ventral-pallidum` ✱ | ◎ | 3, 6, 11 | AVPR1A, MOR | A nervous; S♀ near putamen |
| `brain.amygdala` | ◎ | 3, 6, 11 | OXTR, AVPR1A, 5HT1A | S♀ amygdaloid complex |
| `brain.pfc` ✱ | ◎ | 3 | DRD2, 5HT2A, OXTR | S♀ brain hemisphere |
| `brain.dacc-insula` ✱ | ◎ | 6.3 | MOR | S♀ brain hemisphere |
| `brain.lateral-septum` ✱ | ◎ | 3, 11 | AVPR1A, OXTR | S♀ near fornix |
| `brain.mpoa` ✱ | ◎ | 11 | ESR1, AR, OXTR | S♀ hypothalamus |
| `brain.hypothalamus.kiss-gnrh` ✱ | ◎ | 8.1 | KISS1R, ESR1, AR | S♀ hypothalamus; A/S♂ brain |
| `pituitary.anterior` | ◎ | 8.1 | GNRHR, AVPR1B, ESR1 | A/S♂ endocrine › pituitary gland (confirm) |
| `heart` | ◎ | 3 | OXTR | A/S♀ cardiac › heart |
| `testis.leydig` ✱ | ♂ | 8.2, 9 | LHCGR, AR | A/S♂ reproductive › testis |
| `testis.sertoli` ✱ | ♂ | 8.3, 9 | FSHR, AR | A/S♂ testis |
| `epididymis` | ♂ | 7.2, 9 | ESR1, AR | A/S♂ epididymis (confirm) |
| `prostate` | ♂ | 9 | AR, ESR2, ESR1 | A/S♂ prostate |
| `seminal-vesicle` | ♂ | 9 | AR | A/S♂ seminal vesicle (confirm) |
| `penis.corpus-cavernosum` | ♂ | 9 | GUCY1 (sGC), ADRA1, AR | A/S♂ penis (confirm) |
| `ovary.follicle.theca` ✱ | ♀ | 8.4, 10 | LHCGR, AR | S♀ ovary |
| `ovary.follicle.granulosa` ✱ | ♀ | 8.4, 10 | FSHR, LHCGR, ESR2, PGR | S♀ ovary |
| `ovary.corpus-luteum` ✱ | ♀ | 8.4, 10 | LHCGR | S♀ ovary |
| `fallopian-tube` | ♀ | 10 | ESR1, PGR | S♀ fallopian tube |
| `uterus` | ♀ | 3, 10 | OXTR | S♀ uterus |
| `uterus.endometrium` ✱ | ♀ | 7.4, 10 | ESR1, PGR, GPER1 | S♀ uterus |
| `uterus.myometrium` ✱ | ♀ | 10 | OXTR, PGR, ESR1 | S♀ uterus |
| `cervix` | ♀ | 10 | ESR1, PGR | S♀ cervix |
| `vagina` | ♀ | 10 | ESR1 | S♀ vagina |
| `breast` | ♀ | 7.4, 10 | ESR1, PGR, OXTR | S♀ mammary gland / lobes / lactiferous ducts / nipple |

Source of truth for fields is `body-map/overlays/receptors-overlays.json`. If this table and the JSON disagree, the JSON wins; fix the table.

## v4 additions — library cards

Connection: `oxtr`, `avpr1a`, `mor`, `drd2`. Sex-steroid: `ar`, `esr1`, `esr2`, `gper1`, `pgr`. HPG: `gnrhr`, `lhcgr`, `fshr`, `testosterone-production`. Planned: `kiss1r`, `avpr1b`, `htr1a-htr2a`, `connection-overview`. Hormone cross-links: `library/hormones/receptor-links.md` (link-only; no hormone prose rewritten).

## v4 guardrails
- Receptor-exact only: PDE5 and aromatase are enzymes, not receptors; label as such.
- Mouse-only findings say "in mice".
- "Typical", not "normal", for sex layers.
- No 3D viewer work; overlays + copy only.

---
**License:** MIT — © 2026 Corpus Nova contributors. See `/LICENSE`. Third-party atlas meshes retain their own licenses.
