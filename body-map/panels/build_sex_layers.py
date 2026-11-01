"""Builds body-map/overlays/sex-layers.json — child structures for the dual-layer (♂/♀) view.
Mesh IDs verified 2026-11-01 against slorksmo/Human-Atlas manifests. Run:
    python3 body-map/panels/build_sex_layers.py"""
import json, pathlib
M, F = "male_layer", "female_layer"
def s(id, layer, title, summary, male=(), female=(), hormones=(), receptors=(), library=(), homolog=None, hotspot=False):
    return {"id": id, "layer": layer, "hover": {"title": title, "summary": summary, "hormones": list(hormones), "receptor_pointers": list(receptors)},
            "atlas": {"male_body": list(male), "female_body": list(female)}, "hotspot_only": hotspot,
            "homolog": homolog, "library": list(library)}
LM, LF, LH = "library/male-reproductive/", "library/female-reproductive/", "library/hormones/"
RX = {"head-neck.hypothalamus": ["brain.hypothalamus.kiss-gnrh", "brain.mpoa"], "head-neck.pituitary": ["pituitary.anterior"],
 "pelvis.testis": ["testis.leydig", "testis.sertoli"], "pelvis.epididymis": ["epididymis"], "pelvis.prostate": ["prostate"],
 "pelvis.seminal-vesicle": ["seminal-vesicle"], "pelvis.penis": ["penis.corpus-cavernosum"],
 "pelvis.ovary": ["ovary.follicle.granulosa", "ovary.follicle.theca", "ovary.corpus-luteum"], "pelvis.uterine-tube": ["fallopian-tube"],
 "pelvis.uterus": ["uterus", "uterus.endometrium", "uterus.myometrium"], "pelvis.cervix": ["cervix"], "pelvis.vagina": ["vagina"], "thorax.breast": ["breast"]}
