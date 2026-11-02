![Corpus Nova](../figures/branding/cn-paper-header.png)

# Interactive plan: Soy, Estrogen and Exogenous Sex Steroids (map-first)

**Status:** plan only, 2026-11-02 (Europe/Zagreb). Nothing has been built or rendered yet. **License:** MIT
**Content source:** `white-papers/soy-estrogen-male-exogenous.md` (§12 "How to read this on the map")
**Numbers:** every hover number comes from `notes/soy-estrogen-male-research.md` / `sources/soy-estrogen-male.md`. A hover may not show any number that is not in the paper.

---

## 0. Ground rules

1. **Map-first.** The deliverable is overlay payloads on the existing body map. It is **not** a new viewer, page app, or "fake web app" mock.
2. **Reuse Human-Atlas under Atlas Lock.**
   - Primary: `slorksmo/Human-Atlas` pinned at commit `5bb5713aab18d7fe9380c3339eb09f173491ea06`, with HRA united-female v1.10 for ♀ and BodyParts3D for ♂.
   - Male fallback: `ashemag/human-atlas`.
   - Mesh IDs (`FJ####`, `HRAF####`) are stable only inside that pin (`body-map/README.md` → Lock pin).
3. **Assets:**
   - transparent **PNG** for all stills
   - **GIF** only for motion
   - no video, WebGL scenes, Lottie or SVG animation
   - STYLE.md palette only: ink #0B0F14 · paper #F7F5F2 · mute #6B7280 · line #E5E2DC · signal #2F6F6A · signal-soft #DCEEEB · alert #8B3A3A (rare)
   - no gradients, shadows or 3D bevels
4. **Evidence badges on every card:**
   - `HUMAN` / `ANIMAL`
   - molecule class: `phytoestrogen` / `pharma-E2` / `cosmetic` / `androgen`
   - strength: `strong` / `mixed` / `weak` / `absent`
5. **No clinical advice** in any hover or tooltip.
6. **VR and the gut-microbiome (equol) layer:** optional and deferred (§6).

---

## 1. Hotspots

Mesh IDs were looked up on 2026-11-02 in the pinned `public/models/atlas.json` (♂) and `public/models/atlas-female.json` (♀) at commit `5bb5713`.

**ID check (Whole Body, 2026-11-02):** hotspot ids below are now the canonical body-map region ids (`<region>.<structure>`, per `body-map/regions/index.md`, `overlays/sex-layers.json`, `panels/whole-body-panels.json`). Receptor-overlay ids (`testis.leydig`, `pituitary.anterior`, `brain.hypothalamus.kiss-gnrh`, `breast`) are cross-links, not hotspot ids. Every `FJ`/`HRAF`/`BM` id here was re-resolved against both pinned manifests on 2026-11-02; ids not in the 80-id set of `notes/atlas-packaging-id-recheck-2026-11-01.md` are marked *pin-verified, not yet in map*. Ids marked **not yet wired** have no body-map entry yet and stay hotspot stubs until Whole Body adds them. Change log: §7.

### 1a. Male body (primary)

| Hotspot id | What the card says (from the paper) | Atlas target | Pin? | Paper § |
|---|---|---|---|---|
| `thorax.breast` (male_layer) | Gynecomastia = estrogen/androgen balance. PATCH E2 86%; soy only extreme-intake cases; pubertal baseline 3.93% (Bulgaria). Lactation sub-card: witch's milk 4.6%; induced lactation n = 1. | No male breast mesh in the pin (`thorax.breast` ♂ `atlas.male_body` = [] in `sex-layers.json`). Pin anchor only on `FJ2810` Skin (FMA7163), anterior thorax. **Not yet wired:** `thorax.breast` is ♀-only in `sex-layers.json`, and receptors overlay `breast` is `sex: female`; a ♂ hotspot entry is needed. | **hotspot_only: true** · mesh ♂ false | §5, §6 |
| `pelvis.testis` (male_layer; receptor cross-link `testis.leydig`) | Soy: no T change (41 studies). Semen mixed. PATCH: castrate T in 93% at 3 months. | `FJ3138` Left testis / `FJ3142` Right testis (matches `sex-layers.json`) | mesh ♂ | §4 |
| `head-neck.hypothalamus` + `head-neck.pituitary` (shared; arrows = overlay `hormones.hpg`; receptor cross-links `brain.hypothalamus.kiss-gnrh`, `pituitary.anterior`) | The thermostat: strong estrogen → LH ↓ → T ↓. Dietary soy doesn't move it. | ♂ `FJ1760` / `FJ1808` Hypothalamus; `FJ1796` Pituitary gland (matches `sex-layers.json`) | mesh ♂ | §4.1 |
| `abdomen.liver` (shared) | First-pass gate: oral E2 is broken down here; skin routes bypass it. Isoflavones are conjugated here. | Pin-verified: concept `FMA7197` liver groups 60 ♂ parts (`FJ2816` Caudate lobe plus hepatovenous segments `FJ2409`, `FJ2818`–`FJ2824`, and hepatic vessels/ducts), so `FJ2816` is not the only liver mesh. **Not yet wired:** `abdomen.liver` is a child in `whole-body-panels.json`, but it has no mesh binding there. | hotspot until wired (mesh ♂ pending; bind by conceptId FMA7197) | §2 |

