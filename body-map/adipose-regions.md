# Body map — adipose / fat-distribution notes

Payloads for the interactive body map (hover / panels). **Map-first.** Calm and factual.  
Do **not** reinvent 3D viewers — inject into existing atlases (see `notes/github-anatomy-landscape.md`).  
Machine-readable twin: `body-map/overlays/adipose-depots.json`.

## Whole-body pattern
- Most stored fat sits under the skin (**subcutaneous**).
- A smaller share wraps organs in the belly (**visceral**).
- **Brown / beige** heat-making pockets: mainly upper chest / neck in adults (cold-activated).

## Sex layers (required)
| Pattern | Who (typical) | Where surplus prefers | Hormone sketch |
|---------|---------------|------------------------|----------------|
| **Gynoid** | Premenopausal women | Gluteofemoral (hips, buttocks, thighs) | Estrogen favors lower-body subcutaneous storage |
| **Android** | Men; many postmenopausal women | Abdominal subcutaneous + higher visceral share | Androgen milieu + lower estrogen → more central fat |

Toggle or dual-layer on the map. Equal depth for male and female systems.

## Region notes

| Map region | Shared hover | Male layer | Female layer |
|------------|--------------|------------|--------------|
| Abdomen (front) | Under-skin + visceral pads | Often larger visceral share | Premenopause: relatively less visceral; rises after menopause |
| Flanks | Subcutaneous belt | Expands with android pattern | Present; gynoid bias is still hips/thighs |
| Hips & buttocks | Gluteofemoral archive | Smaller typical share | Estrogen-favored long-term store |
| Thighs | Limb subcutaneous | Present | Major gynoid volume |
| Upper chest / neck | Brown/beige heat pockets | Cold-activated PET signal | Same map job; annotate sex diffs later if needed |
| Omentum / mesentery | Visceral / portal drainage | Often larger | Smaller premenopause |
| Perirenal | Visceral-adjacent | Map with deep belly | Same |
| Epicardial | Heart-surface pad | Specialized; not belly VAT | Same |
| Breast (where present) | Gland + adipose mix | — | Not visceral belly fat |

## Hover field suggestions
- `fat_type`: subcutaneous | visceral | brown | specialized
- `sex_layer`: male | female | shared
- `storage_role`: archive | heat | cushion
- `library_card`: path under `library/adipose-metabolism/`

## Ownership
Theme 5 (Adipose). Coordinate with Whole Body for region meshes; hormones library for androgen/estrogen pathways; do not overwrite vessel/pressure fields.
