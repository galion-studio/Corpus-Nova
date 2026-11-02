# The Gut as a Reactor
### One tube, four gates, an acid bath, and 38 trillion co-pilots

*Food & Energy Systems · Paper 01 · Map-first content source · Draft v1, 1 Nov 2026*
*Audience: universal · Depth: PhD-worthy · Voice: abstract, easy, fun, simple*

**Feeds:** `body-map/overlays/gut-energy.json` · `body-map/gut-energy-regions.md` · `body-map/regions/abdomen.md` · `library/gut-energy/`  
**Outline (locked):** `white-papers/food-energy-01-gut-as-reactor.OUTLINE.md`  
**Does not build:** 3D viewers or the renderer (reuse open atlases — `notes/github-anatomy-landscape.md`).

> You are a tube with a body wrapped around it. Everything you eat is, technically, still *outside* you until a wall of single cells decides to let it in. This paper walks one meal down that tube: through gates that open on command, through an acid bath near pH 1.5, past enzymes that act like bond-specific keys, and finally into a dark, warm fermenter run by trillions of tenants who pay rent in fatty acids, immune training, and — maybe — mood.

---

## 1. The reactor you carry

Engineers have three classic ways to run a chemical reaction:

- **Batch tank.** Load it, stir it, wait, empty it.
- **Continuous stirred tank.** Feed goes in, product comes out, contents stay well mixed.
- **Plug-flow reactor.** A long pipe. Each slug of feed reacts as it travels, so position along the pipe *is* reaction time.

In 1987, Deborah Penry and Peter Jumars took that vocabulary and applied it to animal guts, asking which reactor designs would extract the most from a given diet (Penry & Jumars 1987). Read the human gut with their lens and the design snaps into focus:

| Stage | Reactor type | What it optimises |
|---|---|---|
| Stomach | Stirred batch-ish tank | Mixing, acid sterilisation, controlled release |
| Small intestine | Plug-flow pipe | Fast enzymatic breakdown + absorption along a gradient |
| Colon | Slow continuous fermenter | Microbial digestion of what we can't break ourselves |

So the gut is not one organ. It is a **three-stage processing plant** in series, each stage tuned for a different kind of chemistry, joined by valves, wired to its own control room, and staffed partly by non-human workers.

The feedstock is other organisms: plants, animals, fungi, microbes. The product is *you* — glucose for the brain, amino acids for muscle, fatty acids for storage, and a stream of signals that tells the rest of the body what just arrived.

*How the product becomes ATP is BioChem territory (`library/biology-chemistry/atp-energy.md`). This paper stops at the factory gate.*

---

## 2. Tube architecture: the production line

![Figure 1. The gut tube as a production line: segments in order, sphincter gates marked, reactor type labelled per stage. Schematic, not to scale.](../figures/gut-energy/gut-energy-tube-and-gates.png)

Unrolled, the adult gut runs roughly **5–8 metres** from lips to anus. The exact number depends on how you measure: living, muscle-toned intestine is shorter than the relaxed intestine measured at autopsy. Here is the line, stage by stage (textbook ranges; Guyton & Hall 2020):

| Segment | Rough size | Job in one line | Typical dwell time |
|---|---|---|---|
| **Mouth** | — | Cut, grind, wet; salivary amylase starts on starch | seconds–minutes |
| **Esophagus** | ~25 cm | Peristaltic conveyor; no digestion | ~5–10 s |
| **Stomach** | ~1–1.5 L fed | Acid tank, protein unlock, storage, metering | ~2–4 h |
| **Duodenum** | ~25 cm | Neutralise + mix with bile and pancreatic juice | minutes |
| **Jejunum** | ~2/5 of the remaining small bowel | Main absorption zone: sugars, amino acids, fats | — |
| **Ileum** | ~3/5 of the remaining small bowel | Mop-up; B12 and bile-acid recovery | small bowel total ~3–5 h |
| **Cecum** | pouch, ~6 cm | Fermenter inlet; appendix hangs here | — |
| **Ascending colon** | right side, upward | Most active fermentation; highest SCFA output | — |
| **Transverse colon** | across the upper belly | Fermentation + water recovery | — |
| **Descending colon** | left side, downward | Water and salt recovery; stool firming | colon total ~12–48 h+ |
| **Sigmoid colon** | S-bend in the pelvis | Holding segment | — |
| **Rectum** | ~12–15 cm | Storage + stretch sensing ("time to go") | variable |
| **Anal canal** | ~3–4 cm | Final double gate | — |

