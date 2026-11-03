![Corpus Nova](../figures/branding/cn-paper-header.png)

# The Archaic Inside

Neanderthal and Denisovan DNA in living human bodies: how much survived, where it sits on the body map, what it does, and what it probably does not do.

---
**Corpus Nova** · Theme Homo Origins · Paper 02 · Universal readers · PhD-worthy depth · Voice: alien-technology minimal  
**License:** MIT · 2026-11-03
---

**Feeds (proposed, not yet built):** `body-map/overlays/homo-origins-archaic.json` · `library/homo-origins/` (paper-backed shelf) · cross-links `library/evolution/` (eureka shelf)  
**Builds on:** [`homo-origins-01-why-we-run-on-this-hardware.md`](homo-origins-01-why-we-run-on-this-hardware.md) (energy base of the *Homo* body; this paper does not repeat it).  
**Hands off:** receptor biology → Receptors · immune/clinical detail → Whole Body + specialists · fat-depot mechanics → Adipose · reproductive physiology → Sex Biology.

## Abstract

> Every person whose ancestry runs outside sub-Saharan Africa carries a small archive of extinct human DNA. Most of it came from Neanderthals: about 2% of the genome in non-Africans (Green et al. 2010; Skov et al. 2020), from gene flow that ancient genomes now place in a single, extended window roughly 50,500 to 43,500 years ago (Iasi et al. 2024; Sümer et al. 2025). A second archaic group, the Denisovans, known from a finger bone before anyone knew what they looked like (Krause et al. 2010; Reich et al. 2010), left a larger share in Oceania and Island Southeast Asia, with the highest measured level in the Ayta Magbukon of the Philippines (Larena et al. 2021). Spread across many people, surviving Neanderthal fragments cover a large fraction of the Neanderthal genome (Vernot & Akey 2014; Skov et al. 2020), yet most of the introgressed DNA was purged: it is depleted near genes, in conserved regulatory sequence, near testis-expressed genes, and fivefold on the X chromosome (Sankararaman et al. 2014; Petr et al. 2019). What stayed at high frequency clusters on a few body systems: **skin and hair** (keratin, pigmentation), **innate immunity** (Toll-like receptors, antiviral OAS genes), **oxygen sensing** (the Denisovan *EPAS1* haplotype in Tibetans), and **fat distribution** (*TBX15/WARS2* in Greenlandic Inuit) (Huerta-Sánchez et al. 2014; Dannemann et al. 2016; Racimo et al. 2017). Archaic alleles also tune pain sensitivity, progesterone signalling, and the risk of severe COVID-19 in both directions (Zeberg et al. 2020; Zeberg, Kelso & Pääbo 2020; Zeberg & Pääbo 2020, 2021). Many headline trait associations are weaker than first reported, and the largest phenotype scan to date found that most are better explained by neighbouring non-archaic variants (Skov et al. 2020). This paper turns the robust findings into body-map layers and labels the contested ones.

---

## 1. The hook: a body built from more than one species of human

**Answer first:** modern human bodies are not the product of one sealed lineage. Our ancestors met at least two other kinds of human, had children with them, and a measurable slice of that DNA still runs skin, immune, oxygen-sensing, and fat-storage programs today. Most of it was filtered out; what remains is a curated, not random, inheritance.

Paper 01 in this theme read the body as an energy ledger. This paper reads it as a **merge log**. In software, a merge brings code from another branch into the main line; most of it gets reverted when it breaks things, and a few patches stay because they fix something. Human genomes show the same pattern.

The players, in brief:

- **Neanderthals.** Lived across Europe and western Asia and disappeared by about 40,000 years ago (Hajdinjak et al. 2021). High-quality genomes now exist from the Altai Mountains in Siberia (Prüfer et al. 2014), from Vindija Cave in Croatia (Prüfer et al. 2017), and from Chagyrskaya Cave in Siberia (Mafessoni et al. 2020).
- **Denisovans.** A sister group of Neanderthals first identified by DNA alone: a mitochondrial genome from a finger bone in Denisova Cave (Krause et al. 2010), then a nuclear genome (Reich et al. 2010) and a high-coverage (30×) genome (Meyer et al. 2012). For a decade they had a genome but almost no face.
- **Modern humans** (*Homo sapiens*), expanding out of Africa into a Eurasia that was already inhabited.

The first draft Neanderthal genome showed that Neanderthals share more genetic variants with present-day Eurasians than with present-day sub-Saharan Africans, which implied gene flow from Neanderthals into the ancestors of non-Africans before those populations split from each other (Green et al. 2010). That single result changed the textbook picture of replacement without contact.

> **Fun fact.** One of the reference Neanderthal genomes behind these maps comes from a woman who lived about 50,000 years ago in Vindija Cave, Croatia. She was more closely related to the Neanderthals who mixed with our ancestors than the Siberian reference was, which let researchers find 10 to 20% more Neanderthal DNA in living people (Prüfer et al. 2017).

### Map panel
> Region: whole body · Overlay: `body-map/overlays/homo-origins-archaic.json` → `archaic.overview`  
> **Merge log.** Non-Africans carry ~2% Neanderthal DNA; some Oceanian and Philippine groups also carry Denisovan DNA. Most archaic DNA was purged; what survived clusters in skin, hair, immunity, oxygen sensing, and fat distribution.

---

## 2. How much, when, and how we know

**Answer first:** about 2% Neanderthal ancestry in non-Africans, from one main, extended period of mixing around 50,500 to 43,500 years ago, with traces of earlier and more complicated contact. Denisovan ancestry is patchier and came in more than one pulse.

### Reading archaic fragments in a living genome

Introgressed DNA arrives as long chromosome segments. Each generation, recombination cuts them shorter. After tens of thousands of years, the surviving Neanderthal segments in any one person are usually less than about a hundred kilobases long (Sankararaman et al. 2014). They can still be recognised because Neanderthal haplotypes (blocks of variants inherited together) are distinctive: they carry mutations that accumulated during roughly half a million years of separate history.

