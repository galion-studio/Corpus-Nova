# The menstrual / ovarian cycle — card

**One-liner:** a monthly clock with two hands — the ovary (follicle → ovulation → corpus luteum) and the uterus (shed → build → prepare) — synced by four hormones.

Map: animated state on `pelvis.ovary` + `pelvis.uterus` (female_layer); arrows from `head-neck.pituitary` (shared). Suggested asset: simple 4-frame transparent GIF (`figures/whole-body/` if made).

## Real-world numbers (612,613 ovulatory cycles, 124,648 users) [24]
| Measure | Mean | 95% range |
|---|---|---|
| Cycle length | **29.3 days** | — |
| Follicular phase | **16.9 days** | 10–30 |
| Luteal phase | **12.4 days** | 7–17 |

- The textbook "28 days, ovulate on day 14" is a tidy average, not a rule — most variation lives in the **follicular** phase [24].
- From age 25 to 45, mean cycle length shortens by ~0.18 days per year, mostly by a shorter follicular phase [24].

## Phases
| Phase | Ovary | Hormones | Uterus |
|---|---|---|---|
| **Menstrual** (day 1 →) | new follicle cohort recruited | E2 & P4 low; FSH rising | functional lining sheds |
| **Follicular** | one follicle becomes dominant | **E2 rises** (granulosa aromatase) | lining rebuilds (*proliferative*) |
| **Ovulation** | dominant follicle ruptures | sustained high E2 → positive feedback → **LH surge** | cervical mucus thin, stretchy |
| **Luteal** (~12 days) | corpus luteum | **P4 high**, E2 moderate; LH/FSH suppressed | lining *secretory*; body temperature slightly up |
| → no pregnancy | corpus luteum regresses | P4 falls | menstruation (loop restarts) |
| → pregnancy | hCG from embryo rescues corpus luteum | P4 maintained | lining kept (decidua) |

Mechanism from [7]; numbers from [24]. HPG wiring: `library/hormones/hpg-axis.md`.

## Male counterpart (for the dual-layer UI)
No monthly clock: testosterone has a **daily** rhythm (higher in the morning) and slow age decline [22, 23]; sperm production runs as overlapping ~64-day waves [29].