### The surface-area trick

A plug-flow reactor's power scales with its wall area, because the wall is where absorption happens. The small intestine folds its wall three times — circular folds, finger-like **villi**, and the **microvilli** "brush border" on each cell. The total inner surface comes to about **32 m²**, roughly half a badminton court (Helander & Fändriks 2014). That replaced the old "tennis court" factoid, which over-counted. Half a badminton court is still a staggering amount of wall to pack into a belly.

### The control room

The gut runs its own nervous system: the **enteric nervous system**, a mesh of roughly 200–600 million neurons in the gut wall (Furness 2012) — the same league as the spinal cord. It coordinates peristalsis, secretion, and blood flow locally, and keeps running even if the vagus nerve is cut. The brain sends supervisory instructions; the gut does the shop-floor management.

Between meals, a "housekeeper" wave called the **migrating motor complex** sweeps the small intestine roughly every 90–120 minutes, clearing leftovers and discouraging bacteria from creeping upstream. That rumble you hear on an empty stomach is often this sweep.

---

## 3. Sphincters: the gates

A tube that only pushes forward would be a hose. A tube with **gates** becomes a plant: each stage can hold its batch until the chemistry is done. Sphincters are rings of muscle that stay squeezed shut by default and open on cue.

### The four headline gates

| Gate | Between | Holds back | Opens when | When it fails |
|---|---|---|---|---|
| **LES** (lower esophageal sphincter) | esophagus → stomach | Acid moving up | A swallow arrives | Reflux / heartburn (GERD) |
| **Pylorus** | stomach → duodenum | Food that isn't liquid enough yet | Chyme is fine-ground; duodenal feedback allows | Too slow: fullness, nausea; too fast: "dumping" |
| **Ileocecal valve** | ileum → cecum | Colon bacteria flowing backward | Ileal contents arrive, after meals | Backflow can seed the small bowel with colonic microbes |
| **Anal sphincters** (internal + external) | rectum → outside | Everything | Rectal stretch + your decision | Incontinence |

Three design details make these gates clever rather than just tight:

1. **The pylorus is a sieve, not a door.** It lets liquid and particles of roughly a millimetre or two through while the stomach grinds larger lumps back for another cycle. Release is throttled by feedback from the duodenum: fat, acid, and concentrated sugar there slow emptying via hormones such as **CCK** and **secretin**, so the downstream reactor is never overloaded.
2. **The LES has a helper.** The diaphragm muscle wraps around the esophagus where it passes into the belly and adds external pinch. A hiatal hernia separates the two and weakens the seal.
3. **The anal gate is two gates.** The **internal** sphincter is smooth muscle, automatic. The **external** sphincter is skeletal muscle, voluntary. When the rectum stretches, the internal gate relaxes reflexively; the external gate waits for you. The body's only digestive valve with a human on the switch.

### Bonus gates
- **Upper esophageal sphincter** — guards the airway end of the esophagus.
- **Sphincter of Oddi** — meters bile and pancreatic juice into the duodenum, opening under CCK when fat arrives.

---

## 4. Acids and enzymes: the unlock cascade

![Figure 2. The unlock cascade: each food class meets a specific key (acid, detergent, or enzyme) and leaves as an absorbable product down a specific exit route.](../figures/gut-energy/gut-energy-unlock-cascade.png)

Food arrives as big polymers: proteins, starches, fats, nucleic acids. The wall can only absorb small pieces. Digestion is therefore a **cascade of keys**, each cutting one kind of chemical bond. Most cuts are **hydrolysis**: water is used to split a bond.

### Stage 1 — the acid bath (stomach)

**Parietal cells** in the stomach lining run a proton pump (**H⁺/K⁺-ATPase**) that concentrates acid about a million-fold relative to blood, pushing stomach contents to **pH ~1–2** (Guyton & Hall 2020). Why so extreme?

- **Denaturation.** Acid unfolds proteins, exposing their bonds to enzymes.
- **Activation.** Acid converts inactive **pepsinogen** into **pepsin**, a protease that only works at low pH. Pepsin then activates more pepsinogen: a chain reaction.
- **Sterilisation.** Most swallowed microbes die. Comparative work places human stomach acidity at the very acidic end of mammals, closer to carrion-eaters than to many plant-eating primates, consistent with an acid filter against food-borne pathogens (Beasley et al. 2015).
- **Vitamin rescue.** Parietal cells also release **intrinsic factor**, without which vitamin B12 can't be absorbed later in the ileum.