Two families of methods do the work. **Reference-based** methods compare a modern genome against sequenced Neanderthal and Denisovan genomes (Sankararaman et al. 2014, 2016). **Reference-free** methods look for unusually divergent segments without needing an archaic template (Vernot & Akey 2014; Browning et al. 2018; Skov et al. 2020). The second family matters for Denisovans, because the people who mixed with our ancestors were often only distantly related to the single Siberian individual first sequenced.

### The numbers

- **Per person.** Vernot & Akey (2014) estimated that non-Africans inherit about 1–3% of their genomes from Neanderthals. Skov et al. (2020), analysing 27,566 Icelanders, put it at about 2%.
- **Across people.** Because different people kept different fragments, the population as a whole preserves far more. Vernot & Akey (2014) recovered introgressed sequence spanning about 20% of the Neanderthal genome from 665 Europeans and East Asians. In Iceland, archaic fragments together covered 38.0–48.2% of the callable genome; 84.5% of them matched Neanderthals, 3.3% matched Denisovans, and 12.2% were of unknown origin (Skov et al. 2020).
- **East versus west.** East Asians carry somewhat more Neanderthal ancestry than Europeans, and this difference survives after accounting for selection (Juric, Aeschbacher & Coop 2016).
- **Africa.** African genomes are not zero. A reference-free method found a stronger Neanderthal signal in African individuals than previously thought, explained by back-migration into Africa, mainly from populations ancestral to Europeans, and by earlier gene flow from modern humans *into* Neanderthals (Chen et al. 2020).

### The timing

Ancient modern-human genomes act as time stamps. The 37,000–42,000-year-old man from Peştera cu Oase, Romania, carried about 6–9% Neanderthal DNA, including segments over 50 centimorgans long, which means a Neanderthal ancestor only four to six generations back (Fu et al. 2015). All three individuals sequenced from Bacho Kiro Cave, Bulgaria (about 45,930–42,580 years ago) also had Neanderthal ancestors a few generations back (Hajdinjak et al. 2021). Neither the Oase population nor the Bacho Kiro population is the main source of later Europeans (Fu et al. 2015; Hajdinjak et al. 2021): those were local mixings that did not leave a strong mark on present-day people.

The shared mixing event that does reach all non-Africans has now been dated twice with ancient data. Genomes from Ranis, Germany, and Zlatý kůň, Czechia (about 45,000 years old) carry Neanderthal segments from a single event shared with all non-Africans, dated to about 45,000–49,000 years ago (Sümer et al. 2025). A catalogue of more than 300 genomes spanning the last 50,000 years attributes the vast majority of Neanderthal gene flow to one shared, extended period between about 50,500 and 43,500 years ago (Iasi et al. 2024).

Contact also ran the other way, and earlier. A population that diverged early from other modern humans contributed DNA to the ancestors of the Altai Neanderthals roughly 100,000 years ago (Kuhlwilm et al. 2016). Late Neanderthals even appear to have had their mitochondrial DNA and Y chromosomes replaced by lineages related to modern humans (Petr et al. 2020). Mixing was a recurring event, not a one-off.

### Denisovans: several pulses, several populations

Denisovan ancestry tells a messier story:

- The first nuclear genome suggested Denisovans contributed 4–6% of the genomes of present-day Melanesians (Reich et al. 2010). Later methods put some Oceanians at up to about 5% Denisovan ancestry, larger than their roughly 2% Neanderthal share (Sankararaman et al. 2016).
- Reference-free scans of 5,639 genomes found Denisovan ancestry in East Asians, South Asians, and Papuans, with two components of different similarity to the sequenced Altai Denisovan: at least two separate admixture pulses (Browning et al. 2018).
- Papuans carry variants from two deeply divergent Denisovan lineages that split more than 350,000 years ago; contact with one of them occurred east of the Wallace line and may have continued until near the end of the Pleistocene. A third Denisovan lineage shows up in East Asians (Jacobs et al. 2019).
- The Ayta Magbukon of the Philippines carry the highest level of Denisovan ancestry yet measured, about 30–40% more than Australians and Papuans, consistent with an independent admixture event (Larena et al. 2021).

And archaic groups mixed with each other. "Denisova 11", a bone fragment from Denisova Cave, came from an individual whose mother was a Neanderthal and whose father was a Denisovan; finding a first-generation hybrid among so few sequenced archaic individuals suggests that mixing was common when groups met (Slon et al. 2018).

### Map panel
> Region: whole body · Overlay: `archaic.timeline`  
> **When.** Main Neanderthal mixing ~50.5–43.5 thousand years ago, shared by all non-Africans. Earlier contact ~100 thousand years ago flowed into Neanderthals. Denisovan DNA arrived in at least two pulses from distinct populations.

---

## 3. The great purge: most archaic DNA did not stay

**Answer first:** selection removed much of the archaic DNA soon after it entered. The removal is strongest near genes, in regulatory sequence, near testis-expressed genes, and on the X chromosome. The leading explanation is a load of weakly harmful mutations that Neanderthals carried because their populations were small.

### Where archaic DNA is missing

Sankararaman et al. (2014) mapped Neanderthal haplotypes in 1,004 people and found that regions with reduced Neanderthal ancestry are **enriched for genes**. Two places stand out:

- Genes more highly expressed in **testes** than in any other tissue are especially depleted.
- The **X chromosome** carries about **five times less** Neanderthal ancestry than the autosomes.

Denisovan ancestry shows the same signature: depletion near genes, on the X chromosome, and near testis-expressed genes (Sankararaman et al. 2016). Petr et al. (2019) found that depletion is strongest in regulatory and conserved non-coding regions and in the most conserved parts of protein-coding sequence.

### Why: two explanations, both partly right

