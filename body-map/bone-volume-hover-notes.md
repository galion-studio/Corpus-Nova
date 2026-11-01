# Body map — bone sector & volume hover notes (Theme 4)

Hover copy for skeletal regions. Keep short, universal voice. Numbers only when source-backed in the white paper / library.

## Long bones (femur, tibia, humerus, radius)

### Proximal sector
- **Hover title:** Proximal bone volume
- **Blurb:** Near the joint. Often richer in trabecular (spongy) bone volume. Takes a lot of the “shock absorber” job.
- **Number:** Femoral head ≈ 50:50 cortical:trabecular [Clarke 2008]. Women’s femoral-neck top-back wall thins ≈ 6.4%/decade [Mayhew 2005].
- **Show:** sector = proximal · tip → cortical shell vs trabecular core

### Midshaft sector
- **Hover title:** Midshaft bone volume
- **Blurb:** The tube in the middle. Mostly cortical (compact) volume — a strong hollow beam.
- **Number:** Radial shaft ≈ 95:5 cortical:trabecular [Clarke 2008]. With age the tube widens (bone area +15–16%) as the wall drifts outward [Riggs 2004].
- **Show:** sector = midshaft · high Ct.V / low Tb.V typical

### Distal sector
- **Hover title:** Distal bone volume
- **Blurb:** Toward the far joint. Trabecular volume rises again; cortical walls often thin.
- **Number:** Distal radius (women 50–80): 68% of bone lost was cortical, 32% trabecular; 84% of it after 65 [Zebaze 2010].
- **Show:** sector = distal

## Compartments (any shaft cross-section)
- **Cortical volume (Ct.V):** the dense outer ring.
- **Trabecular volume (Tb.V):** the inner lattice / honeycomb.
- **Total volume (TV):** the whole ROI; BV/TV is “how much of that space is bone.”
- **Number:** skeleton ≈ 80% cortical / 20% trabecular; vertebra ≈ 25:75 with a ≈ 0.38 mm shell [Clarke 2008; Eswaran 2006].

## Laterality (left vs right)
- **Hover title:** Left–right volume
- **Blurb:** Sides rarely match perfectly. Habitual loading and handedness nudge volume and cortical geometry — especially in arm bones.
- **Show:** compare L/R CSA or Ct.V; don’t assume pathology from mild asymmetry alone.
- **Numbers (arms):** humeral shaft breadth median +2.98% right (76% of people right-biased); radius +2.21%; >10% not rare [Auerbach & Ruff 2006]. Tennis playing arm: cortical area +12–32%, density ≈ same [Haapasalo 2000].
- **Numbers (legs):** femur −0.49%, tibia −0.78%; leg length median ≤ 0.71% (≈ 2.5 mm) [Auerbach & Ruff 2006].
- **Numbers (hips):** L/R r = 0.92–0.95, yet >half differ beyond scanner noise [Mounach 2012].

## Envelopes (growth / aging cue)
- **Periosteal:** outer surface — can add volume outward.
- **Endosteal:** inner surface of the cortex — can expand the marrow cavity and thin the wall.
- **Number:** inner-wall remodelling = 47% of distal-radius loss in women [Zebaze 2010]. GIF: `figures/bone-volume/bone-volume-envelopes.gif`.

## Sex layer (female / male toggle)
Bone-metric differences only (reproductive anatomy lives in other themes).
- **Female tip:** Peak total-body bone mineral ≈ age 18. With age, the sponge loses struts (Tb.N −13%, gaps +24%) [Baxter-Jones 2011; Khosla 2006].
- **Male tip:** Peak ≈ age 20. Bone cross-sections 35–42% larger. With age, struts mostly thin (−24%) rather than vanish [Baxter-Jones 2011; Riggs 2004; Khosla 2006].
- **Both:** ≈ 39% of adult total-body bone mineral is laid down in the 4 years around the growth spurt [Baxter-Jones 2011].
- **Arms:** humeral asymmetry +3.35% (men) vs +2.29% (women) [Auerbach & Ruff 2006].
- **Atlas:** use slorksmo/Human-Atlas for paired male + female bodies.

## Region IDs (for map wiring)
| region_id | label | notes_key |
|-----------|-------|-----------|
| bone.femur.prox | Femur · proximal | proximal |
| bone.femur.mid | Femur · midshaft | midshaft |
| bone.femur.dist | Femur · distal | distal |
| bone.tibia.prox | Tibia · proximal | proximal |
| bone.tibia.mid | Tibia · midshaft | midshaft |
| bone.tibia.dist | Tibia · distal | distal |
| bone.humerus.prox | Humerus · proximal | proximal |
| bone.humerus.mid | Humerus · midshaft | midshaft |
| bone.humerus.dist | Humerus · distal | distal |
| bone.radius.prox | Radius · proximal | proximal |
| bone.radius.mid | Radius · midshaft | midshaft |
| bone.radius.dist | Radius · distal | distal |
| bone.laterality.arms | Arms · L/R | laterality |
| bone.laterality.legs | Legs · L/R | laterality |
| bone.laterality.hips | Hips · L/R DXA | laterality |
| bone.vertebra.body | Vertebral body | compartments |
| bone.femur.neck | Femoral neck | proximal |
| bone.envelopes | Periosteal vs endosteal | envelopes |
| bone.compartment.xsec | Shaft cross-section | compartments |

## Mesh binding (reuse, don’t invent)
Bind to existing BodyParts3D-style bone meshes (e.g. “right femur” / “left femur”, “right humerus” / “left humerus”) via ashemag/human-atlas or slorksmo/Human-Atlas; sectors = clip/shader bands along the long axis. Verify exact mesh names against the atlas manifest. Payload: `body-map/overlays/bone-volume-overlays.json`.

Source of truth: `white-papers/bone-volume-sectors-laterality.md` + `library/bone-metrics/` · citations in `sources/bone-volume-sources.md`.

## Sex layer (bone metrics only)
- Use male / female (or dual) atlas views; bind to existing meshes (BodyParts3D / Z-Anatomy / human-atlas) — do not invent bones.
- Hover may add one line on average sex differences in size, CSA, or peak-mass timing; details → `library/bone-metrics/sex-differences.md`.
- Do not paste reproductive-system content into bone hovers.

## Atlas reuse
- Prefer: ashemag/human-atlas, slorksmo/Human-Atlas (M/F), Z-Anatomy / BodyParts3D-derived viewers.
- Overlay JSON: `body-map/overlays/bone-volume-overlays.json`
