# The Crowded Cell: Why Physics Feels Different Inside

*Theme 2 — Cell Physics · Paper 01 (series opener)*

**Abstract.** Picture a protein in a glass of water: it drifts, spins, and bumps into things now and then. Now drop it into a living cell, where a fifth to nearly a third of the space is already taken. The laws of physics don't change in there, but the numbers do. Molecules walk strange paths, the "liquid" acts partly like jelly, and a single random kick from heat is about as strong as the cell's own motors. This paper is a field guide to that crowded world.

---

## A test tube tells a gentle lie

Most of what we know about proteins started in a test tube. You purify one protein, put it in buffer (salty water that holds the pH steady), and measure it. Clean, simple, and lonely: the protein takes up well under 1% of the space.

A cell is the opposite. In the gut bacterium *E. coli*, proteins and RNA add up to roughly 300–400 grams per liter of cytoplasm (Zimmerman & Trach, 1991). Cytoplasm is the stuff that fills the cell outside the nucleus. Across cell types, big molecules take up about 20–30% of the volume (Ellis, 2001). Ellis's review title says it best: crowding is "obvious but underappreciated."

So the first rule of cell physics is easy to say: **the inside of a cell is not dilute water. It is a packed, soft material.**

## Crowding is soft-matter physics

*Soft matter* means materials that are easy to squish because thermal energy (heat jiggle) is strong enough to rearrange them. Gels, toothpaste, mayonnaise. Cytoplasm belongs on that list.

The key idea is **excluded volume**: two molecules can't sit in the same place. In a crowd, the space a newcomer *could* use is much smaller than the room's total size (Minton, 1981). Think of a sold-out concert: a huge hall, but few open seats.

That simple fact has big effects (reviewed by Zhou, Rivas & Minton, 2008):

- **Compact shapes win.** A folded or bound pair of molecules takes up less space than two loose ones. So crowding nudges molecules to stick together and fold up.
- **The "effective concentration" goes up.** Chemists call this *activity*: how concentrated a molecule acts, not just how much is there. In a crowd, each molecule behaves as if there were more of it.
- **Size matters.** Small molecules slip through gaps. Big ones feel the crowd much more.

Binding chemistry and metabolism belong to the BioChem series. Our point is physical: **crowding is a geometry problem first.**

## Random walks, crowded edition

Heat makes every molecule wiggle. This is **Brownian motion**: a random walk driven by countless tiny water-molecule kicks. Einstein (1905) showed how to turn this into numbers.

In plain water, the walk follows one clean rule. The average *squared* distance a molecule travels grows in step with time. Physicists call that average the **mean squared displacement (MSD)**:

> MSD ∝ t   (normal diffusion)

How fast this happens is set by the **diffusion coefficient**, *D*. For a ball in a simple liquid, the **Stokes–Einstein relation** says *D* = k_BT / (6πηr). Here k_BT is heat energy, η (eta) is the liquid's thickness (viscosity), and r is the ball's radius. Hotter means faster. Thicker or bigger means slower.

Now go inside. Take green fluorescent protein (GFP), a small barrel a few nanometers across. In salt water it diffused at about 87 µm²/s. In the cytoplasm of Chinese hamster ovary (CHO) cells, it moved about 3.2 times slower (Swaminathan, Hoang & Verkman, 1997). Yet it *rotated* only about 1.5 times slower. Spinning in place barely noticed the crowd. Traveling did. The authors' reading: GFP mostly slows down because it keeps bumping into other big molecules, not because the water itself got thicker.

Better still: as cells swelled from half to twice their normal volume, GFP moved 4.7 times faster. Crowding was turning the dial.

### When the rule breaks

Sometimes the MSD stops growing in step with time. Instead:

> MSD ∝ t^α, with α < 1   (**subdiffusion**, a kind of *anomalous diffusion*)

Anomalous just means "not the textbook rule." With α below 1, spreading keeps slowing down. The molecule rattles in a "cage" of neighbors, then now and then escapes to the next cage (see `cell-physics-diffusion-paths.png`).