1. **Hybrid incompatibility.** The X and testis pattern resembles what other species show when hybrid males have reduced fertility. Sankararaman et al. (2014, 2016) proposed that some archaic alleles lowered male fertility on a modern human genetic background. The El Sidrón Neanderthal Y chromosome, which has never been found in present-day humans, carries protein-coding changes in genes that produce male-specific minor histocompatibility antigens. Mendez et al. (2016) raised the possibility that maternal immune responses to these antigens contributed to reproductive isolation. This remains a hypothesis.

2. **Genetic load and population size.** Neanderthals lived in small, inbred populations. The Altai Neanderthal's parents were related at the level of half-siblings (Prüfer et al. 2014), and both Neanderthal and Denisovan genomes show low genetic diversity (Meyer et al. 2012; Prüfer et al. 2017). Small populations accumulate weakly harmful mutations that selection cannot remove efficiently. Harris & Nielsen (2016) estimated that Neanderthals had at least 40% lower fitness than modern humans on average, and that this load alone predicts the depletion around genes without needing incompatibilities. Juric, Aeschbacher & Coop (2016) likewise found that most selection against Neanderthal ancestry is best modelled as acting on many weakly deleterious alleles that were nearly neutral in small Neanderthal populations but selected against in larger human ones.

The two explanations are not exclusive. Load explains the genome-wide depletion well. The extreme X and testis pattern is harder to explain with load alone, which is why incompatibility remains on the table.

### When the purge happened

An earlier reading of ancient European genomes suggested Neanderthal ancestry declined steadily over 45,000 years. Petr et al. (2019) showed that this apparent decline was an artefact of gene flow between modern human populations; using a statistic that avoids that bias, they found **no change** over that period. Iasi et al. (2024) reached a consistent conclusion from the other direction: most selection on Neanderthal variants, positive and negative, happened **rapidly**, soon after the gene flow.

There is a twist. Harris & Nielsen (2016) also predicted a residual Neanderthal mutational load in non-Africans that reduces fitness by at least 0.5%. And not every archaic allele is new: Rinker et al. (2020) showed that introgression **reintroduced thousands of ancestral alleles** that Eurasians had lost earlier, and that these reintroduced alleles were better tolerated and more often affect gene expression than truly Neanderthal-derived ones.

> **Fun fact.** On your X chromosome, Neanderthal DNA is about five times rarer than on your other chromosomes (Sankararaman et al. 2014). The fertility machinery is where hybrid DNA was least welcome.

### Map panel
> Region: pelvis (male and female layers) · Overlay: `archaic.purge.reproductive`  
> **Least welcome here.** Archaic DNA is most depleted near testis-expressed genes and on the X chromosome. Leading explanations: harmful mutation load from small Neanderthal populations, plus possible hybrid male fertility problems (hypothesis).

---

## 4. What stayed: the archaic toolkit on the body map

**Answer first:** a few archaic haplotypes rose to high frequency, which is the signature of *adaptive introgression* (beneficial alleles borrowed from another population). They cluster on the body's interfaces with a new environment: skin and hair, the innate immune system, oxygen sensing at altitude, and fat distribution in the cold.

Gittelman et al. (2016) identified 126 high-frequency archaic haplotypes as putative targets of adaptive introgression. The loci were enriched for immune genes (including *OAS1/2/3*, *TLR1/6/10*, and *TNFAIP3*) and included pigmentation genes such as *OCA2* and *BNC2*. Many acted as expression quantitative trait loci (eQTLs: variants that change how much of a gene is made), which suggests that archaic DNA mostly turned volume knobs rather than rewriting proteins. Racimo et al. (2015) reviewed the methods and graded the strength of evidence for each example; their caution applies to everything below.

### 4.1 Skin and hair: the outermost layer

The first genome-wide maps found that regions with high frequencies of Neanderthal alleles are enriched for genes affecting **keratin filaments**, the structural proteins of skin, hair, and nails (Sankararaman et al. 2014). Vernot & Akey (2014) independently found Neanderthal adaptive variation at loci involved in skin phenotypes.

In 112,000 UK Biobank participants, Neanderthal DNA was associated with skin tone and hair colour, among other traits. Several Neanderthal alleles at different loci contributed to **both lighter and darker** skin and hair, suggesting Neanderthals themselves varied in these traits (Dannemann & Kelso 2017). Across more than 400 traits, introgressed regions were depleted of heritability for everything **except skin and hair traits** (McArthur, Rinker & Capra 2021). Skin is the one system where the archaic signal is consistently strong.

### Map panel
> Region: skin / scalp · Overlay: `archaic.skin_hair`  
> **Borrowed coat.** Neanderthal-rich regions are enriched for keratin genes. Archaic alleles shift skin tone and hair colour in both directions. Skin and hair are the only trait families where introgressed DNA is not depleted of heritability.

### 4.2 Innate immunity: borrowed local defences

Neanderthals had lived in western Eurasia for a long time before modern humans arrived. Dannemann, Andrés & Kelso (2016) argued that their immune alleles would have been tuned to local pathogens, and found three distinct archaic haplotypes at the *TLR6-TLR1-TLR10* cluster (two Neanderthal-like, one Denisovan-like). Toll-like receptors (TLRs) are sensors on immune cells that recognise molecules from bacteria, fungi, and parasites. The archaic haplotypes change TLR expression and are associated with allergic disease in large cohorts: the same alleles are linked to greater microbial resistance, with a cost in allergy. Deschamps et al. (2016) found that innate immunity genes as a class carry more Neanderthal introgression than the rest of the coding genome, with the *TLR6-TLR1-TLR10* cluster among the highest.

At the level of cells, Quach et al. (2016) measured how monocytes (blood immune cells) from Africans and Europeans respond to bacterial and viral stimuli. Neanderthal admixture introduced regulatory variants into European genomes that preferentially affected **responses to viral challenge**. Enard & Petrov (2018) found that long, frequent, likely adaptive Neanderthal segments are enriched for proteins that interact with viruses, especially RNA viruses: a genetic trace of ancient epidemics.