The stomach doesn't digest itself because a layer of mucus loaded with bicarbonate keeps the wall near neutral, and the lining renews constantly.

### Stage 2 — neutralise and emulsify (duodenum)

Acid chyme hits the duodenum and two rescue squads arrive:

- **Pancreatic bicarbonate** raises the pH so pancreatic enzymes can work.
- **Bile** from the liver (stored in the gallbladder) carries **bile acids**, which are biological detergents. They break fat into tiny droplets and then into **micelles**, nanoscale shuttles that carry fat to the wall. About 95% of bile acids are reabsorbed in the terminal ileum and recycled back to the liver several times a day — the **enterohepatic circulation** (Hofmann & Hagey 2008). A detergent loop with near-perfect recycling.

### Stage 3 — the enzyme toolkit (pancreas + brush border)

| Food class | Key(s) | Product |
|---|---|---|
| Starch | Salivary + pancreatic **amylase** → brush-border **maltase, sucrase-isomaltase** | Glucose |
| Lactose (milk sugar) | Brush-border **lactase** | Glucose + galactose |
| Protein | Pepsin → **trypsin, chymotrypsin, elastase, carboxypeptidases** → brush-border peptidases | Amino acids, di- and tripeptides |
| Fat (TAG) | **Pancreatic lipase** (+ colipase), with bile | Fatty acids + monoglycerides |
| Fibre | *No human key* | Passes to colon → microbes |

Pancreatic proteases ship as inactive precursors so they can't digest the pancreas. The safety catch is released only in the gut: **enteropeptidase**, an enzyme on the duodenal brush border, activates **trypsinogen → trypsin**, and trypsin activates everyone else. One master key, mounted exactly where the lock should open.

Notice the last row. Humans carry no enzyme for most dietary fibre. That isn't a bug; it's an outsourcing decision. Section 6 meets the contractors.

---

## 5. Digestion → absorption → routes out

Absorption is where outside becomes inside. The wall is one cell thick, and those cells (**enterocytes**) choose what crosses.

### Water-soluble products → portal vein → liver first

- **Glucose and galactose** ride **SGLT1**, which co-transports sodium: the downhill sodium gradient pays for the uphill sugar move (Wright, Loo & Hirayama 2011). This same coupling is why oral rehydration solution — salt plus sugar — saves lives in diarrhoeal disease.
- **Fructose** uses **GLUT5**.
- All three exit the cell's far side through **GLUT2** into capillaries.
- **Amino acids** use a family of transporters; small peptides use a proton-coupled peptide transporter and are finished off inside the cell.

These capillaries drain into the **portal vein**, which goes straight to the **liver**. The liver gets first look at almost everything absorbed from the gut: a customs office that stores glucose, processes amino acids, and detoxifies what slipped through.

### Fats → lymph → around the liver

Fats take the side door. Inside the enterocyte, fatty acids and monoglycerides are reassembled into TAG, packaged into **chylomicrons**, and released into **lacteals** — lymph vessels in each villus. Lymph flows to the thoracic duct and joins the blood near the heart, so dietary fat reaches muscle and fat tissue *before* passing the liver.

**Handoff → Adipose.** What happens when a chylomicron arrives at a fat-tissue capillary (lipoprotein lipase, re-esterification, lipid droplet growth) is told in `white-papers/adipose-01-how-fat-is-built.md`.

**Handoff → BioChem.** How glucose, fatty acids, and amino acids become ATP lives in `library/biology-chemistry/atp-energy.md` and the BioChem paper.

**Handoff → Cell Physics.** The physics of molecules crossing the mucus layer and the unstirred water layer at the villus surface is Cell Physics territory.

### What reaches the colon

By the end of the ileum, most digestible starch, protein, and fat is gone. What crosses the ileocecal valve is water, salts, fibre, resistant starch, some protein, sloughed cells, and mucus. To us: leftovers. To the colon's tenants: dinner.

---

## 6. The microbiome: co-pilot, not passenger

### Census