Weiss and colleagues (2004) saw exactly this for tracers in living mammalian cells, more so for bigger tracers. Disrupting the cytoskeleton (the cell's scaffold of protein fibers) or internal membranes didn't remove it, so crowding alone can do it. They proposed α as a ruler for "how crowded is it in here?" Höfling & Franosch (2013) review the many ways a crowd bends a random walk.

## Jelly, not honey

Is cytoplasm a thick liquid, like honey? Or a soft solid, like jelly? The fun answer: **it depends on how big you are and how long you look.**

- **Viscous** means it flows and resists flow (honey).
- **Elastic** means it springs back (jelly).
- **Viscoelastic** means both, depending on timing. Silly Putty bounces if you throw it fast. It puddles if you leave it alone.

Size first. Kalwarczyk and colleagues (2011) measured probes from below a nanometer to hundreds of nanometers in human HeLa cells. Tiny probes, smaller than the gaps in the mesh (about 5 nm), felt a viscosity of about 2 mPa·s. That's only a few times water. Large probes felt about 44 mPa·s, around twenty times more. **Same cell, same moment, different "thickness"**, just because of size.

Time next. Poke a cell quickly, and water can't escape the protein-and-fiber mesh fast enough. The cell pushes back like a firm sponge. Wait, and the water seeps through pores and the cell relaxes. Moeendarbary and colleagues (2013) showed this **poroelastic** behavior in living cells. *Poroelastic* means a squishy solid soaked with fluid that moves through its pores. The effect showed up at times below about half a second.

And bacteria go further. Parry and colleagues (2014) found that the bacterial cytoplasm acts like a **glass-forming liquid**. Small things move freely. Things bigger than about 30 nm get caged. When the cells' metabolism (their energy use) was turned off, big particles nearly froze. Switch it on, and the cytoplasm "fluidizes." Living activity keeps the inside stirred.

## Reactions in a maze

Two molecules must meet before they can react. So crowding changes reaction speed in two opposite ways (Zhou, Rivas & Minton, 2008):

- **Meeting is slower.** Slow diffusion delays the first bump. Reactions limited by travel time can slow down.
- **Staying together is easier.** Once partners meet, crowding favors the compact, bound state. Reactions limited by the binding step itself can speed up.

There's a third twist. Normal diffusion in 3D is a sloppy explorer. It wanders off and leaves gaps. Crowded, subdiffusive walks are more **compact**: they check nearby spots again and again. Bénichou and colleagues (2010) showed that in compact search, **the starting distance to the target matters a lot**. They called it "geometry-controlled kinetics." Kinetics just means how fast reactions run. In a crowded cell, *where* you start can matter as much as *how fast* you move. That's one physical reason cells keep partner molecules close.

A quick back-of-envelope sum shows why distance is everything. Take GFP's measured cytoplasm speed, roughly 87 ÷ 3.2 ≈ 27 µm²/s. To wander across a 10 µm cell takes about a second (t ≈ x²/6D). To diffuse down a 1-meter human nerve fiber would take centuries (t ≈ x²/2D ≈ 2 × 10¹⁰ s). Diffusion is great for short trips and hopeless for long ones. That is why nerve cells run motor proteins along fiber tracks. (Our own estimate, from the Swaminathan numbers.)

## The cell's energy money: kT and piconewtons

Everything in a cell is priced in one currency: **k_BT**, the typical energy of heat jiggle. At body temperature (310 K), k_BT ≈ 4.3 × 10⁻²¹ joules.

In cell-sized units:

> **k_BT ≈ 4.3 pN·nm**

A piconewton (pN) is a trillionth of a newton. A nanometer (nm) is a billionth of a meter. So heat can deliver a push of about one piconewton over a few nanometers. That is the same scale as the cell's own machines:

- A single **kinesin** motor (a protein that walks cargo along microtubule tracks) stalls at about 5.5–7 pN and takes 8 nm steps (Visscher, Schnitzer & Block, 1999).
- A single **myosin** (the motor in muscle) pulls with about 3–4 pN (Finer, Simmons & Spudich, 1994).

Do the math: 6 pN × 8 nm ≈ 48 pN·nm ≈ 11 k_BT per kinesin step. Only about ten times thermal noise. Molecular machines work *inside* the storm, not above it.

Size also kills inertia. Purcell's classic talk "Life at low Reynolds number" (1977) showed that for tiny things in water, friction beats momentum. The **Reynolds number** compares the two. For a cell, it is far below 1. Stop pushing, and you stop almost at once. No coasting. It feels like swimming in tar, even though it's mostly water.

## Why it matters in real human cells

Crowding isn't fixed. Your cells change volume all the time, for example when the salt balance around them shifts. Less water means more crowding.

Jalihal and colleagues (2020) shrank mammalian cells with extra-salty (hyperosmotic) medium. Within about 10 seconds, a protein called DCP1A gathered into droplets. Back in normal medium, the droplets dissolved in about 100 seconds. Droplet formation tracked how much the cell shrank, and many proteins built from three or more copies did the same. In the nucleus, one such protein (CPSF6) was pulled away from genes, and the clean "stop" signal at the end of gene readouts faltered. Water loss → crowding → a change in gene output.

These droplets are **biomolecular condensates**: membrane-free compartments that form by phase separation, like oil drops in vinegar (Banani et al., 2017). Crowding pushes them to form. In yeast, the growth regulator mTORC1 sets ribosome levels. Ribosomes are big crowders. Blocking mTORC1 nearly halved ribosome levels and could double how fast particles of 20 nm or larger moved. Ribosome crowding also tuned condensate formation in yeast and in human cells (Delarue et al., 2018).

The dark side: the same push toward sticking can tip into trouble. The ALS-linked protein FUS forms liquid droplets; in the test tube they age into solid fibers, and patient mutations speed this up (Patel et al., 2015). ALS is a disease that kills the nerve cells controlling muscles. Crowding is not the single cause of such diseases. But it is part of the physics stage they play on.

## Takeaways

- A cell is a **crowded soft material**: roughly 20–30% of its volume is big molecules.
- Movement **depends on size**: small things barely notice; big things get caged and can subdiffuse.
- The cytoplasm is **viscoelastic and poroelastic**: liquid-like for some sizes and times, solid-like for others.
- Crowding **slows meetings but favors binding**, and makes distance a key control knob.
- Heat (≈ 4.3 pN·nm) and motors (a few pN × a few nm) live on the **same energy scale**.

Next in the series: how the cell's skeleton turns these piconewtons into shape, stiffness, and motion.

---

## Further reading

All verified (see `sources/cell-physics-01-sources.md` for DOIs).

- Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen. *Annalen der Physik* 17, 549–560.
- Purcell, E. M. (1977). Life at low Reynolds number. *American Journal of Physics* 45, 3–11.
- Minton, A. P. (1981). Excluded volume as a determinant of macromolecular structure and reactivity. *Biopolymers* 20, 2093–2120.
- Zimmerman, S. B. & Trach, S. O. (1991). Estimation of macromolecule concentrations and excluded volume effects for the cytoplasm of *Escherichia coli*. *J. Mol. Biol.* 222, 599–620.
- Finer, J. T., Simmons, R. M. & Spudich, J. A. (1994). Single myosin molecule mechanics: piconewton forces and nanometre steps. *Nature* 368, 113–119.
- Swaminathan, R., Hoang, C. P. & Verkman, A. S. (1997). Photobleaching recovery and anisotropy decay of green fluorescent protein GFP-S65T in solution and cells. *Biophys. J.* 72, 1900–1907.
- Visscher, K., Schnitzer, M. J. & Block, S. M. (1999). Single kinesin molecules studied with a molecular force clamp. *Nature* 400, 184–189.
- Ellis, R. J. (2001). Macromolecular crowding: obvious but underappreciated. *Trends Biochem. Sci.* 26, 597–604.
- Weiss, M., Elsner, M., Kartberg, F. & Nilsson, T. (2004). Anomalous subdiffusion is a measure for cytoplasmic crowding in living cells. *Biophys. J.* 87, 3518–3524.
- Zhou, H.-X., Rivas, G. & Minton, A. P. (2008). Macromolecular crowding and confinement. *Annu. Rev. Biophys.* 37, 375–397.
- Bénichou, O., Chevalier, C., Klafter, J., Meyer, B. & Voituriez, R. (2010). Geometry-controlled kinetics. *Nature Chemistry* 2, 472–477.
- Kalwarczyk, T. et al. (2011). Comparative analysis of viscosity of complex liquids and cytoplasm of mammalian cells at the nanoscale. *Nano Letters* 11, 2157–2163.
- Höfling, F. & Franosch, T. (2013). Anomalous transport in the crowded world of biological cells. *Rep. Prog. Phys.* 76, 046602.
- Moeendarbary, E. et al. (2013). The cytoplasm of living cells behaves as a poroelastic material. *Nature Materials* 12, 253–261.
- Parry, B. R. et al. (2014). The bacterial cytoplasm has glass-like properties and is fluidized by metabolic activity. *Cell* 156, 183–194.
- Patel, A. et al. (2015). A liquid-to-solid phase transition of the ALS protein FUS accelerated by disease mutation. *Cell* 162, 1066–1077.
- Banani, S. F., Lee, H. O., Hyman, A. A. & Rosen, M. K. (2017). Biomolecular condensates: organizers of cellular biochemistry. *Nat. Rev. Mol. Cell Biol.* 18, 285–298.
- Delarue, M. et al. (2018). mTORC1 controls phase separation and the biophysical properties of the cytoplasm by tuning crowding. *Cell* 174, 338–349.
- Jalihal, A. P. et al. (2020). Multivalent proteins rapidly and reversibly phase-separate upon osmotic cell volume change. *Molecular Cell* 79, 978–990.

## Figures

- `figures/cell-physics/cell-physics-crowding-scale.png` — Dilute test tube vs. crowded cytoplasm: soft macromolecule "blobs" around a tracer protein a few nm across, with ~10 nm scale bars (schematic).
- `figures/cell-physics/cell-physics-diffusion-paths.png` — Same number of random steps: a normal Brownian walk spreads out; a crowded walk rattles in cages and hops. Inset: MSD ∝ t vs. MSD ∝ t^α (α < 1), illustrative.


---

## Map / library payloads

This paper feeds the interactive body map and universal library (map-first pipeline). Extract cards live in:

- `body-map/cell-physics/payloads/crowded-cell-map-extract.md`
- `body-map/cell-physics/*.md` (region hover notes, incl. sex-layer physics)
- `library/cell-physics/*.md`

Map UI should reuse open-source anatomy stacks listed in `notes/github-anatomy-landscape.md` — do not invent a new 3D viewer.
