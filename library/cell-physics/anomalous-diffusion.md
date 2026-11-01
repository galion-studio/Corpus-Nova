# Anomalous diffusion

**What it is:** Heat makes molecules random-walk (*Brownian motion*). In open water, the average squared distance travelled (*mean squared displacement*, MSD) grows in step with time: MSD ∝ t. In a crowded cell it can grow more slowly: MSD ∝ t^α with α < 1. That's *subdiffusion*, one kind of anomalous diffusion. Picture a molecule rattling in a cage of neighbors, then now and then hopping to the next cage.

**Evidence:** Tracers in living mammalian cells subdiffuse, bigger ones more strongly, and it persists when the cytoskeleton is disrupted — crowding alone can do it (Weiss et al. 2004). Review: Höfling & Franosch 2013.

**Real numbers:** GFP diffuses at ~87 µm²/s in saline, ~3.2× slower in CHO cytoplasm, but rotates only ~1.5× slower (Swaminathan et al. 1997) — collisions, not thick water, slow it.

**Why it matters:** Search times for signals and enzymes depend on *how* molecules explore. Crowded walks re-check nearby spots ("compact" search), so the starting distance to a target matters a lot (Bénichou et al. 2010).

**Rule of thumb (our arithmetic):** At ~27 µm²/s, crossing a 10 µm cell takes ~1 s; diffusing down a 1 m nerve fiber would take centuries — hence motor proteins.

**See also:** Paper 01; figure `figures/cell-physics/cell-physics-diffusion-paths.png`; `body-map/cell-physics/brain-axon-transport.md`.
**Sources:** `sources/cell-physics-01-sources.md` (#6, #9, #11, #13).
