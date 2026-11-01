# Outline — The Gut as a Reactor (food-energy-01) · MAP-FIRST

**Theme:** Food & energy systems → map layers + library cards  
**Audience:** Universal; PhD-worthy depth; voice abstract / easy / fun / simple — alien-technology premium  
**Status:** **LOCKED 2026-11-01** (roadmap step 1 complete) · draft landed in the same pass  
**Title:** *The Gut as a Reactor*  
**Subtitle:** *One tube, four gates, an acid bath, and 38 trillion co-pilots*

## Architecture
White paper = content source for:
- `body-map/overlays/gut-energy.json` (segments, sphincters, microbiome hotspots; machine-readable)
- `body-map/gut-energy-regions.md` (region prose + hover fields)
- `body-map/regions/abdomen.md` (GI hover fields appended to the Whole Body seed)
- `library/gut-energy/*` cards  
Do **not** reinvent 3D viewers (`notes/github-anatomy-landscape.md`). Renderer (Rust / NVIDIA) is a sibling lane; this paper ships payloads only.

## Design rule for the whole paper
Treat the gut as a **chemical plant built from a tube**. Every section answers one engineering question:
*What does this stage do to the feedstock? What gate controls flow? Who does the work — host or tenant? Where does the product go?*
Chemical-reactor framing is real, not a metaphor we invented: Penry & Jumars (1987) modelled animal guts as batch, stirred-tank, and plug-flow reactors.

## Sections
1. **Hook — the reactor you carry.** A ~5–8 m processing line that turns other organisms into you. Reactor types: stomach ≈ stirred batch tank, small intestine ≈ plug-flow reactor, colon ≈ continuous fermenter.
2. **Tube architecture.** Mouth → esophagus → stomach → duodenum / jejunum / ileum → cecum → ascending / transverse / descending / sigmoid colon → rectum → anal canal. Lengths, transit times, the ~32 m² inner surface (Helander & Fändriks 2014). The enteric nervous system as the plant's local control room.
3. **Sphincters as gates.** The four headline gates (LES, pylorus, ileocecal valve, anal sphincters) + bonus gates (UES, sphincter of Oddi). Each gate: what it holds back, what opens it, what goes wrong when it leaks.
4. **Acids & enzymes — the unlock cascade.** HCl (parietal cells, pH ~1–2), pepsin, intrinsic factor; bicarbonate neutralisation; bile acids as detergents; pancreatic proteases (trypsin activation cascade), amylase, lipase; brush-border enzymes incl. lactase. Each = a key that opens one bond class.
5. **Digestion → absorption → routes out.** Transporters (SGLT1, GLUT5, GLUT2, peptide transport); fats → micelles → chylomicrons → lymph; water-solubles → portal vein → liver first-pass. **Handoffs:** ATP and pathways → BioChem (`library/biology-chemistry/atp-energy.md`); chylomicron → droplet → Adipose.
6. **Microbiome as co-pilot.** Who's there (Sender 2016 counts; HMP 2012; Qin 2010 gene catalogue); density gradient stomach → colon; mucus "no-fly zone" (Johansson 2008); SCFAs (acetate / propionate / butyrate) and their destinations; colonisation at birth and maturation by ~age 3; microbiome and energy harvest (Bäckhed 2004; Turnbaugh 2006) → Adipose handoff.
7. **Lactose intolerance.** Lactase non-persistence is the ancestral default (~68% of adults; Storhaug 2017). LCT −13910*T (Enattah 2002), convergent African alleles (Tishkoff 2007), selection signals (Bersaglieri 2004), the dairying-vs-selection timing puzzle (Evershed 2022). Malabsorption ≠ intolerance; the colon decides symptoms.
8. **Fermented reintroduction.** Education frame, not medical advice. What counts as fermented (ISAPP 2021); live vs dead; why yogurt / kefir carry their own lactase (Kolars 1984; Hertzler 2003); colonic adaptation (Hertzler & Savaiano 1996); the Stanford fermented-food trial (Wastyk 2021); caveats (Suez 2018; histamine; immunocompromise). "Low, slow, one at a time, log it."
9. **Microbiome ↔ immunity / mood.** Gut-immune axis: SFB → Th17 (Ivanov 2009), butyrate → Treg (Furusawa 2013; Smith 2013). Gut-brain axis: vagus (Bravo 2011; Bonaz 2018), neuropod cells (Kaelberer 2018), serotonin made in gut (Yano 2015), HPA programming (Sudo 2004), human depression associations (Valles-Colomer 2019) and transfer experiments (Kelly 2016). Map-ready depth; causality flagged honestly.
10. **Evolutionary base of *Homo sapiens*.** Smaller gut / bigger brain (Aiello & Wheeler 1995); cooking as external pre-digestion (Wrangham 1999; Carmody 2011); AMY1 copy number and starch (Perry 2007); dairy and lactase persistence; microbes that co-speciated with hominids (Moeller 2016); acid as filter (Beasley 2015); industrialised microbiome drift (Sonnenburg 2016; Smits 2017). **Deliberate handoff → Homo Origins** for deep-time papers.
11. **So what + map/library pointers.** Bullet "design principles"; open questions; payload paths.
12. **Further reading.** Curated; full list in `sources/food-energy-01-sources.md`.

## Figures (transparent PNG)
| ID | Path | Content |
|----|------|---------|
| F1 | `figures/gut-energy/gut-energy-tube-and-gates.png` | Gut tube schematic: segments + sphincter gates + reactor-type labels |
| F2 | `figures/gut-energy/gut-energy-unlock-cascade.png` | Acid/enzyme unlock cascade: food class → key → product → exit route |
| F3 | `figures/gut-energy/gut-energy-microbiome-axes.png` | Microbiome hub ↔ immunity / mood / energy (SCFA, vagus, serotonin, Treg) |
Script: `figures/gut-energy/src/make_figures.py` (matplotlib, `transparent=True`, matches BioChem script style).

## Handoffs (deliberate)
| Sibling | We hand them |
|---------|--------------|
| BioChem | ATP yield, glycolysis/β-oxidation/TCA, acid–base chemistry depth |
| Adipose | Chylomicron → LPL → lipid droplet; microbiome-driven fat storage |
| Cell Physics | Diffusion across mucus/unstirred layer; villus-scale transport physics |
| Receptors | Enteroendocrine receptors (CCK, GLP-1, 5-HT₃/5-HT₄, FFAR2/3 for SCFAs) |
| Homo Origins | Deep-time diet evolution, archaeological dairying, hominin gut anatomy |
| Whole Body | Organ-system overview; abdomen region meshes and IDs |

---
**License:** MIT — © 2026 Corpus Nova contributors. See `/LICENSE`. Third-party atlas meshes retain their own licenses.
