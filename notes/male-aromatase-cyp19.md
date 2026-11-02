![Corpus Nova](../figures/branding/cn-paper-header.png)

# Male aromatase (CYP19A1): where a man's estradiol comes from

---
**Corpus Nova** · Theme 1 (BioChem) · Notes mirror · Pointer target for soy WP §4.1a · Universal readers · PhD-worthy depth · Voice: alien-technology minimal  
**License:** MIT · 2026-11-02
---

**What this is.** This note is about one enzyme and one bookkeeping question. Aromatase (CYP19A1) removes one carbon from an androgen and turns ring A aromatic, which makes an estrogen. In a man, how much of the estradiol (E2) in blood comes from the testis itself, and how much is made on the fly in fat, muscle, bone and brain? Every number carries its source. Bracketed numbers are entry numbers in [`../sources/male-aromatase-cyp19.md`](../sources/male-aromatase-cyp19.md). The long form lives in paper 01 **§7.7** ([`../white-papers/01-human-biology-chemistry-in-vivo.md`](../white-papers/01-human-biology-chemistry-in-vivo.md#77-conversion-in-the-periphery-aromatase-and-5α-reductase)). Library card: [`../library/hormones/male-aromatase-cyp19.md`](../library/hormones/male-aromatase-cyp19.md).

**Ownership.** BioChem owns the enzyme chemistry and the production fractions. Medical Builder owns the soy white paper (`white-papers/soy-estrogen-male-exogenous.md`) and its research note. This file only **offers** a pointer for §4.1a and doesn't edit that body. Receptors owns ERα/ERβ/GPER ([`../library/receptors/esr1.md`](../library/receptors/esr1.md) · [`esr2.md`](../library/receptors/esr2.md) · [`gper1.md`](../library/receptors/gper1.md)), and we only link to them. Nothing here is clinical advice. There is no dosing and no testing guidance. Aromatase-inhibitor papers appear only for their physiology background.

**Row tags.** *measured* means the number appears in the source as written. *review* means a review states it (the primary source it cites is named). *derived* means our own arithmetic on the sources' numbers. **Species on every row.** All rows are HUMAN unless marked RAT.

**Keep two numbers apart.**
- **Conversion share of T output** asks what fraction of a man's testosterone ends up as E2. The tracer value is **0.39%** ([ρ]BB) [1]. Paper 01 gives ~0.2% (Handelsman 2026).
- **Origin share of circulating E2** asks how much blood E2 was made outside the testis. That is **≥ ~73%** (derived) [2], or ~80% (review) [4].

The first is a small slice of a big T stream. The second is most of a small E2 stream. Both are true at once.

## 1. The reaction (chemistry)
| Item | Value | Species | Tag | Source |
|---|---|---|---|---|
| Main reactions | **testosterone → 17β-estradiol (E2)** · **androstenedione → estrone (E1)** · 16α-OH-T → estriol | HUMAN | measured (qualitative) | Ghosh 2009 [17] |
| Steps | **3 oxidations**, each **1 O₂ + 1 NADPH**, with cytochrome P450 reductase. Steps 1–2 hydroxylate the **C19 methyl** (→ 19-aldehyde via gem-diol). Step 3 **aromatizes ring A** | HUMAN | measured / review in paper | Ghosh 2009 [17] |
| Totals per E2 made | **3 O₂ + 3 NADPH** | HUMAN | derived (3 × 1) | [17] |
| Formula change | T C₁₉H₂₈O₂ (288.4) → E2 C₁₈H₂₄O₂ (272.4). A C₁₉H₂₆O₂ (286.4) → E1 C₁₈H₂₂O₂ (270.4). **−1 C** (the C19 methyl) | — | derived (PubChem formulas) | sources unit key |
| E1 → E2 | by **17β-HSD** (type 1 co-localizes with aromatase in bone) | HUMAN | measured (qualitative) / review | Sasano 1997 [11]; de Ronde 2011 [4] |
| Uniqueness | "the only enzyme in vertebrates known to catalyse the biosynthesis of all oestrogens from androgens" | HUMAN | review (in paper) | [17] |
| Preferred substrate in vivo | androstenedione is aromatized "to a greater degree" than T | HUMAN | measured | Longcope 1969 [1] |

## 2. The enzyme and gene
| Item | Value | Species | Tag | Source |
|---|---|---|---|---|
| Gene / locus | ***CYP19A1*, chr 15q21.1** | HUMAN | review (in paper) | Ghosh 2009 [17] |
| Protein | **503 aa** + haem. ER membrane-anchored. Androgen-shaped cleft (Asp309 2.6 Å from the 3-keto O) | HUMAN | measured (crystal, 2.90 Å) | [17] |
| One enzyme, many switches | exons 2–10 identical in all tissues. **Tissue-specific exon 1 / promoter** | HUMAN | measured | Harada 1993 [16] |
| Promoter examples | gonadal **PII** (gonadotropins). Adipose/bone **I.4** (IL-6, IL-11, TNF-α) | HUMAN | review | de Ronde 2011 [4]; testis PII "main one" Carreau 2003 [14] |
| Bone promoter use | fibroblast-type exon **1b** in **23/26** bone samples | HUMAN | measured | Sasano 1997 [11] |
| Bone aromatase Km (androstenedione) | **6–50 nM** (mean 20.4 ± 3.9), "in the range of" placenta | HUMAN (4 ♂ + 11 ♀) | measured | Schweikert 1995 [10] |
| Bone aromatase Vmax | **0.14–1.23 nmol/g DNA/h** | HUMAN | measured | [10] |

## 3. How much E2 a man makes, and from where (the core table)
| Item | Value | Species | Tag | Source |
|---|---|---|---|---|
| **E2 production rate** | **44 µg/24 h** (mean, 4 young men) | HUMAN | measured | MacDonald 1979 [2] |
| E1 production rate | **58 µg/24 h** | HUMAN | measured | [2] |
| E2 production rate, review | **35–45 µg/day** (0.130–0.165 µmol) | HUMAN | review (cites [2, 3]) | de Ronde 2011 [4] |
| E2 production, molar | 44 µg ≈ **0.16 µmol/day** | HUMAN | derived | from [2] |
| T production rate (same men) | **5.7 mg/24 h** | HUMAN | measured | [2]. Paper 01's 5–7 mg/day (Handelsman 2026) agrees |
| E2 **not** explained by peripheral conversion (≈ testis-secreted) | **≤ 12 µg/24 h** | HUMAN | measured | [2] |
| **Testis-secreted share of E2** | **≤ ~27%** (≤ 12 ÷ 44) | HUMAN | derived | from [2] |
| **Extraglandular (peripheral) share of E2** | **≥ ~73%** | HUMAN | derived | from [2] |
| Directly from testes, review | **~20%** | HUMAN | review | de Ronde 2011 [4] (cites Baird 1969 [3], MacDonald [2]) |
| Not directly secreted, review complement | **~80%** | HUMAN | derived (100 − 20) | [4]. Matches paper 01's "about 80%" (Handelsman 2026, not re-read this pass) |
| **Testis-dependent E2** (direct + aromatized testicular T) | **~60%** | HUMAN | review | [4] (cites [5]) |
| From adrenal precursors (rest) | **~40%** | HUMAN | derived (100 − 60) | [4] |
| Testis-dependent E2, elderly men, by DHEAS stratum | **72% → 60% → 52% → 44%** | HUMAN (292 ♂ vs 367 postmenopausal ♀) | measured (model-based subtraction) | de Ronde 2005 [5] |
| Testis-dependent E1, elderly men | **54–34%** | HUMAN | measured (model) | [5] |
| All E1 production | accounted for by **extraglandular** formation | HUMAN | measured | [2] |
| Testis-secreted E1 | **< 5%** of E1 production | HUMAN | measured | Weinstein 1974 [7] |

**Reading.** "Made outside the testis" (~73–80%) and "independent of the testis" (~40%) are **different cuts**. Most peripheral E2 is still made from **testicular T** that travelled to fat, muscle or bone first [4, 5]. Mixing up the two cuts is how textbook numbers drift.

## 4. Peripheral conversion efficiency (tracer studies)
| Item | Value | Species | Tag | Source |
|---|---|---|---|---|
| Transfer constant [ρ]BB **T → E2** | **0.39%** men · 0.15% women | HUMAN | measured | Longcope 1969 [1] |
| Transfer constant [ρ]BB **A → E1** | **1.35%** men · 0.74% women | HUMAN | measured | [1] |
| Conversion ratio T → E2 | **0.0018** men · 0.005 women | HUMAN | measured | [1] |
| Conversion ratio A → E1 | **0.013** men · 0.007 women | HUMAN | measured | [1] |
| Paper 01 "share of T output → E2" | **~0.2%** | HUMAN | review | Handelsman 2026 (corpus). *Different metric from [ρ]BB, so we don't reconcile the two here* |
| Forearm fractional conversion T → E2 | **muscle 0.0007 ± 0.0001** · **adipose 0.0012 ± 0.0002** | HUMAN (15 ♂) | measured | Longcope 1978 [9] |
| Share of total extragonadal aromatization | **muscle 25–30%** · **adipose 10–15%** (if tissue aromatization is assumed constant body-wide) | HUMAN | measured (model assumption stated) | [9] |

**Surprise worth a map callout:** per gram, fat converts better than muscle. But there is so much more muscle that, in Longcope's whole-body extrapolation, muscle carries a **bigger share** [9]. Paper 01 §7.7 says "mainly in fat," which is softer than what this primary paper shows. See the pointer appended there.

## 5. Direct testicular secretion (spermatic-vein gradient)
| Item | Value | Species | Tag | Source |
|---|---|---|---|---|
| Spermatic-vein E2 | **1049 ± 57 pg/mL** (8 men) · **1298 ± 216 pg/mL** (14 men) | HUMAN | measured | Kelch 1972 [6]; Weinstein 1974 [7] |
| Peripheral-vein E2 (same study) | **20 ± 1.6 pg/mL** (≈ 73 pmol/L, derived). Individuals 8–28 pg/mL. RIA, 1972 method | HUMAN | measured | [6] |
| Testis → blood E2 gradient | **~50×** (T gradient: **110×**) | HUMAN | measured | [6] |
| Spermatic-vein E1 | **306 ± 55 pg/mL** | HUMAN | measured | [7] |
| hCG stimulus (experimental) | testicular E2 secretion **8×** | HUMAN | measured | [7] |
| Plasma E2 : T | E2 ≈ **1/200** of T | HUMAN | review | de Ronde 2011 [4] |

## 6. Where CYP19 is switched on (tissue map)
| Site | Finding | Species | Tag | Source |
|---|---|---|---|---|
| **Testis: Leydig cells** | adult aromatase immunostain "always associated with Leydig cells," absent from Sertoli. Activity **0.014–0.55 pmol/mg/h**. Highest at 18–20 y | HUMAN | measured | Brodie 2001 [13] |
| Testis: germ cells / sperm | aromatase in Leydig, germ cells, elongated spermatids (RAT). mRNA + protein in ejaculated **human** sperm | RAT · HUMAN | measured (review of own data) | Carreau 2003 [14] |
| **Adipose** | in vivo T→E2 conversion in subcutaneous fat (see §4). Depot gradient buttocks > thighs > abdomen, rising 2–4× with age, **women only** | HUMAN ♂ (conversion) · HUMAN ♀ (depot map) | measured | Longcope 1978 [9]; Bulun & Simpson 1994 [15] |
| **Muscle** | T→E2 0.0007. **25–30%** of extragonadal aromatization (model) | HUMAN | measured | [9] |
| **Bone** | lining cells, osteoblasts, chondrocytes, marrow adipocytes. mRNA **11.25 ± 9.77 amol/ng RNA**, no age or sex correlation | HUMAN (16 ♂ + 12 ♀ RT-PCR) | measured | Sasano 1997 [11]; Schweikert 1995 [10] |
| **Brain** | CYP19 mRNA temporal **2.29** > hippocampus 1.41 > frontal **0.92** AU. **No sex difference** | HUMAN (54 ♂ + 45 ♀, epilepsy biopsies) | measured (arbitrary units) | Stoffel-Wagner 1999 [12] |
| Also reported | hair, vascular tissue, placenta | HUMAN | review | de Ronde 2011 [4] |
| Local vs circulating | local aromatase "can generate high levels of estradiol locally without significantly affecting circulating levels" | HUMAN (review) | review | Simpson 2002 [19] |

## 7. Map hooks
| Node | Use |
|---|---|
| `pelvis.testis` (male_layer) | §5 + Leydig row in §6. Payload neighbour: [`../body-map/regions/gonads-male-chemistry.md`](../body-map/regions/gonads-male-chemistry.md) |
| fat depots (shared) | §4 adipose rows. Adipose shelf: [`../library/adipose-metabolism/sex-hormones-and-fat.md`](../library/adipose-metabolism/sex-hormones-and-fat.md) |
| skeleton / muscle (shared) | §4 muscle row, §6 bone rows (Bone Metrics, Theme 4) |
| brain (shared) | §6 brain row (Mind sector) |
| Receptors ESR1 / ESR2 / GPER1 | link only. The E2 made here is the ligand they hear |
| Soy WP §4.1a / research note gap #12 | pointer to §3 (see `notes/soy-estrogen-male-research.md` §13a) |

## 8. UNSOURCED (named gaps, not claims)
- The textbook "**~85%**" peripheral figure (no checked primary cite).
- C19 leaving as **formic acid** (textbook, not verified this pass).
- kcat/Vmax of purified human aromatase.
- **Male** adipose CYP19 per depot.
- Obesity's effect on male E2 production rate.
- Leydig vs germ-cell split of testicular E2 (HUMAN).
- Age trend of male extraglandular aromatization (Hemsell 1974 has no abstract).
- Baird 1969 and Longcope 1972 numbers (not read).
- Handelsman 2026's "80%" and "0.2%" (not re-read this pass because of an NCBI captcha. They are consistent with [2, 4]).
- A modern LC-MS/MS male E2 range. That belongs to the soy WP's clinical sections.

---
**License:** MIT © 2026 Corpus Nova contributors. See [`/LICENSE`](../LICENSE). Third-party atlases and anatomy meshes keep their upstream licenses.