The COVID-19 pandemic produced the clearest modern test, and it cuts both ways:

- **Risk.** The major genetic risk factor for severe COVID-19, on chromosome 3, is a roughly 50-kilobase segment inherited from Neanderthals. It is carried by about 50% of people in South Asia and about 16% in Europe (Zeberg & Pääbo 2020).
- **Protection.** A Neanderthal haplotype on chromosome 12, in a region encoding the *OAS* proteins that activate antiviral enzymes, is associated with **protection** against severe disease. It is found at substantial frequencies in every region outside Africa, and its frequency in western Eurasia may have risen between 20,000 and 10,000 years ago and again during the last 1,000 years (Zeberg & Pääbo 2021).

The same archaic inheritance raised and lowered risk for one modern virus. An allele that helped against ancient pathogens can be a liability against a new one.

### Map panel
> Region: blood / lymphatic · lungs · Overlay: `archaic.immune`  
> **Borrowed alarms.** Archaic haplotypes at *TLR6-1-10* change TLR expression; linked to microbial resistance and more allergy. Neanderthal regulatory variants tune antiviral responses. For COVID-19: a chr3 Neanderthal segment raises severe-disease risk; a chr12 *OAS* Neanderthal segment lowers it.

### 4.3 Oxygen at altitude: the Denisovan *EPAS1*

The best-documented case of adaptive introgression sits in the blood-oxygen system. *EPAS1* encodes a transcription factor in the hypoxia response pathway. It showed the most extreme signal of positive selection in Tibetans and is associated with differences in haemoglobin concentration at altitude. Huerta-Sánchez et al. (2014) re-sequenced the region in 40 Tibetans and 40 Han Chinese and found a haplotype structure that can be convincingly explained only by introgression from Denisovans or a Denisovan-related population. The selected haplotype was found in Denisovans and Tibetans, and at very low frequency in Han Chinese.

A follow-up on 78 Tibetans dated the story in two steps (Zhang et al. 2021): the haplotype most likely entered the ancestors of Tibetans about **48,700 years ago** (range 16,000–59,500), but selection on it began only about **9,000 years ago** (range 2,500–42,000). The authors concluded that this textbook case of adaptive introgression is really selection on **standing archaic variation**: a borrowed allele that sat at low frequency for tens of thousands of years until people settled at high altitude.

Denisovans themselves had been there first. A Denisovan mandible from Baishiya Karst Cave on the Tibetan Plateau, identified by ancient proteins, is at least 160,000 years old (Chen et al. 2019). Archaic humans occupied the plateau long before *Homo sapiens* arrived.

### Map panel
> Region: thorax / blood · Overlay: `archaic.hypoxia.epas1`  
> **Altitude patch.** Tibetans carry a Denisovan-derived *EPAS1* haplotype linked to haemoglobin regulation at altitude. It entered ~48,700 years ago and was selected from ~9,000 years ago: a dormant download, activated by life on the plateau.

### 4.4 Fat in the cold: *TBX15/WARS2*

The region with the second most extreme selection signal in Greenlandic Inuit contains a deeply divergent haplotype closely related to the Denisovan genome (Racimo et al. 2017). The region holds two genes, *WARS2* and *TBX15*, previously associated with adipose tissue differentiation and **body-fat distribution**. The archaic allele changes expression of both genes in tissues including subcutaneous fat and the adrenal gland, and has been under selection across a much wider region than Greenland. A plausible link to cold adaptation follows from the biology, but the specific physiological benefit has not been demonstrated directly.

### Map panel
> Region: abdomen / subcutaneous adipose · Overlay: `archaic.adipose.tbx15` (→ Adipose for depot mechanics)  
> **Fat-map tweak.** A Denisovan-like haplotype at *TBX15/WARS2*, selected in Greenlandic Inuit and beyond, alters expression of genes that shape where fat is stored.

---

## 5. Quieter dials: nerves, pregnancy, sleep, and the skull

**Answer first:** beyond the clear adaptive cases, archaic alleles nudge many traits by small amounts. Some effects are well characterised at the molecular level; many population-level associations are weak, and several have not survived re-testing.

### Pain: a Neanderthal sodium channel

Nav1.7, encoded by *SCN9A*, is a sodium channel that fires peripheral pain signals. The Neanderthal version carried three amino acid substitutions. Expressed in cells, the full Neanderthal variant shows **reduced inactivation**, so the channel stays active longer, suggesting Neanderthal peripheral nerves were more sensitive to painful stimuli. Through gene flow, the three substitutions occur in about 0.4% of present-day Britons, where they are associated with **heightened pain sensitivity** (Zeberg, Dannemann et al. 2020).

### Pregnancy: a Neanderthal progesterone receptor

The progesterone receptor gene (*PGR*) carries introgressed Neanderthal haplotypes that have reached nearly **20% frequency** in non-Africans. Carriers express more of the receptor. In a British cohort, carriers had more siblings, fewer miscarriages, and less bleeding during early pregnancy, suggesting the Neanderthal alleles promote fertility (Zeberg, Kelso & Pääbo 2020). The same haplotypes had earlier been associated with preterm birth, so the net effect is not simply "better". This is a rare example of archaic DNA that may help the reproductive system, in contrast to the purge described in Section 3. Hand-off → Sex Biology and Receptors for receptor biology.

### Sleep, mood, and other behavioural associations

Two large studies opened this area. In about 28,000 adults of European ancestry linked to electronic health records, Neanderthal alleles were associated with neurological, psychiatric, immunological, and dermatological phenotypes, including depression risk, sun-induced skin lesions (actinic keratosis), hypercoagulation, and tobacco use (Simonti et al. 2016). In UK Biobank, Neanderthal DNA was associated with height, sleeping patterns (chronotype), mood, and smoking status, in addition to skin and hair (Dannemann & Kelso 2017).

