# Testosterone — levels and testicular production

**One-liner:** a cholesterol-built steroid that the testes pour out at about 7 mg a day — and that every woman also makes, in much smaller amounts.

Map: `pelvis.testis` (male_layer, primary) · `pelvis.ovary`, `abdomen.adrenal` (female_layer sources) · HPG control from `head-neck.hypothalamus` / `head-neck.pituitary`.

---

## 1. Where it is made (♂): the Leydig-cell factory
- **Who:** about **500 million Leydig cells** sitting in the *interstitium* (the gaps between seminiferous tubules) [18].
- **Trigger:** pituitary **LH** binds the LH/choriogonadotropin receptor (LHCGR) on Leydig cells → cAMP rises → steroid production speeds up [19, 20].
- **Output:** **3–10 mg per day (mean ~7 mg)** in adult men, versus ~0.3 mg/day in women [18].
- **Share:** in healthy men, circulating testosterone comes **almost exclusively** from Leydig cells; adrenal contribution is minor [18].

### The assembly line (human testis)
| Step | Where | Enzyme / protein | Product |
|---|---|---|---|
| 1. Cholesterol import | outer → inner mitochondrial membrane | **StAR** (rate-limiting delivery) | cholesterol at the enzyme |
| 2. Side-chain cut | mitochondrion | **CYP11A1** (P450scc) | pregnenolone |
| 3. 17α-hydroxylation + 17,20-lyase | smooth ER | **CYP17A1** | 17-OH-pregnenolone → **DHEA** (human Δ5 route preferred) |
| 4. 3β-HSD step | ER | **HSD3B2** | androstenedione |
| 5. Final reduction | ER | **HSD17B3** (testis-specific isoform) | **testosterone** |
| 6. Optional upgrades (target tissue) | prostate, skin, genital tissue / fat, bone, brain | **SRD5A2** / **CYP19A1** | DHT (stronger AR agonist) / estradiol |

Pathway per Miller & Auchus [19] and Payne & Hales [20]. HSD17B3 deficiency or SRD5A2 deficiency are classic "one-enzyme" differences of sex development — proof that each step is load-bearing [19].

## 2. Two concentrations: inside vs outside the testis
- **Inside the testis:** testosterone is about **100× higher than in blood** [17, 18]. Sertoli cells need that local flood to support sperm production.
- Intratesticular **DHT is only ~2%** of testosterone — locally, testosterone itself does the job [17].
- Practical twist: giving testosterone *from outside* suppresses LH via feedback, so intratesticular testosterone falls and sperm production drops — the basis of male hormonal-contraception research [17, 18].

## 3. Levels in blood (♂ and ♀)
| Group | Range (total T, LC-MS / harmonized) | Source |
|---|---|---|
| Healthy non-obese men 19–39 y | **264–916 ng/dL** (≈ 9.2–31.8 nmol/L); median 531 ng/dL | Travison 2017 [16] |
| Healthy men 18–40 y (pooled LC-MS) | **7.7–29.4 nmol/L** | Handelsman 2018 [18] |
| Healthy premenopausal women | **0–1.7 nmol/L** (stays < 2 nmol/L at all ages) | Handelsman 2018 [18] |
| Women with PCOS (upper bound) | ~3.1 nmol/L (95% one-sided) | Handelsman 2018 [18] |

Unit tip: **ng/dL × 0.0347 = nmol/L.**

### What moves the number
- **Time of day:** in men aged 30–40, testosterone is **20–25% lower at 16:00 than at 08:00**; the gap shrinks to ~10% by age 70. Measure in the morning [22].
- **Age:** within-person total testosterone falls ~**1.6% per year** in middle-aged men; bioavailable T falls **2–3% per year**, partly because SHBG rises (~1.6%/yr cross-sectionally) [23].
- **Health:** absence of obesity, chronic illness, and heavy drinking added ~10–15% to several androgen levels [23].
- **Assay:** much between-lab variation is assay drift; harmonizing to the CDC reference method fixes a lot of it [16].
- **Diagnosis (men):** hypogonadism needs **symptoms plus repeated, unequivocally low morning fasting** testosterone — one low afternoon value is not enough [16, 22, 25].

## 4. Where it comes from (♀)
Roughly **equal thirds**: direct ovarian secretion, direct adrenal secretion, and conversion of precursors (DHEA, androstenedione) in liver, kidney, muscle, fat, and skin [18, 26]. Women secrete more androgen than estrogen by mass; much of it is "pro-androgen" (DHEA-S, DHEA, androstenedione) that only becomes active after conversion [26].

## 5. What it does (overview — receptors deep-dive → Receptors theme)
Acts through the **androgen receptor (AR)**, a nuclear receptor, directly or after conversion to DHT; some effects go via estradiol and estrogen receptors. Drives male puberty, spermatogenesis (with FSH), libido, muscle mass, haemoglobin, and bone. The male–female difference in circulating testosterone largely explains sex differences in muscle mass, strength, and haemoglobin [18].

## Map payload (male_layer · `pelvis.testis`)
```yaml
testosterone_facts:
  - "Leydig cells (~500 million) make 3–10 mg/day, mean ~7 mg [18]"
  - "LH → LHCGR → cAMP → StAR → CYP11A1 → CYP17A1 → HSD3B2 → HSD17B3 [19,20]"
  - "Inside testis ≈ 100× blood level [17]"
  - "Adult men 19–39 y: 264–916 ng/dL (harmonized) [16]"
  - "Morning > afternoon by 20–25% in 30–40 y men [22]"
  - "Total T falls ~1.6%/yr within-person in mid-life [23]"
receptor_pointers: [AR, LHCGR, FSHR, SRD5A2, CYP19A1]   # → Receptors theme
```