### 1b. Female body (mirror, secondary)

| Hotspot id | Card | Atlas target | Pin? | Paper § |
|---|---|---|---|---|
| `thorax.breast` (female_layer) | T → glandular reduction + fibrosis in 93%. Volume: UNSOURCED. | `HRAF0008` / `HRAF0018` Mammary lobes L/R (matches `sex-layers.json`). Optional: `HRAF0006`/`HRAF0014` nipples (pin-verified, not yet in map) | mesh ♀ | §10.2 |
| `head-neck.skin-hair` (female_layer; **proposed, not yet wired**; was `skin.hair.face-body`) | Terminal hair ↑; below male diameter at 12 months; scalp loss later. | Anchor only on `HRAF0003` Skin (pin-verified), face, with a second pin on the abdomen. No female hair mesh. The male `FJ2813` Hair of head and `FJ2815` Pubic hair are not borrowed. | **hotspot_only** · mesh ♀ false | §10.3 |
| `head-neck.mandible` (female_layer; **proposed, not yet wired**; was `head.mandible`) | Lower-face soft-tissue volume ↑, fastest at 0–3 months. Bone: UNSOURCED. | Anchor only on `HRAF0003` Skin, lower face. `BM0012` (conceptId `BORROWED:FJ3289`, system `borrowed`) is a borrowed male bone. It sits in an off-by-default gap-fill system and must not be bound into `female_layer` (`sex-layers.md` rules). | **hotspot_only** · mesh ♀ false | §10.4 |
| `head-neck.larynx` (female_layer; **proposed, not yet wired**; was `neck.larynx`) | Mean F0 125 Hz at 12 months; 24% voice symptoms. Adam's apple: UNSOURCED. | `HRAF0770` Thyroid cartilage, `HRAF0769` Cricoid cartilage (pin-verified, system `respiratory`; not yet in map) | mesh ♀ (after wiring) | §10.5 |
| `pelvis.uterus` | Endometrium mostly atrophic (45–62%); volume not clearly reduced; myometrial hypertrophy in some. Mixed. | `HRAF0435`–`HRAF0440` (body, fundus, cornua, lower segment, walls). These are a subset of the map's 18-id `pelvis.uterus` binding; the card can use the full map set. | mesh ♀ | §10.6 |
| `pelvis.ovary` | Usually enlarged; cortex and stroma hyperplasia; PCO-like in one series, not in the Japanese one. Mixed. | `HRAF0432` / `HRAF0433` Ovary L/R. These are a subset of the map's 8-id `pelvis.ovary` binding. | mesh ♀ | §10.6 |
| `pelvis.clitoris` *(optional, minor)* | Enlarges; size UNSOURCED. | No clitoris mesh in the HRA v1.10 pin (already `hotspot_only` in `sex-layers.json`). Anchor near `HRAF0406` Vagina. | hotspot_only · mesh ♀ false | §10.6 |

**Male ↔ female pairing for the sex toggle** (existing `body-map/overlays/sex-layers.json`):
- `thorax.breast` ♂ (hotspot) ↔ `thorax.breast` ♀ (mesh). This is the same structure on both bodies, not a `homolog` pair.
- `head-neck.hypothalamus` / `head-neck.pituitary` ↔ same ids (shared; ♀ hypothalamus `HRAF0338` / `HRAF0339`; the ♀ pituitary has no mesh, per the atlas re-check note, so it uses `female_hotspot`)
- `pelvis.testis` ↔ `pelvis.ovary` (existing `homolog` pair)
- `abdomen.liver` ↔ `abdomen.liver` (shared; ♀ liver surface meshes such as `HRAF0474` Capsule of the liver are in the pin but not yet in the map)

---

## 2. Overlay JSON sketch

Target file (not yet written): `body-map/overlays/soy-estrogen-male.json`, plus `soy-estrogen-female-mirror.json`. The schema follows `receptors-overlays.json` v2.