Read these as **small statistical tilts**, not as "your Neanderthal side makes you a night owl". McArthur, Rinker & Capra (2021) found that introgressed variants are generally **depleted** for contributions to trait heritability, especially for cognitive traits, while variants shared across multiple Neanderthal populations showed consistent effects on a short list of traits: hair and skin, autoimmunity, chronotype, bone density, lung capacity, and age at menopause. Skov et al. (2020) tested 271 phenotypes in Iceland, found only 5 associations driven by archaic variants, and showed that **most previously reported associations are better explained by nearby non-archaic variants**.

### The skull and the brain: handle with care

Modern humans have a distinctively globular (rounded) braincase. Gunz et al. (2019) derived a globularity score from brain MRI in thousands of present-day people and found that Neanderthal alleles on chromosomes 1 and 18 are associated with slightly **less globular** endocranial shape. These alleles influence the expression of *UBR4* (involved in neurogenesis) and *PHLPP1* (involved in myelination). The effects are small, and the step from braincase shape to cognition is not established.

The most dramatic brain claim is also the most contested. Trujillo et al. (2021) used genome editing to put the archaic version of *NOVA1*, a neural splicing regulator, into human stem cells and reported that the resulting cortical organoids (lab-grown mini-brain tissue) developed more slowly and had more complex surfaces. Maricic et al. (2021) re-analysed the deposited sequencing data and reported that the edited cell lines carried unintended heterozygous deletions at the target site, which could explain the effects. In their response, the original authors confirmed a deletion in only one clone and maintained their interpretation (Herai et al. 2021). For the map, this stays labelled **unresolved**.

### Map panel
> Region: peripheral nerves · Overlay: `archaic.nerve.nav1_7`  
> **Louder pain wire.** A Neanderthal *SCN9A* (Nav1.7) variant in ~0.4% of Britons slows channel inactivation and is linked to higher pain sensitivity.

### Map panel
> Region: pelvis (female layer) · uterus · Overlay: `archaic.reproductive.pgr`  
> **Pregnancy receptor.** Neanderthal *PGR* haplotypes (~20% of non-Africans) raise receptor expression; carriers report fewer miscarriages and less early-pregnancy bleeding. Earlier linked to preterm birth: net effect still debated.

### Map panel
> Region: head / brain · Overlay: `archaic.cranium` (status: low confidence)  
> **Rounder or not.** Neanderthal alleles near *UBR4* and *PHLPP1* go with slightly less globular braincases on MRI. Archaic *NOVA1* organoid results are disputed. No established effect on cognition.

---

## 6. Putting faces on the Denisovans

**Answer first:** until recently Denisovans were a genome without a body. Ancient proteins and DNA have now tied them to a jaw from Tibet, a jaw from the seafloor off Taiwan, and a nearly complete skull from northeastern China. The picture is of robust jaws and teeth, and a range from Siberia to the subtropics.

- **Xiahe mandible** (Tibetan Plateau, at least 160,000 years old): identified by ancient protein analysis; the first Denisovan evidence outside the Altai (Chen et al. 2019).
- **Penghu 1** (dredged from the Penghu Channel off Taiwan; best age estimates 10,000–70,000 or 130,000–190,000 years ago): a male Denisovan identified from 4,241 recovered amino acid residues, including two Denisovan-specific variants. It extends their range into warm, humid regions and shares their robust jaw and tooth morphology, in marked contrast to Neanderthals (Tsutaya et al. 2025).
- **The Harbin cranium** (northeastern China, at least 146,000 years old): originally named a new species, *Homo longi*, on morphology (Ji et al. 2021). In 2025 it yielded 95 endogenous proteins with three Denisovan-derived amino acid variants (Fu, Bai et al. 2025) and Denisovan mitochondrial DNA from dental calculus (hardened plaque) linked to an early Denisovan branch known from Denisova Cave (Fu, Cao et al. 2025). Together these give the first nearly complete Denisovan skull. Whether the name *Homo longi* should take precedence as the species name for Denisovans is a taxonomic question that is still debated and is not settled by these data.

Before these finds, Gokhman et al. (2019) attempted to predict Denisovan anatomy from patterns of DNA methylation inferred from ancient genomes, proposing features such as an elongated face, a wide pelvis, and an increased dental arch. The method is indirect, and its predictions can now be tested against real Denisovan bones. For the map, predicted traits should be labelled as predictions.

### Map panel
> Region: head (mandible, cranium) · Overlay: `archaic.denisovan.morphology`  
> **A face at last.** Denisovan identity confirmed by proteins or DNA for jaws from Tibet and Taiwan and the Harbin skull (≥146 thousand years old). Robust jaws and large teeth; range from Siberia to subtropical Asia.

---

## 7. What is robust and what is still argued

### Robust

1. **Non-Africans carry about 2% Neanderthal ancestry** from gene flow before the split of Eurasian populations (Green et al. 2010; Skov et al. 2020).
2. **The main Neanderthal mixing was shared and dates to roughly 50,500–43,500 years ago** (Iasi et al. 2024; Sümer et al. 2025).
3. **Denisovan ancestry came from multiple, distinct Denisovan populations**, highest in Oceania and the Philippines (Browning et al. 2018; Jacobs et al. 2019; Larena et al. 2021).
4. **Most archaic DNA was removed by selection**, especially near genes, on the X chromosome, and near testis-expressed genes (Sankararaman et al. 2014, 2016; Petr et al. 2019).
5. **A handful of adaptive introgression cases are well supported**: *EPAS1* in Tibetans, the *TLR6-1-10* cluster, and enrichment of skin, hair, and immune loci (Huerta-Sánchez et al. 2014; Dannemann et al. 2016; Gittelman et al. 2016).

### Still argued