The best current estimate for a reference adult is about **3.8 × 10¹³ bacteria** — roughly the same order as our ~3 × 10¹³ human cells, a ratio near 1.3 : 1, not the old 10 : 1 myth (Sender, Fuchs & Milo 2016). Nearly all of them live in the colon, at about 10¹¹ cells per gram of contents, one of the densest microbial ecosystems known.

Density climbs steeply down the tube. The stomach is nearly sterile by comparison, the duodenum sparse, the ileum busier, the colon packed (O'Hara & Shanahan 2006). Acid, bile, and fast flow keep the upstream reactors clean; slow flow and no oxygen make the colon a microbial city.

Their collective genome dwarfs ours. The first large metagenomic catalogue found about 3.3 million non-redundant microbial genes in the human gut, roughly 150 times the human gene count (Qin et al. 2010). The Human Microbiome Project showed that healthy people differ a lot in *which* species they carry, but much less in *which metabolic jobs* get done (Human Microbiome Project Consortium 2012). Different crews, similar shifts.

**Who's on the crew (broad strokes):** two big bacterial groups dominate — **Bacillota** (formerly Firmicutes) and **Bacteroidota** (formerly Bacteroidetes) — with **Actinomycetota** (including *Bifidobacterium*), **Pseudomonadota**, **Verrucomicrobiota** (*Akkermansia*, a mucus specialist), and methane-making archaea such as *Methanobrevibacter*.

### The demilitarised zone

The colon wall is coated by two layers of mucus. The outer layer is loose and full of bacteria. The inner layer is dense and, in healthy conditions, nearly bacteria-free (Johansson et al. 2008). A buffer zone about the thickness of a few cells keeps 38 trillion tenants from touching the building. When it thins, inflammation follows.

### What the tenants make: short-chain fatty acids

Microbes ferment fibre and resistant starch into **short-chain fatty acids (SCFAs)**: mainly **acetate**, **propionate**, and **butyrate**, in roughly a 60 : 20 : 20 ratio (Cummings et al. 1987). Each has a destination:

| SCFA | Main destination | Job |
|---|---|---|
| **Butyrate** | Colon wall cells | Their preferred fuel (Roediger 1980); also a signalling molecule for immune tolerance |
| **Propionate** | Liver (via portal vein) | Feedstock for making glucose; satiety signalling |
| **Acetate** | Bloodstream → body | Fuel for muscle, heart, brain; substrate for lipid synthesis |

Together SCFAs can supply on the order of **5–10% of daily human energy**, more on high-fibre diets (Bergman 1990; den Besten et al. 2013). Not the main power line, but a meaningful auxiliary generator — and the colon's own cells run mostly on it.

SCFAs also act as messages. They bind receptors on gut and immune cells (FFAR2 and FFAR3) and change gene activity, linking diet to hormones, immunity, and the brain (Koh et al. 2016). *Receptor detail → Receptors team.*

### Energy harvest and fat (handoff → Adipose)

Germ-free mice — raised with no microbes — carry less body fat than normal mice. Give them a gut microbiota and they gain fat fast, even while eating less (Bäckhed et al. 2004). Microbiota from obese mice transferred more fat gain than microbiota from lean mice, and carried more genes for breaking down otherwise indigestible carbohydrates (Turnbaugh et al. 2006). Translating these mouse results into human weight regulation is still work in progress, but the principle is clear: **the tenants change how much energy the reactor extracts.**

### Colonisation: installing the crew

Before birth, the gut is essentially unpopulated. The first crew depends on delivery: vaginally born babies pick up communities resembling the mother's vaginal microbes; C-section babies are first colonised by skin-type microbes (Dominguez-Bello et al. 2010). Breast milk carries sugars (human milk oligosaccharides) that infants can't digest but *Bifidobacterium* can — the mother feeding the baby's microbes. Communities mature toward an adult-like configuration over roughly the first three years, and that adult configuration differs across countries and lifestyles (Yatsunenko et al. 2012).

> **Fun fact.** Many people in Japan carry gut bacteria with genes for digesting porphyran, a sugar in red seaweed (nori). The genes appear to have jumped from marine bacteria into a human gut bacterium, likely carried in on seaweed (Hehemann et al. 2010). Diet can install new software in the crew.

---

## 7. Lactose intolerance: the default setting

### The ancestral program

All mammals make lactase as babies, to digest milk sugar. After weaning, lactase production normally falls. That **lactase non-persistence** is the ancestral mammalian default — and still the human majority. A global meta-analysis estimated that about **68% of adults** have lactose malabsorption, with the lowest rates in northern Europe and much higher rates across most of Asia, Africa, and the Middle East (Storhaug, Fosse & Fadnes 2017).

So the evolutionary oddity is not lactose intolerance. It's the ~third of humanity who keep making lactase for life: **lactase persistence**.

### The switch

Lactase persistence in Europeans traces largely to a single-letter change, **−13910 C>T** (rs4988235), sitting about 14,000 DNA letters upstream of the lactase gene *LCT*, inside an intron of a neighbouring gene, *MCM6* (Enattah et al. 2002). It's not a change in the enzyme; it's a change in the **enhancer**, the dimmer switch that keeps the gene on.

In East Africa, different mutations near the same switch (for example −14010 G>C) produce the same trait — **convergent evolution** in real time, within the last several thousand years (Tishkoff et al. 2007). The genomic region around the European allele carries one of the strongest signatures of recent positive selection in the human genome (Bersaglieri et al. 2004). Models place its origin in Europe around 7,500 years ago, among early farming communities (Itan et al. 2009). Several more persistence alleles exist in Arabia and Africa (Ingram et al. 2009; Ségurel & Bon 2017).

### The timing puzzle

Here's the twist. Ancient-DNA and pottery-residue data show that Europeans were using milk for thousands of years *before* the persistence allele became common. Milk use alone doesn't explain the selection. One leading model: in times of famine and infection, drinking milk without lactase caused diarrhoea that could turn deadly, so persistence paid off most during crises (Evershed et al. 2022). Selection by catastrophe, not by daily breakfast. *Deep-time archaeology → Homo Origins.*

### Malabsorption ≠ intolerance

**Malabsorption** means lactose isn't fully absorbed. **Intolerance** means symptoms. The bridge between them is the colon: undigested lactose reaches the fermenter, microbes convert it to gas (hydrogen, CO₂, sometimes methane) and acids, and unabsorbed sugar pulls water in (Misselwitz et al. 2019). Bloating, cramps, and loose stools follow.

The dose matters. An NIH consensus panel concluded most people with lactose malabsorption tolerate about **12 g of lactose** — roughly one cup of milk — in one sitting, more when spread through the day or taken with food (Suchy et al. 2010). Self-diagnosis is unreliable in both directions: many people who believe they are lactose intolerant tolerate modest doses well or don't malabsorb at all, and symptoms often have other causes (Lomer, Parkes & Sanderson 2008).

| | Persistent | Non-persistent |
|---|---|---|
| Adult lactase | high | low |
| Lactose fate | absorbed in jejunum | fermented in colon |
| Typical tolerance | large doses | ~12 g at once; more with meals |
| Global share (adults) | ~1/3 | ~2/3 |

---

## 8. Fermented reintroduction: bringing the crew back on shift

*Educational framing only — not medical advice. People with immune suppression, serious GI disease, pregnancy, or histamine problems should involve a clinician.*

Many people avoid foods for a while: after antibiotics, during an elimination diet, after a lactose scare, or simply out of habit. Fermented foods are a natural candidate to bring back. Here is the science that shapes *how*.

### What counts

The international consensus definition: fermented foods are "foods made through desired microbial growth and enzymatic conversions of food components" (Marco et al. 2021). Two consequences:

- **Not all fermented foods are live.** Sourdough bread is baked; most beer is filtered; shelf-stable sauerkraut is often pasteurised. They're fermented, but their microbes are dead or gone.
- **Live examples** include yogurt and kefir with live cultures, refrigerated unpasteurised sauerkraut and kimchi, many aged cheeses, miso, and kombucha.

Benefits can come from the microbes themselves, from what they made (acids, peptides, vitamins), or from what they removed — such as lactose (Marco et al. 2017).

### Fermented dairy carries its own lactase

Yogurt bacteria contain lactase. In lactose malabsorbers, yogurt produced far less breath hydrogen (a marker of colonic lactose fermentation) than the same lactose in milk — the bacteria digest lactose inside the gut (Kolars et al. 1984). Kefir showed a similar effect in adults with lactose maldigestion (Hertzler & Clancy 2003). Hard aged cheeses contain very little lactose because it was fermented away or drained with the whey. The European Food Safety Authority accepted a health claim that live yogurt cultures improve lactose digestion (EFSA 2010).

The colon can also adapt. After a period of daily lactose feeding, maldigesters showed lower breath hydrogen and fewer symptoms — the microbial crew retrains (Hertzler & Savaiano 1996).

### The strongest human trial so far

In a 10-week Stanford study, adults who gradually ramped up fermented foods (to about six servings a day) increased gut microbiome diversity and lowered **19 inflammatory proteins** in blood, including IL-6. A high-fibre group did not increase diversity over the same window (Wastyk et al. 2021). Small study, one site — but it was randomised, and the ramp-up design itself is instructive.

### More microbes ≠ automatically better

After antibiotics, high-dose probiotic capsules *delayed* the return of people's own native gut communities compared with no intervention or a transplant of their own banked microbes (Suez et al. 2018). Foods aren't capsules, but the lesson stands: the goal is a healthy native crew, not a flood of strangers.

### A reintroduction frame (education, not a protocol)

| Principle | Why |
|---|---|
| **Low and slow** | Gas and bloating usually reflect fermentation load; ramping gives the colon time to adapt (Wastyk's design; Hertzler & Savaiano 1996) |
| **One food at a time** | Lets you tell kefir apart from kimchi in your own response |
| **Start with low-lactose, live forms** if dairy is the issue | Yogurt, kefir, aged cheese carry their own lactase or little lactose |
| **Log it** | Dose, food, symptoms, 24–48 h window |
| **Watch the hidden passengers** | Salt (kimchi, sauerkraut, miso), alcohol (kombucha), histamine and tyramine (aged cheese, ferments), FODMAPs (some ferments) |
| **Respect red flags** | Immune suppression, recent GI surgery, unexplained pain, blood, weight loss → clinician first |

Humans have been doing this for a very long time: chemical residues from pottery at Jiahu, China, point to a fermented rice–honey–fruit drink around 7000 BCE (McGovern et al. 2004).

---

## 9. Microbiome ↔ immunity and mood

![Figure 3. The microbiome as a hub: SCFAs, immune training, the vagus nerve, enteroendocrine signals, and serotonin connect gut tenants to immunity, mood, and energy. Arrows mark evidence-backed routes; dashed arrows are still being tested in humans.](../figures/gut-energy/gut-energy-microbiome-axes.png)

### The gut–immune axis: a training ground

The gut wall faces the largest, busiest antigen load in the body, so it hosts a very large share of the body's immune cells, organised into patches, follicles, and scattered cells that differ along the tube (Mowat & Agace 2014). The job is hard: tolerate food and friendly microbes, attack pathogens.

Microbes actively train that system (Hooper, Littman & Macpherson 2012; Belkaid & Hand 2014):

- **Segmented filamentous bacteria** attach to the mouse gut wall and drive the development of **Th17 cells**, an inflammatory, pathogen-fighting T-cell type (Ivanov et al. 2009). Different microbes, different immune "personalities."
- **Butyrate** from fibre fermentation pushes immature T cells toward **regulatory T cells (Tregs)**, the immune system's brakes (Furusawa et al. 2013; Smith et al. 2013).

So fibre → microbes → butyrate → calmer immune tone is one of the clearest diet–microbe–immunity chains we have. A tighter gut barrier fits the same picture; when barrier proteins loosen, microbial products leak into tissue and immune activation rises (Fasano 2011).

### The gut–brain axis: four cables

The gut and brain talk constantly. Four main cables (Cryan et al. 2019):

1. **The vagus nerve.** About 80% of its fibres carry signals *from* gut *to* brain. In mice, a *Lactobacillus* strain reduced anxiety-like behaviour and changed brain GABA receptors — and cutting the vagus abolished the effect (Bravo et al. 2011; Bonaz, Bazin & Pellissier 2018).
2. **Neuropod cells.** Some gut sensor cells form synapse-like contacts with vagal nerve fibres, sending nutrient signals to the brain within milliseconds (Kaelberer et al. 2018). The gut has a direct wired line, not just a hormonal post.
3. **Serotonin and hormones.** About 90% of the body's serotonin is made in the gut by enterochromaffin cells, and spore-forming gut bacteria boost that production (Yano et al. 2015). Gut serotonin doesn't cross into the brain; it acts on gut motility, platelets, and nearby vagal nerve endings. Gut hormones like GLP-1 and CCK also signal fullness.
4. **Immune and stress chemistry.** Germ-free mice show an exaggerated stress-hormone response, which colonisation can reset — but only if done early in life (Sudo et al. 2004). The crew helps calibrate the stress thermostat.

### What we know in humans (and what we don't)

- In over 1,000 Belgian adults, two bacterial groups (*Coprococcus* and *Dialister*) were depleted in people with depression, even after accounting for antidepressant use (Valles-Colomer et al. 2019).
- Gut microbiota from people with depression, transplanted into microbe-depleted rats, induced depression-like behaviour (Kelly et al. 2016).

That's suggestive, not settled. Most mechanistic evidence comes from mice; human data are mostly associations. The honest map label: **"evidence-backed route in animals; human causality under active study."**

*Receptor-level detail (5-HT₃/5-HT₄, GLP-1R, CCK receptors, FFAR2/3) → Receptors team. Systems overview of the nervous–endocrine–immune trio → Whole Body (`library/whole-body/coordination-trio.md`).*

---

## 10. The evolutionary base of *Homo sapiens*

*Brief frame only. Deep-time papers belong to the **Homo Origins** teammate.*

Our gut is a recent redesign, and it shows.

- **Smaller gut, bigger brain.** Compared with other primates of our size, humans have a relatively small gut — especially a small colon — and a very large brain. The "expensive-tissue hypothesis" proposes that a higher-quality diet let our ancestors shrink one costly organ to afford another (Aiello & Wheeler 1995).
- **Cooking as an external stomach.** Cooking gelatinises starch, denatures protein, and softens food, increasing the energy we extract. Mice fed cooked food gained more than mice fed the same food raw (Carmody, Weintraub & Wrangham 2011). Richard Wrangham argues cooking was a turning point in human evolution, effectively moving part of digestion outside the body (Wrangham et al. 1999; Carmody & Wrangham 2009). How early cooking began is debated — a question for Homo Origins.
- **Starch.** Populations with traditionally high-starch diets carry, on average, more copies of the salivary amylase gene *AMY1* (Perry et al. 2007). More copies → more enzyme → more starch unlock in the mouth.
- **Dairy.** Lactase persistence (Section 7) is one of the clearest cases of recent human genetic adaptation to culture.
- **Acid.** Our very acidic stomach fits an ancestral filter against pathogens in scavenged or stored food (Beasley et al. 2015).
- **Co-evolving crew.** Some gut bacterial lineages split in step with their hominid hosts over millions of years — humans, chimps, bonobos, and gorillas carry related but distinct strains (Moeller et al. 2016). Across mammals, gut communities cluster by both diet and family tree (Ley et al. 2008).
- **Modern drift.** The Hadza hunter-gatherers of Tanzania carry more diverse gut communities that cycle with the seasons; some taxa that vanish in the dry season are rare or absent in industrialised guts (Schnorr et al. 2014; Smits et al. 2017). In mice, low-fibre diets caused microbial extinctions that compounded across generations and weren't fully reversed by restoring fibre (Sonnenburg et al. 2016; Sonnenburg & Sonnenburg 2014).

**Handoff → Homo Origins:** hominin dental and gut anatomy, the archaeology of fire and cooking, the timeline of dairying, AMY1 history, and microbial ancestry belong in their papers. This section is the hook; their papers are the depth.

---

## 11. So what?

Pull back and the design principles are clear:

- **The gut is a series reactor.** Batch tank → plug-flow pipe → fermenter. Each stage has its own chemistry, flow rate, and crew.
- **Gates make it a plant.** Sphincters hold each batch until it's ready and stop backflow of acid or bacteria.
- **Digestion is a key-and-lock cascade.** Acid, detergents, and enzymes each unlock one bond class; the safety catches (pepsinogen, trypsinogen) open only where they should.
- **Two exit routes.** Sugars and amino acids go to the liver first. Fats take the lymph and skip it.
- **We outsource fibre.** Microbes turn what we can't digest into SCFAs that feed the colon wall, tune immunity, and add a few percent to our energy budget.
- **Lactose intolerance is the default.** Lactase persistence is a recent, repeatedly evolved exception.
- **Reintroduction is an ecology problem.** Low, slow, one at a time — and native crew over imported crowds.
- **The gut talks.** Through the vagus, hormones, serotonin, and immune cells, the reactor reports to the brain. How much it steers mood in humans is one of biology's open frontiers.
- **This paper is map fuel.** The hover copy, overlays, and cards are the product; the prose keeps them accurate.

### Open questions
1. How much of human mood variation, if any, is *caused* by gut microbes?
2. Can we define a "healthy microbiome" by function rather than by species list?
3. How fast and how completely can an industrialised microbiome recover lost diversity?
4. Why did lactase persistence spread so late, and so differently, across populations?
5. How much energy does the colon really return to a person on a modern low-fibre diet?

### Map & library pointers
- Overlay: [`../body-map/overlays/gut-energy.json`](../body-map/overlays/gut-energy.json)
- Region notes: [`../body-map/gut-energy-regions.md`](../body-map/gut-energy-regions.md) · [`../body-map/regions/abdomen.md`](../body-map/regions/abdomen.md)
- Library shelf: [`../library/gut-energy/`](../library/gut-energy/)

### Sibling handoffs
| Sibling | Picks up |
|---|---|
| **BioChem** | ATP yield, glycolysis/β-oxidation/TCA, acid–base chemistry (`library/biology-chemistry/`) |
| **Adipose** | Chylomicron → droplet; microbiome-driven fat storage (`white-papers/adipose-01-how-fat-is-built.md`) |
| **Cell Physics** | Transport physics across mucus and the villus surface |
| **Receptors** | CCK, GLP-1, 5-HT₃/5-HT₄, FFAR2/3 receptor stories |
| **Homo Origins** | Deep-time diet, cooking archaeology, dairying, microbial ancestry |
| **Whole Body** | System overview, abdomen meshes and region IDs (`white-papers/whole-body-anatomy-overview.md`) |

---

## Figures

| ID | File | What it shows |
|---|---|---|
| F1 | [`../figures/gut-energy/gut-energy-tube-and-gates.png`](../figures/gut-energy/gut-energy-tube-and-gates.png) | Tube segments in order, sphincter gates, reactor type per stage |
| F2 | [`../figures/gut-energy/gut-energy-unlock-cascade.png`](../figures/gut-energy/gut-energy-unlock-cascade.png) | Food class → key → product → exit route (portal vs lymph vs colon) |
| F3 | [`../figures/gut-energy/gut-energy-microbiome-axes.png`](../figures/gut-energy/gut-energy-microbiome-axes.png) | Microbiome hub ↔ immunity / mood / energy |

Simple schematics, not to scale, transparent backgrounds. Script: `figures/gut-energy/src/make_figures.py`.

---

## Further reading (for the curious)

Full citations, DOIs, PMIDs, and what each one supports: [`../sources/food-energy-01-sources.md`](../sources/food-energy-01-sources.md).

**Frame**
- Penry & Jumars (1987) *Am Nat*. Modeling animal guts as chemical reactors.
- Helander & Fändriks (2014) *Scand J Gastroenterol*. Surface area of the digestive tract — revisited.
- Furness (2012) *Nat Rev Gastroenterol Hepatol*. The enteric nervous system.

**Microbiome**
- Sender, Fuchs & Milo (2016) *PLoS Biol*. Revised cell counts.
- Human Microbiome Project Consortium (2012) *Nature*.
- den Besten et al. (2013) *J Lipid Res* · Koh et al. (2016) *Cell*. SCFAs.
- Turnbaugh et al. (2006) *Nature*. Energy harvest.

**Lactose**
- Enattah et al. (2002) *Nat Genet* · Tishkoff et al. (2007) *Nat Genet*.
- Evershed et al. (2022) *Nature*. Dairying, diseases, and lactase persistence.
- Storhaug et al. (2017) *Lancet Gastroenterol Hepatol*. Global prevalence.

**Fermented foods**
- Marco et al. (2021) *Nat Rev Gastroenterol Hepatol*. ISAPP consensus.
- Wastyk et al. (2021) *Cell*. Fermented-food diet and immune status.

**Immunity & mood**
- Belkaid & Hand (2014) *Cell*. Microbiota in immunity.
- Cryan et al. (2019) *Physiol Rev*. The microbiota–gut–brain axis.

**Evolution (hook; depth → Homo Origins)**
- Aiello & Wheeler (1995) *Curr Anthropol*. Expensive-tissue hypothesis.
- Perry et al. (2007) *Nat Genet*. AMY1 copy number.
- Moeller et al. (2016) *Science*. Cospeciation of gut microbiota with hominids.