```json
{
  "version": 2,
  "theme": "sex-biology.exogenous-sex-steroids",
  "description": "Hover payloads: dietary phytoestrogens vs pharmaceutical/cosmetic estrogens on the male body; exogenous androgens on the female mirror. Content source: white-papers/soy-estrogen-male-exogenous.md.",
  "atlas_binding": { "prefer": ["slorksmo/Human-Atlas@5bb5713"], "rule": "Overlays and copy only — no new viewer, no new meshes." },
  "layers": [
    { "id": "exo.estrogen.male", "label": "Outside estrogens (♂)", "sex": "male" },
    { "id": "exo.androgen.female", "label": "Outside androgens (♀ mirror)", "sex": "female" }
  ],
  "regions": [
    {
      "id": "thorax.breast",
      "layer": "exo.estrogen.male",
      "sex": "male",
      "parent_region": "thorax",
      "hotspot": true,
      "mesh": { "male": false },
      "receptor_overlay_ids": ["breast"],
      "atlas_targets": [{ "project": "slorksmo/Human-Atlas", "mesh_or_system_hint": "anchor only: FJ2810 Skin (FMA7163), anterior thorax; no male breast mesh" }],
      "title": "Breast gland",
      "hover": "Grows when the estrogen/androgen balance tips. Patch estradiol: 86% gynecomastia. Soy: extreme-intake case reports only.",
      "badges": { "evidence": "HUMAN", "class": ["pharma-E2", "phytoestrogen"], "strength": { "pharma-E2": "strong", "phytoestrogen": "weak" } },
      "cites": ["PMID 33581820", "PMID 18558591", "PMID 17659215"],
      "dig_deeper": "white-papers/soy-estrogen-male-exogenous.md#5-gynecomastia",
      "figure": "figures/soy-estrogen/hover-breast-male.png"
    },
    {
      "id": "head-neck.larynx",
      "layer": "exo.androgen.female",
      "sex": "female",
      "parent_region": "head-neck",
      "hotspot": false,
      "map_status": "not yet wired: add head-neck.larynx as a head-neck child before build",
      "atlas_targets": [{ "project": "slorksmo/Human-Atlas", "mesh_or_system_hint": "HRAF0770 Thyroid cartilage; HRAF0769 Cricoid cartilage" }],
      "title": "Larynx & voice",
      "hover": "Testosterone thickens the vocal folds: mean pitch 125 Hz after 12 months. Adam's apple growth in adults: unmeasured.",
      "badges": { "evidence": "HUMAN", "class": ["androgen"], "strength": "strong" },
      "cites": ["PMID 26678122"],
      "unsourced": ["thyroid cartilage prominence change"],
      "dig_deeper": "white-papers/soy-estrogen-male-exogenous.md#105-larynx-voice-and-the-adams-apple"
    }
  ]
}
```

The other hotspots follow the same pattern. Hotspot `id`s use the §1 canonical region ids, and the `parent_region` ids must match `body-map/regions/index.md`. Every `cites` entry must already appear in the paper.

---

## 3. Asset list (PNG/GIF, STYLE.md palette)

All assets go in `figures/soy-estrogen/`, generated by a script (`notes/soy-estrogen-make-figures.py`, to write), matching `receptors-make-sex-figs.py`.