1. **Why the purge happened.** Mutation load from small Neanderthal populations explains much of it (Harris & Nielsen 2016; Juric et al. 2016); whether hybrid incompatibility explains the X and testis pattern is open (Sankararaman et al. 2014; Mendez et al. 2016).
2. **How large the trait effects really are.** Early association studies reported many effects (Simonti et al. 2016; Dannemann & Kelso 2017); the largest re-test attributes most of them to non-archaic variants (Skov et al. 2020).
3. **Whether archaic alleles shaped brain development.** Endocranial shape effects are small (Gunz et al. 2019); the *NOVA1* organoid result is disputed (Trujillo et al. 2021; Maricic et al. 2021; Herai et al. 2021).
4. **Denisovan naming and anatomy.** Molecular data now tie Denisovans to specific fossils (Fu, Bai et al. 2025; Fu, Cao et al. 2025; Tsutaya et al. 2025), but species naming and how far methylation-based predictions hold (Gokhman et al. 2019) are not settled.
5. **Net effect of single alleles.** The same archaic segment can be protective in one setting and harmful in another (COVID-19 risk vs protection; *PGR* fertility vs preterm birth).

### Open questions for future papers in this stream

- How much of the "unknown origin" archaic DNA (12.2% of fragments in Iceland; Skov et al. 2020) comes from groups we have not yet sequenced?
- Do the Denisovan lineages that mixed east of the Wallace line correspond to any known fossil population?
- Can ancient proteins identify more Middle Pleistocene Asian fossils, now that dental calculus has yielded Denisovan DNA (Fu, Cao et al. 2025)?
- How do archaic regulatory variants change gene expression across tissues and developmental stages, rather than just in adult blood cells?

---

## 8. Synthesis: what "part Neanderthal" does and does not license

**Answer first:** "you are 2% Neanderthal" is true and mostly inert. The archaic DNA that matters is a short list of borrowed adaptations at the body's interfaces with a new world: skin, immune sensors, oxygen sensing, fat storage. Everything else is a faint and often disputed statistical signal.

| Body-map layer | Archaic source | Locus / signal | Confidence | Key sources |
|---|---|---|---|---|
| Skin, hair | Neanderthal | Keratin-enriched regions; *BNC2*, *OCA2*; tone and colour both ways | High | Sankararaman et al. 2014; Vernot & Akey 2014; Dannemann & Kelso 2017; McArthur et al. 2021 |
| Innate immunity | Neanderthal + Denisovan | *TLR6-1-10*; antiviral regulatory variants; RNA-virus-interacting proteins | High | Dannemann et al. 2016; Deschamps et al. 2016; Quach et al. 2016; Enard & Petrov 2018 |
| Lungs (COVID-19) | Neanderthal | chr3 risk segment; chr12 *OAS* protective segment | High (association) | Zeberg & Pääbo 2020, 2021 |
| Blood / hypoxia | Denisovan | *EPAS1* in Tibetans | High | Huerta-Sánchez et al. 2014; Zhang et al. 2021 |
| Adipose | Denisovan-like | *TBX15/WARS2* in Inuit | Medium (function) | Racimo et al. 2017 |
| Peripheral nerves | Neanderthal | *SCN9A* (Nav1.7), pain sensitivity | Medium | Zeberg, Dannemann et al. 2020 |
| Reproduction | Neanderthal | *PGR* (enriched); X and testis genes (depleted) | Medium / High | Zeberg, Kelso & Pääbo 2020; Sankararaman et al. 2014 |
| Cranium / brain | Neanderthal | Globularity (*UBR4*, *PHLPP1*); *NOVA1* (disputed) | Low | Gunz et al. 2019; Trujillo et al. 2021; Maricic et al. 2021 |

Three design rules follow for the map:

1. **Show depletion as well as presence.** The absence of archaic DNA in reproductive and conserved regions is as informative as its presence in skin and immune genes.
2. **Attach confidence to every hover card.** Use the labels in the table; never show a low-confidence association without its label.
3. **Avoid ancestry determinism.** Archaic alleles shift averages slightly across populations; they do not define individuals, and populations differ in which archaic groups contributed.

Paper 01 explained the energy chassis that every human shares. This paper adds the patch history: borrowed code, mostly reverted, with a few lasting fixes where our ancestors met new skies, new pathogens, and thin air.

### Map panel
> Region: whole body (layer switcher) · Overlay: `body-map/overlays/homo-origins-archaic.json`  
> **Eight archaic layers.** Skin/hair · immunity · lungs · blood/hypoxia · adipose · nerves · reproduction · cranium. Each card carries a confidence label. Depletion maps (X chromosome, testis genes) sit beside presence maps.

---

## Hand-offs to sibling themes

| Topic in this paper | Owner for depth | What they take |
|---|---|---|
| TLRs, Nav1.7, progesterone receptor biology | **Receptors** | Receptor mechanism cards |
| *PGR* in pregnancy; X and testis depletion | **Sex Biology** | Reproductive layer notes |
| *TBX15/WARS2* and fat distribution | **Adipose** | Depot-level mechanics |
| COVID-19 risk loci; allergy; immune clinical notes | **Whole Body** + specialists | Clinical context |
| Energy chassis of *Homo* | **Homo Origins 01** | Already covered; not repeated here |

## Figures (planned, not yet generated)

| # | Proposed file | Shows |
|---|---|---|
| 1 | `figures/homo-origins/homo-origins-archaic-timeline.png` | Contact events: ~100 ka into Neanderthals; ~50.5–43.5 ka main Neanderthal pulse; Denisovan pulses |
| 2 | `figures/homo-origins/homo-origins-archaic-body-map.png` | Eight archaic layers on a body silhouette, with confidence labels |
| 3 | `figures/homo-origins/homo-origins-archaic-purge.png` | Schematic: archaic DNA presence vs depletion (X chromosome, testis genes, conserved regions) |

Figures must use only numbers printed in this paper and its sources.

## Sources

Every reference below was checked on 2026-11-03 against Crossref and/or PubMed (authors, title, journal, year, DOI); the claims attributed to each were checked against its abstract or the publisher page.