structures = [
 # shared
 s("head-neck.hypothalamus", "shared", "Hypothalamus — HPG top floor", "Kisspeptin + pulsatile GnRH: the ignition and metronome for both sexes.", ["FJ1760","FJ1808"], ["HRAF0338","HRAF0339"], ["kisspeptin","GnRH"], ["KISS1R","GnRHR"], [LH+"hpg-axis.md"]),
 s("head-neck.pituitary", "shared", "Pituitary — LH & FSH", "Same gonadotroph cells in both sexes; LH and FSH go to testes or ovaries. Female body: hotspot (no HRA pituitary mesh).", ["FJ1796"], [], ["LH","FSH","prolactin"], ["GnRHR"], [LH+"hpg-axis.md"]),
 s("abdomen.adrenal", "shared", "Adrenal — cortisol + adrenal androgens", "Minor androgen source in men; ~⅓ of circulating testosterone origin in women [18]. Female body: hotspot (no HRA adrenal mesh).", ["FJ3129","FJ3130"], [], ["cortisol","aldosterone","DHEA","DHEA-S"], ["MC2R"], [LH+"overview.md"]),
 s("pelvis.bladder", "shared", "Urinary bladder", "Same organ, different neighbours: prostate below (♂) or uterus on top (♀).", ["FJ3149"], ["HRAF0609","HRAF0610","HRAF0611","HRAF0612"], [], [], ["body-map/regions/pelvis.md"]),
 # male
 s("pelvis.testis", M, "Testis — sperm + testosterone factory", "Tubules make sperm; ~500 million Leydig cells make ~7 mg testosterone/day [18]; inside ≈100× blood level [17].", ["FJ3138","FJ3142"], [], ["testosterone","inhibin B","estradiol (small)"], ["LHCGR","FSHR","AR"], [LM+"testes.md", LH+"testosterone.md"], "pelvis.ovary"),
 s("pelvis.epididymis", M, "Epididymis — finishing school", "~6 m of coiled duct where sperm gain motility.", ["FJ3136","FJ3141"], [], [], ["AR"], [LM+"ducts.md"]),
 s("pelvis.vas-deferens", M, "Vas deferens — express pipe", "Scrotum → groin → over the ureter → prostate.", ["FJ3135","FJ3140"], [], [], ["ADRA1A"], [LM+"ducts.md"]),
 s("pelvis.seminal-vesicle", M, "Seminal vesicle — fuel tank", "Largest share of semen: fructose, prostaglandins, semenogelin.", ["FJ3137","FJ3143"], [], [], ["AR"], [LM+"accessory-glands.md"]),
 s("pelvis.prostate", M, "Prostate — DHT-driven gland", "PSA, citrate, zinc; grows under DHT from SRD5A2.", ["FJ3139"], [], ["DHT"], ["AR","SRD5A2"], [LM+"accessory-glands.md"], "pelvis.paraurethral"),
 s("pelvis.ejaculatory-duct", M, "Ejaculatory duct", "Vas + seminal-vesicle duct, tunnelling through the prostate.", hotspot=True, library=[LM+"ducts.md"]),
 s("pelvis.bulbourethral", M, "Bulbourethral (Cowper's) glands", "Pre-ejaculate mucus.", hotspot=True, library=[LM+"accessory-glands.md"], homolog="pelvis.vestibular-glands"),
 s("pelvis.penis", M, "Penis — erectile tissue", "2 corpora cavernosa + corpus spongiosum + glans; NO–cGMP erection.", ["FJ3132","FJ3133","FJ3134"], [], [], ["PDE5 (enzyme)"], [LM+"accessory-glands.md"], "pelvis.clitoris"),
 s("pelvis.urethra-male", M, "Male urethra — shared exit", "Urine and semen, never at once.", ["FJ3148"], [], [], [], [LM+"ducts.md"]),
 s("pelvis.scrotum", M, "Scrotum — cooling pouch", "Keeps testes a few °C below core.", hotspot=True, library=[LM+"testes.md"], homolog="pelvis.vulva"),
 s("pelvis.spermatic-cord", M, "Testicular vessels", "Artery from aorta; pampiniform plexus cools; left vein → left renal vein.", ["FJ3532","FJ3617","FJ3533","FJ3618"], [], [], [], [LM+"testes.md"]),
 # female
 s("pelvis.ovary", F, "Ovary — egg bank + hormone clock", "~12% of peak follicle pool left by 30 y, ~3% by 40 y [27]; each cycle one follicle makes estradiol, then progesterone.", [], ["HRAF0432","HRAF0433","HRAF0423","HRAF0424","HRAF0425","HRAF0426","HRAF0430","HRAF0431"], ["estradiol","progesterone","inhibin A/B","AMH","testosterone"], ["FSHR","LHCGR","ESR1","ESR2","PGR"], [LF+"ovaries.md", LH+"estrogen-progesterone.md"], "pelvis.testis"),
 s("pelvis.uterine-tube", F, "Uterine tube — catch & meet", "Fimbriae sweep the egg in; fertilization usually in the ampulla.", [], [f"HRAF0{n}" for n in range(408,416)] + ["HRAF0434","HRAF0428","HRAF0429"], [], ["ESR1","PGR"], [LF+"tracts.md"]),
 s("pelvis.uterus", F, "Uterus — self-rebuilding room", "Estradiol builds the lining, progesterone readies it, oxytocin contracts the muscle.", [], ["HRAF0435","HRAF0436","HRAF0437","HRAF0438","HRAF0439","HRAF0440","HRAF0427","HRAF0416","HRAF0417","HRAF0418","HRAF0419","HRAF0420","HRAF0421","HRAF0422","HRAF0629","HRAF0630","HRAF0631","HRAF0632"], ["estradiol","progesterone","oxytocin"], ["ESR1","PGR","OXTR"], [LF+"uterus.md", LF+"cycle.md"]),
 s("pelvis.cervix", F, "Cervix — gatekeeper", "Mucus thin near ovulation, thick under progesterone.", [], ["HRAF0441","HRAF0442","HRAF0443","HRAF0407"], [], ["ESR1","PGR"], [LF+"uterus.md"]),
 s("pelvis.vagina", F, "Vagina", "Fibromuscular canal; acidic, Lactobacillus-dominated.", [], ["HRAF0406"], [], ["ESR1"], [LF+"tracts.md"]),
 s("pelvis.vulva", F, "Vulva", "Mons, labia, vestibule.", hotspot=True, library=[LF+"tracts.md"], homolog="pelvis.scrotum"),
 s("pelvis.clitoris", F, "Clitoris", "Glans, body, crura, vestibular bulbs — erectile, NO-driven.", hotspot=True, library=[LF+"tracts.md"], homolog="pelvis.penis"),
 s("pelvis.vestibular-glands", F, "Greater vestibular (Bartholin) glands", "Lubricating mucus.", hotspot=True, library=[LF+"tracts.md"], homolog="pelvis.bulbourethral"),
 s("pelvis.paraurethral", F, "Paraurethral (Skene's) glands", "Small glands beside the urethra.", hotspot=True, library=[LF+"tracts.md"], homolog="pelvis.prostate"),
 s("thorax.breast", F, "Breast — mammary lobes", "Grown by estradiol + progesterone; milk by prolactin; let-down by oxytocin.", [], ["HRAF0008","HRAF0018"], ["estradiol","progesterone","prolactin","oxytocin"], ["ESR1","PGR","PRLR","OXTR"], [LF+"tracts.md"]),
]
for x in structures:
    x["receptor_overlay_ids"] = RX.get(x["id"], [])
out = {"version": 1, "theme": "whole-body", "description": "Dual-layer sex view: shared + male_layer + female_layer child structures. Docs: body-map/sex-layers.md.",
       "layers": {"shared": {"label": "Both bodies"}, "male_layer": {"label": "Male", "body": "BodyParts3D 4.0 (male)"}, "female_layer": {"label": "Female", "body": "HRA female v1.10"}},
       "aliases": {"male": "male_layer", "female": "female_layer", "both": "shared"},
       "cite_source": "sources/whole-body-overview-sources.md", "structures": structures}
p = pathlib.Path(__file__).resolve().parents[1] / "overlays" / "sex-layers.json"
p.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n"); print("wrote", p, len(structures))