| File | Type | Content | Paper ref |
|---|---|---|---|
| `affinity-ladder.png` | PNG | ER affinity / transcription threshold: E2, estrone, genistein, equol, daidzein, BPA | Fig 1, §1 |
| `intake-bars.png` | PNG | Log mg/day: PL 0.16 · EU <1 · JP 18 / 76 · soy-formula infant 28–47 | Fig 2, §3, §8 |
| `diet-vs-drug.png` | PNG | Three columns: soy 18 mg/d (no T change) · PATCH (93% castrate, 86% gynecomastia) · de Blok (+3.8 cm) | Fig 3, §8.5 |
| `dev-timeline.png` | PNG | Ages 0–25 by window, with HUMAN/ANIMAL badges | Fig 4, §7 |
| `female-mirror-organs.png` | PNG | ↑ hair, voice, lower face, ovary, lean mass · ↓ breast gland, endometrium · dashed outline = unmeasured (jaw bone, Adam's apple) | Fig 5, §10 |
| `history-lanes.png` | PNG | Fact lane / legend lane; qiu shi = contested marker | Fig 6, §9 |
| `hover-*.png` (×11) | PNG | Mini card art per hotspot (icon + 1 number) | §12 |
| `hpg-feedback.gif` | **GIF** | E2 → hypothalamus/pituitary → LH ↓ → testis T ↓ loop, soft pulse only | §4.1 |
| `breast-12mo.gif` | **GIF** | de Blok breast–chest difference 4.1 → 7.9 cm over 12 months, as a bar growing (not anatomy morphing) | §5 |
| `voice-f0.gif` (optional) | **GIF** | F0 bar falling to 125 Hz over 12 months (Nygren) | §10.5 |

Colour code for strength:
- `signal` fill = strong
- `signal-soft` fill = mixed or weak
- `line` hatched = absent or UNSOURCED
- `alert` only for an "ANIMAL-only" warning edge

---

## 4. Tension note: user requests vs STYLE.md and Atlas Lock

Users and steering have asked for **animation, maps and 3D**. House rules limit what can ship:
- **STYLE.md:** transparent PNG / simple GIF only; no 3D bevels or busy chrome.
- **Atlas Lock:** a pinned viewer commit; overlays only; no new meshes.

How each request is resolved:

| Request | What we ship | What we defer or decline |
|---|---|---|
| Animation | Simple GIFs (pulse, bar growth) | Organ-morph animation, video |
| Maps | Hotspot overlays on the locked atlas | A new viewer or page-app |
| 3D | The existing atlas 3D (already 3D) | New 3D models (male breast gland, clitoris, laryngeal prominence) — **would break Atlas Lock** |
| Interactivity | Hover cards + sex toggle + two dose sliders (if the viewer supports sliders; otherwise static PNG with two scales) | A custom dose simulator |

**Admin decision needed (Maciej):** whether to request upstream meshes for the male breast gland or clitoris (a Lock re-validation) or keep them as hotspots.

---

## 5. Build order (when approved)

1. Write `figures/soy-estrogen/*.png` via a script, using only paper numbers.
2. Write the two overlay JSONs and a `soy-estrogen-male-panel.md`. The hover copy mirrors the paper's *Map panel* boxes.
3. Validate the mesh IDs against the pin (re-run the atlas ID check).
4. Add GIFs last.
5. No web app at any step.

---

## 6. Later / optional

- **VR:** only if the upstream atlas gains a VR mode. No custom VR here.
- **Gut / equol layer:** a `gut-energy.json` cross-link showing daidzein → equol conversion. 25–30% of Western adults vs 50–60% of East Asian adults are producers (Setchell & Clerici 2010, PMID 20519412). It would hook into the existing Food & Energy gut overlay.
- **Poland data layer:** blocked on UNSOURCED Polish data.

---

## 7. ID check log (Whole Body, 2026-11-02)

Checked against Atlas Lock pin `5bb5713aab18d7fe9380c3339eb09f173491ea06` (`body-map/README.md`, not modified), `body-map/regions/`, `overlays/sex-layers.json`, `panels/build_whole_body_panels.py`, `overlays/receptors-overlays.json` and `notes/atlas-packaging-id-recheck-2026-11-01.md`. I changed ids only; no card text or numbers changed.

| Before | After | Reason |
|---|---|---|
| `breast.gland.male` | `thorax.breast` (male_layer, hotspot_only, mesh ♂ false) | Uses the canonical map id. No ♂ breast mesh exists; `FJ2810` is an anchor only. |
| `testis.leydig` (hotspot id) | `pelvis.testis` (+ cross-link `testis.leydig`) | `testis.leydig` is a receptor-overlay id, not a region id. |
| `hpg.hypothalamus-pituitary` | `head-neck.hypothalamus` + `head-neck.pituitary` | The plan's id was invented. ♂ meshes exist, so the status changes from hotspot to mesh. |
| `liver.hepatic` | `abdomen.liver` | Uses the existing child id. The "only `FJ2816`" claim was corrected: concept FMA7197 covers 60 parts. |
| `breast.gland.female` | `thorax.breast` (female_layer) | Uses the canonical map id. |
| `skin.hair.face-body` | `head-neck.skin-hair` (proposed) | Region-prefix convention. Not yet in the map. |
| `head.mandible` (mesh `BM0012`) | `head-neck.mandible` (proposed, hotspot_only, mesh ♀ false) | `head` is not a region id. A borrowed male bone cannot be bound into `female_layer`. |
| `neck.larynx` | `head-neck.larynx` (proposed) | `neck` is not a region id. `HRAF0769`/`HRAF0770` are pin-verified. |
| `pelvis.uterus`, `pelvis.ovary`, `pelvis.clitoris` | unchanged | Already canonical. |

**Still to wire (hotspot stubs only, no new meshes):**
- ♂ `thorax.breast` entry in `sex-layers.json` and a ♂ `breast` receptor row
- `abdomen.liver` binding by conceptId FMA7197
- `head-neck.larynx`
- `head-neck.mandible`
- `head-neck.skin-hair`

Before build, add the pin-verified ids that are not yet in the map to the next packaging-id re-check: `FJ2810`, `FJ2816` / FMA7197, `HRAF0003`, `HRAF0006`, `HRAF0014`, `HRAF0769`, `HRAF0770`.

---
**License:** MIT — © 2026 Corpus Nova contributors. See `/LICENSE`. Third-party atlas meshes retain their own licenses.
