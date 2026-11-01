# Map panel copy — Sex hormones & reproductive receptors

*Panel text for the body-map UI. Pair with `receptors-overlays.json` (layers `receptors.sex-steroid` and `receptors.hpg-axis`). Each `### id` block matches a region id. Keep each block short: a title, two or three short lines, and a "dig deeper" link. Long-form source: `white-papers/receptors-human-connections.md` §7–§11.*

---

## Layer intro (shown when the layer is switched on)

**Same locks, different keys.**
Males and females carry mostly the same hormone receptors: AR, ERα, ERβ, GPER1, PR, LHCGR, FSHR, GNRHR. What differs is how much of each hormone arrives, which cells carry the receptor, and when. Tap a glowing spot to see who's listening.

**Legend:** ● nuclear receptor (slow, gene-switching) · ◆ membrane receptor (fast, GPCR) · colour = sex view (male / female / both)

**Toggle:** *Male body* (BodyParts3D) · *Female body* (HRA female) · regions marked *both* appear on either body.

---

## The drumbeat (both)

### brain.hypothalamus.kiss-gnrh
**Puberty ignition**
Kisspeptin knocks on ◆KISS1R on GnRH cells, which then fire in pulses. Break KISS1R and puberty never starts.
*Dig deeper →* `library/receptors/gnrhr.md`

### pituitary.anterior
**LH & FSH factory**
◆GNRHR hears each GnRH pulse and sends out LH and FSH. Pulses = go. A constant flood = stop. That's how some prostate-cancer and puberty-blocking drugs work.
*Dig deeper →* `library/receptors/gnrhr.md`

### brain.mpoa
**Care & mating switchboard**
●ERα, ●AR and ◆OXTR meet here. In rats, mothers who give more care carry more estrogen-boosted OXTR in this spot.
*Dig deeper →* `library/receptors/esr1.md`

---

## Male body

### testis.leydig
**Testosterone kitchen**
LH rings ◆LHCGR → cAMP → cholesterol moves into mitochondria → testosterone. The cholesterol move is the slow step.
*Dig deeper →* `library/receptors/testosterone-production.md`

### testis.sertoli
**Sperm nursery staff**
◆FSHR + ●AR. Testosterone works through the *nurse* cells' AR, not the sperm's. Remove that AR and sperm making stalls mid-way.
*Dig deeper →* `library/receptors/ar.md`

### epididymis
**Sperm finishing school**
Surprise: ●ERα, an "estrogen" receptor, soaks up fluid here so sperm leave concentrated. Mice without it are less fertile.
*Dig deeper →* `library/receptors/esr1.md`

### prostate
**Androgen-loving gland**
Turns testosterone into stronger DHT and listens through ●AR. ●ERβ was first discovered in this gland.
*Dig deeper →* `library/receptors/ar.md` · `esr2.md`

### seminal-vesicle
**Fluid factory**
Makes most of the semen fluid and stays active thanks to ●AR.
*Dig deeper →* `library/receptors/ar.md`

### penis.corpus-cavernosum
**Blood-flow switch**
Nerves release nitric oxide (NO). Its receptor, soluble guanylyl cyclase, makes cGMP and relaxes the muscle, so blood rushes in. ◆α1-adrenoceptors keep the muscle squeezed, so it stays soft at rest.
*Fine print:* PDE5 (the target of common ED pills) is an enzyme that breaks down cGMP, not a receptor.

---

## Female body

### ovary.follicle.theca
**Androgen makers**
LH via ◆LHCGR → androgens. Yes, ovaries make androgens. They're the raw material for estrogen.
*Dig deeper →* `library/receptors/lhcgr.md`

### ovary.follicle.granulosa
**Estrogen finishers**
FSH via ◆FSHR switches on aromatase, which turns the theca's androgens into estradiol. Two cells, two receptors, one estrogen. Near ovulation they gain ◆LHCGR, and ●PR becomes essential.
*Dig deeper →* `library/receptors/fshr.md`

### ovary.corpus-luteum
**Progesterone pop-up**
After ovulation the empty follicle becomes a temporary gland. ◆LHCGR keeps it making progesterone, and in early pregnancy the embryo's hCG rings the same bell.
*Dig deeper →* `library/receptors/lhcgr.md`

### fallopian-tube
**Egg's escalator**
●ERα and ●PR tune the tiny beating hairs (cilia) and muscle that carry the egg.

### uterus.endometrium
**Monthly rebuild**
●ERα grows the lining. ●PR makes it ready to host an embryo. ◆GPER1 adds fast estrogen signals.
*Dig deeper →* `library/receptors/pgr.md`

### uterus.myometrium
**Labor engine**
◆OXTR numbers climb all pregnancy and peak in early labor. ●PR keeps the muscle quiet until then.
*Dig deeper →* `library/receptors/oxtr.md`

### cervix
**Gatekeeper**
●ERα → thin, sperm-friendly mucus. ●PR → thick, closed-gate mucus.

### vagina
**Estrogen-fed lining**
●ERα keeps the lining thick and moist. It thins when estrogen falls after menopause.

### breast
**Grow, branch, deliver**
●ERα grows the ducts. ●PR-B branches them in pregnancy. ◆OXTR squeezes milk out at let-down. Males have the same receptors in a small, quiet gland.
*Dig deeper →* `library/receptors/pgr.md` · `oxtr.md`

---

## Sex differences in the "connection" receptors (both)

**Card title:** *Same doors, different traffic*
- **Oxytocin & vasopressin receptors:** in rodents, receptor binding differs between males and females in specific brain areas. It is not a blanket "more in one sex", and behavioural effects can flip by sex (Dumais & Veenema 2016).
- **Estrogen → OXTR:** estradiol can raise OXTR in some brain areas (rat MPOA, lateral septum). That links the steroid layer to the bonding layer (Champagne et al. 2001).
- **µ-opioid receptor:** in a PET study of the same pain intensity, men showed more MOR activation in some regions and women less in the nucleus accumbens (Zubieta et al. 2002).
- **Honest gap:** Many human receptor-imaging studies used mostly men, and there is still no human OXTR PET tracer.

---

## Fact-check footer (shown small)
Claims trace to `sources/receptors-sources.md`. Mesh names: female → slorksmo/Human-Atlas (HRA female v1.10); male → BodyParts3D 4.0 (ashemag/human-atlas, slorksmo male edition). Brain nuclei and cell types are hotspots, not meshes.