1. Browning SR, Browning BL, Zhou Y, Tucci S, Akey JM. Analysis of human sequence data reveals two pulses of archaic Denisovan admixture. *Cell* 2018;173:53–61.e9. doi:10.1016/j.cell.2018.02.031
2. Chen F, Welker F, Shen C-C, et al. A late Middle Pleistocene Denisovan mandible from the Tibetan Plateau. *Nature* 2019;569:409–412. doi:10.1038/s41586-019-1139-x
3. Chen L, Wolf AB, Fu W, Li L, Akey JM. Identifying and interpreting apparent Neanderthal ancestry in African individuals. *Cell* 2020;180:677–687.e16. doi:10.1016/j.cell.2020.01.012
4. Dannemann M, Andrés AM, Kelso J. Introgression of Neandertal- and Denisovan-like haplotypes contributes to adaptive variation in human Toll-like receptors. *Am J Hum Genet* 2016;98:22–33. doi:10.1016/j.ajhg.2015.11.015
5. Dannemann M, Kelso J. The contribution of Neanderthals to phenotypic variation in modern humans. *Am J Hum Genet* 2017;101:578–589. doi:10.1016/j.ajhg.2017.09.010
6. Deschamps M, Laval G, Fagny M, et al. Genomic signatures of selective pressures and introgression from archaic hominins at human innate immunity genes. *Am J Hum Genet* 2016;98:5–21. doi:10.1016/j.ajhg.2015.11.014
7. Enard D, Petrov DA. Evidence that RNA viruses drove adaptive introgression between Neanderthals and modern humans. *Cell* 2018;175:360–371.e13. doi:10.1016/j.cell.2018.08.034
8. Fu Q, Hajdinjak M, Moldovan OT, et al. An early modern human from Romania with a recent Neanderthal ancestor. *Nature* 2015;524:216–219. doi:10.1038/nature14558
9. Fu Q, Bai F, Rao H, et al. The proteome of the late Middle Pleistocene Harbin individual. *Science* 2025;389:704–707. doi:10.1126/science.adu9677
10. Fu Q, Cao P, Dai Q, et al. Denisovan mitochondrial DNA from dental calculus of the >146,000-year-old Harbin cranium. *Cell* 2025;188:3919–3926.e9. doi:10.1016/j.cell.2025.05.040
11. Gittelman RM, Schraiber JG, Vernot B, Mikacenic C, Wurfel MM, Akey JM. Archaic hominin admixture facilitated adaptation to out-of-Africa environments. *Curr Biol* 2016;26:3375–3382. doi:10.1016/j.cub.2016.10.041
12. Gokhman D, Mishol N, de Manuel M, et al. Reconstructing Denisovan anatomy using DNA methylation maps. *Cell* 2019;179:180–192.e10. doi:10.1016/j.cell.2019.08.035
13. Green RE, Krause J, Briggs AW, et al. A draft sequence of the Neandertal genome. *Science* 2010;328:710–722. doi:10.1126/science.1188021
14. Gunz P, Tilot AK, Wittfeld K, et al. Neandertal introgression sheds light on modern human endocranial globularity. *Curr Biol* 2019;29:120–127.e5. doi:10.1016/j.cub.2018.10.065
15. Hajdinjak M, Mafessoni F, Skov L, et al. Initial Upper Palaeolithic humans in Europe had recent Neanderthal ancestry. *Nature* 2021;592:253–257. doi:10.1038/s41586-021-03335-3
16. Harris K, Nielsen R. The genetic cost of Neanderthal introgression. *Genetics* 2016;203:881–891. doi:10.1534/genetics.116.186890
17. Herai RH, Szeto RA, Trujillo CA, Muotri AR. Response to Comment on "Reintroduction of the archaic variant of *NOVA1* in cortical organoids alters neurodevelopment". *Science* 2021;374:eabi9881. doi:10.1126/science.abi9881
18. Huerta-Sánchez E, Jin X, Asan, et al. Altitude adaptation in Tibetans caused by introgression of Denisovan-like DNA. *Nature* 2014;512:194–197. doi:10.1038/nature13408
19. Iasi LNM, Chintalapati M, Skov L, et al. Neanderthal ancestry through time: insights from genomes of ancient and present-day humans. *Science* 2024;386:eadq3010. doi:10.1126/science.adq3010
20. Jacobs GS, Hudjashov G, Saag L, et al. Multiple deeply divergent Denisovan ancestries in Papuans. *Cell* 2019;177:1010–1021.e32. doi:10.1016/j.cell.2019.02.035
21. Ji Q, Wu W, Ji Y, Li Q, Ni X. Late Middle Pleistocene Harbin cranium represents a new *Homo* species. *The Innovation* 2021;2:100132. doi:10.1016/j.xinn.2021.100132
22. Juric I, Aeschbacher S, Coop G. The strength of selection against Neanderthal introgression. *PLoS Genet* 2016;12:e1006340. doi:10.1371/journal.pgen.1006340
23. Krause J, Fu Q, Good JM, et al. The complete mitochondrial DNA genome of an unknown hominin from southern Siberia. *Nature* 2010;464:894–897. doi:10.1038/nature08976
24. Kuhlwilm M, Gronau I, Hubisz MJ, et al. Ancient gene flow from early modern humans into Eastern Neanderthals. *Nature* 2016;530:429–433. doi:10.1038/nature16544
25. Larena M, McKenna J, Sanchez-Quinto F, et al. Philippine Ayta possess the highest level of Denisovan ancestry in the world. *Curr Biol* 2021;31:4219–4230.e10. doi:10.1016/j.cub.2021.07.022
26. Mafessoni F, Grote S, de Filippo C, et al. A high-coverage Neandertal genome from Chagyrskaya Cave. *PNAS* 2020;117:15132–15136. doi:10.1073/pnas.2004944117
27. Maricic T, Helmbrecht N, Riesenberg S, et al. Comment on "Reintroduction of the archaic variant of *NOVA1* in cortical organoids alters neurodevelopment". *Science* 2021;374:eabi6060. doi:10.1126/science.abi6060
28. McArthur E, Rinker DC, Capra JA. Quantifying the contribution of Neanderthal introgression to the heritability of complex traits. *Nat Commun* 2021;12:4481. doi:10.1038/s41467-021-24582-y
29. Mendez FL, Poznik GD, Castellano S, Bustamante CD. The divergence of Neandertal and modern human Y chromosomes. *Am J Hum Genet* 2016;98:728–734. doi:10.1016/j.ajhg.2016.02.023
30. Meyer M, Kircher M, Gansauge M-T, et al. A high-coverage genome sequence from an archaic Denisovan individual. *Science* 2012;338:222–226. doi:10.1126/science.1224344
31. Petr M, Pääbo S, Kelso J, Vernot B. Limits of long-term selection against Neandertal introgression. *PNAS* 2019;116:1639–1644. doi:10.1073/pnas.1814338116
32. Petr M, Hajdinjak M, Fu Q, et al. The evolutionary history of Neanderthal and Denisovan Y chromosomes. *Science* 2020;369:1653–1656. doi:10.1126/science.abb6460
33. Prüfer K, Racimo F, Patterson N, et al. The complete genome sequence of a Neanderthal from the Altai Mountains. *Nature* 2014;505:43–49. doi:10.1038/nature12886
34. Prüfer K, de Filippo C, Grote S, et al. A high-coverage Neandertal genome from Vindija Cave in Croatia. *Science* 2017;358:655–658. doi:10.1126/science.aao1887
35. Quach H, Rotival M, Pothlichet J, et al. Genetic adaptation and Neandertal admixture shaped the immune system of human populations. *Cell* 2016;167:643–656.e17. doi:10.1016/j.cell.2016.09.024
36. Racimo F, Sankararaman S, Nielsen R, Huerta-Sánchez E. Evidence for archaic adaptive introgression in humans. *Nat Rev Genet* 2015;16:359–371. doi:10.1038/nrg3936
37. Racimo F, Gokhman D, Fumagalli M, et al. Archaic adaptive introgression in *TBX15/WARS2*. *Mol Biol Evol* 2017;34:509–524. doi:10.1093/molbev/msw283
38. Reich D, Green RE, Kircher M, et al. Genetic history of an archaic hominin group from Denisova Cave in Siberia. *Nature* 2010;468:1053–1060. doi:10.1038/nature09710
39. Rinker DC, Simonti CN, McArthur E, et al. Neanderthal introgression reintroduced functional ancestral alleles lost in Eurasian populations. *Nat Ecol Evol* 2020;4:1332–1341. doi:10.1038/s41559-020-1261-z
40. Sankararaman S, Mallick S, Dannemann M, et al. The genomic landscape of Neanderthal ancestry in present-day humans. *Nature* 2014;507:354–357. doi:10.1038/nature12961
41. Sankararaman S, Mallick S, Patterson N, Reich D. The combined landscape of Denisovan and Neanderthal ancestry in present-day humans. *Curr Biol* 2016;26:1241–1247. doi:10.1016/j.cub.2016.03.037
42. Simonti CN, Vernot B, Bastarache L, et al. The phenotypic legacy of admixture between modern humans and Neandertals. *Science* 2016;351:737–741. doi:10.1126/science.aad2149
43. Skov L, Coll Macià M, Sveinbjörnsson G, et al. The nature of Neanderthal introgression revealed by 27,566 Icelandic genomes. *Nature* 2020;582:78–83. doi:10.1038/s41586-020-2225-9
44. Slon V, Mafessoni F, Vernot B, et al. The genome of the offspring of a Neanderthal mother and a Denisovan father. *Nature* 2018;561:113–116. doi:10.1038/s41586-018-0455-x
45. Sümer AP, Rougier H, Villalba-Mouco V, et al. Earliest modern human genomes constrain timing of Neanderthal admixture. *Nature* 2025;638:711–717. doi:10.1038/s41586-024-08420-x
46. Trujillo CA, Rice ES, Schaefer NK, et al. Reintroduction of the archaic variant of *NOVA1* in cortical organoids alters neurodevelopment. *Science* 2021;371:eaax2537. doi:10.1126/science.aax2537
47. Tsutaya T, Sawafuji R, Taurozzi AJ, et al. A male Denisovan mandible from Pleistocene Taiwan. *Science* 2025;388:176–180. doi:10.1126/science.ads3888
48. Vernot B, Akey JM. Resurrecting surviving Neandertal lineages from modern human genomes. *Science* 2014;343:1017–1021. doi:10.1126/science.1245938
49. Zeberg H, Dannemann M, Sahlholm K, et al. A Neanderthal sodium channel increases pain sensitivity in present-day humans. *Curr Biol* 2020;30:3465–3469.e4. doi:10.1016/j.cub.2020.06.045
50. Zeberg H, Kelso J, Pääbo S. The Neandertal progesterone receptor. *Mol Biol Evol* 2020;37:2655–2660. doi:10.1093/molbev/msaa119
51. Zeberg H, Pääbo S. The major genetic risk factor for severe COVID-19 is inherited from Neanderthals. *Nature* 2020;587:610–612. doi:10.1038/s41586-020-2818-3
52. Zeberg H, Pääbo S. A genomic region associated with protection against severe COVID-19 is inherited from Neandertals. *PNAS* 2021;118:e2026309118. doi:10.1073/pnas.2026309118
53. Zhang X, Witt KE, Bañuelos MM, et al. The history and evolution of the Denisovan-*EPAS1* haplotype in Tibetans. *PNAS* 2021;118:e2020803118. doi:10.1073/pnas.2020803118

---
**License:** MIT © 2026 Corpus Nova contributors. See [`/LICENSE`](../LICENSE). Text, figures, and map payloads in this paper are MIT. Third-party atlases and anatomy meshes keep their upstream licenses (e.g. CC BY / CC BY-SA); they are not relicensed here.
