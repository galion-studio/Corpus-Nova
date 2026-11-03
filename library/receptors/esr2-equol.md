![Corpus Nova](../../figures/branding/cn-paper-header.png)

# ERβ and equol: the soft lock that plant keys prefer

---
**Corpus Nova** · Theme 3 (Receptors) × soy/isoflavones · Nova Sheet · Universal readers · Voice: easy, abstract, a little fun  
**License:** MIT · 2026-11-02
---

**Plain idea:** Estrogen has two nuclear locks, ERα and ERβ. Estradiol opens both with a near-perfect fit. Soy's plant keys (genistein, daidzein, and equol, which some gut bacteria make from daidzein) fit much more loosely, and they **lean toward ERβ**. This card is only about that fit: **how tightly, and which lock they prefer.** What soy does to hormones in a real body is a different question, and it lives elsewhere (see Links).

**Exact name:** Estrogen receptor beta · gene `ESR2` · nuclear receptor **NR3A2** · ligands in this card: **17β-estradiol (E2)** as the reference key; **genistein**, **daidzein**, **S-(−)-equol** as plant/microbial keys. Short general card: [`esr2.md`](esr2.md).

**How to read the tags:** **IN-VITRO** = receptor protein or cells in a dish (binding or reporter assays). **RAT** = rat receptor. **HUMAN** = measured in people. **REVIEW** = a review stating the point, not a new measurement. A dish Kd is **not** a human tissue Kd.

## Affinity and selectivity

| Measure | Value | Species / assay | Source |
|---|---|---|---|
| E2 grip, ERα vs ERβ (Kd) | **≈ 0.1 nM (ERα)** vs **≈ 0.4 nM (ERβ)** | **IN-VITRO** (ligand-binding assay, ERα and ERβ protein; not human tissue) | Kuiper et al. 1997 |
| E2 grip at ERβ (Kd), follow-up study | **0.05–0.1 nM** | **IN-VITRO** | Kuiper et al. 1998 |
| E2 grip at ERβ (Kd), first report | **≈ 0.6 nM** | **RAT · IN-VITRO** (cloned rat ERβ, original cloning paper) | Kuiper et al. 1996 |
| Genistein: which lock? | prefers **ERβ over ERα**; binds ERβ about as well as **estrone** | **IN-VITRO** | Kuiper et al. 1997 |
| ERβ potency order | **E2 ≫ genistein = coumestrol > zearalenone > daidzein** | **IN-VITRO** | Kuiper et al. 1998 |
| Where gene switching starts | phytoestrogens **1–10 nM**; BPA-type industrial chemicals **100–1000 nM** | **IN-VITRO** (transcription assay) | Kuiper et al. 1998 |
| Equol: which lock? | binds **ERα and ERβ**; natural **S-(−)** form **prefers ERβ** | **REVIEW** (no Kd stated here) | Setchell et al. 2002; Setchell & Clerici 2010 |
| Genistein / daidzein / equol Kd, Ki or RBA % at human native ERβ | — | — | **UNSOURCED** |

**Reading the table, in one breath:** E2 is the master key at sub-nanomolar grip on both locks, with a tilt toward ERα in that 1997 assay. Genistein is a decent ERβ key (estrone-class), daidzein sits near the bottom of the list, and equol is daidzein's gut-upgraded cousin that also leans ERβ. "Leans ERβ" is a **preference**, not a number. We don't turn it into one.

## Who even makes equol? (context, not affinity)

| Measure | Value | Species | Source |
|---|---|---|---|
| Equol producers | **25–30%** of Western adults vs **50–60%** in Japan, Korea, China | **HUMAN** (population frequency, from a review) | Setchell & Clerici 2010 |

Same soy, different gut, different key. This is why equol matters for the ERβ story. It tells you **who has the key**, not **how hard it turns the lock**.

## What this card does *not* own

- **Hormone levels in men:** a meta-analysis found no change in testosterone and related hormones with soy/isoflavone intake (Reed et al. 2021, **HUMAN**). That is an intake/outcome fact, owned by the hormones stub and the soy white paper, not a receptor fact → [`../hormones/isoflavones-phytoestrogens.md`](../hormones/isoflavones-phytoestrogens.md).
- **Intake, diet, plasma levels, puberty, semen:** Medical Builder's soy white paper (§1.3 onward) and the hormones stub.
- **Dosing:** out of scope. None here.

## UNSOURCED (named gaps, not claims)
Absolute Kd / Ki / RBA % for **genistein, daidzein or equol** at **human native ERβ** (the corpus has preference and rank order only) · equol Kd at ERα or ERβ in any assay · S-(−) vs R-(+) equol selectivity as a number · **HUMAN** tissue ERβ density or occupancy with dietary isoflavones · in-vivo **brain** or **prostate** ERβ occupancy from soy intake · a single in-vivo potency ratio of isoflavones vs E2 (also flagged UNSOURCED in the soy WP §1.3) · any claim that equol **"equals"** estradiol (not supported; the 1998 potency order puts E2 far ahead of every plant key) · native human ERβ Kd for E2 (all E2 Kd values above are dish or rat).

## Map

No new region ids. This card hangs off the existing `ESR2` entries in [`../../body-map/overlays/receptors-overlays.json`](../../body-map/overlays/receptors-overlays.json) via [`esr2.md`](esr2.md) (`prostate`, `ovary.follicle.granulosa`). Soy map hotspots (`liver.hepatic`, `testis.leydig`, `breast.gland.male`) belong to the hormones stub's plan.

## Links
- **Short ERβ card:** [`esr2.md`](esr2.md) · sibling lock [`esr1.md`](esr1.md) · fast estrogen GPCR [`gper1.md`](gper1.md)
- **Hormones stub (intake, male hormones):** [`../hormones/isoflavones-phytoestrogens.md`](../hormones/isoflavones-phytoestrogens.md)
- **Medical Builder soy white paper:** [`../../white-papers/soy-estrogen-male-exogenous.md`](../../white-papers/soy-estrogen-male-exogenous.md) §1.1–1.3 (two kinds of "estrogen")
- **Affinity table (research notes):** [`../../notes/soy-estrogen-male-research.md`](../../notes/soy-estrogen-male-research.md) §1
- **Bibliography:** [`../../sources/soy-estrogen-male.md`](../../sources/soy-estrogen-male.md) §A (entries 1–4) · Receptors pointer: [`../../sources/receptors-sources.md`](../../sources/receptors-sources.md) §H
- **Receptors paper:** [`../../white-papers/receptors-human-connections.md`](../../white-papers/receptors-human-connections.md) §7 (sex-steroid receptors)

**Key sources:** Kuiper et al. 1997 (PMID 9048584, doi:10.1210/endo.138.3.4979) · Kuiper et al. 1998 (PMID 9751507, doi:10.1210/endo.139.10.6216) · Kuiper et al. 1996 (PMID 8650195) · Setchell, Brown & Lydeking-Olsen 2002 (PMID 12468591, doi:10.1093/jn/132.12.3577) · Setchell & Clerici 2010 (PMID 20519412, doi:10.3945/jn.109.119776) · context only: Reed et al. 2021 (PMID 33383165, doi:10.1016/j.reprotox.2020.12.019). Full entries: [`../../sources/soy-estrogen-male.md`](../../sources/soy-estrogen-male.md) §A, §B.

*A description of mechanism, not medical advice.*

---
**License:** MIT © 2026 Corpus Nova contributors. See [`/LICENSE`](../../LICENSE). Third-party atlas meshes keep their own licenses.
