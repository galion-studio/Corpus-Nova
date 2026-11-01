"""Fig 5 for white paper 01: the sex-steroid pathway (one shared assembly line).
Run from figures/biology-chemistry/:  python3 src/make_steroid_figure.py"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
INK="#1f2a44"; GREY="#8a94a6"; ATP="#e8a317"
MALE="#2f7fc1"; FEMALE="#c2477a"; BOTH="#3a9d5d"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"text.color":INK})
fig,ax=plt.subplots(figsize=(15,9)); ax.set_xlim(0,15.9); ax.set_ylim(0.2,10.4); ax.axis("off")
W,H=2.5,0.95
def node(x,y,t,fc,ec=INK,fs=12):
    ax.add_patch(FancyBboxPatch((x-W/2,y-H/2),W,H,boxstyle="round,pad=0,rounding_size=0.18",fc=fc,ec=ec,lw=2.2))
    ax.text(x,y,t,ha="center",va="center",fontsize=fs,fontweight="bold")
def step(a,b,label,c=INK,off=(0,0),fs=10,ha="center"):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=18,color=c,lw=2.2))
    mx,my=(a[0]+b[0])/2+off[0],(a[1]+b[1])/2+off[1]
    ax.text(mx,my,label,ha=ha,va="center",fontsize=fs,color=c,style="italic")
P={"chol":(1.6,9.3),"preg":(1.6,7.0),"prog":(1.6,4.7),"ohp":(5.2,7.0),"dhea":(8.8,7.0),
   "a4":(8.8,4.7),"T":(13.0,4.7),"E1":(8.8,2.2),"E2":(13.0,2.2),"DHT":(13.0,7.0)}
node(*P["chol"],"Cholesterol","#eeeeee")
node(*P["preg"],"Pregnenolone","#fbe7b0")
node(*P["prog"],"Progesterone","#f6d3e2",FEMALE)
node(*P["ohp"],"17-OH-\npregnenolone","#fbe7b0",fs=11)
node(*P["dhea"],"DHEA","#fbe7b0")
node(*P["a4"],"Androstenedione","#fbe7b0",fs=11)
node(*P["T"],"Testosterone","#d4e6f5",MALE)
node(*P["DHT"],"DHT","#d4e6f5",MALE)
node(*P["E1"],"Estrone","#f6d3e2",FEMALE)
node(*P["E2"],"Estradiol","#f6d3e2",FEMALE)
h=H/2
step((1.6,9.3-h),(1.6,7.0+h),"  StAR carries it into\n  mitochondria; CYP11A1\n  cuts the side chain\n  = THE GATE (LH-driven)",ATP,off=(0.05,0),ha="left",fs=10.5)
step((1.6,7.0-h),(1.6,4.7+h),"  3β-HSD2",BOTH,ha="left")
step((1.6+W/2,7.0),(5.2-W/2,7.0),"CYP17A1\n17α-hydroxylase",BOTH,off=(0,-0.75))
step((5.2+W/2,7.0),(8.8-W/2,7.0),"CYP17A1\n17,20-lyase",BOTH,off=(0,-0.75))
step((8.8,7.0-h),(8.8,4.7+h),"  3β-HSD2",BOTH,ha="left")
step((8.8+W/2,4.7),(13.0-W/2,4.7),"17β-HSD3 (testis)\nAKR1C3 (elsewhere)",MALE,off=(0,0.8),fs=9.5)
step((13.0,4.7+h),(13.0,7.0-h),"  5α-reductase\n  (skin, prostate)\n  ~2–10× stronger",MALE,ha="left")
step((8.8,4.7-h),(8.8,2.2+h),"  aromatase\n  (CYP19A1)",FEMALE,ha="left")
step((13.0,4.7-h),(13.0,2.2+h),"  aromatase\n  (CYP19A1)",FEMALE,ha="left")
step((8.8+W/2,2.2),(13.0-W/2,2.2),"17β-HSD1\n(granulosa)",FEMALE,off=(0,-0.75))
ax.text(1.6,3.85,"corpus luteum stops here\n(~25 mg/day mid-luteal)",ha="center",va="top",fontsize=10,color=FEMALE)
ax.text(14.35,4.1,"testes:\n~5–7 mg/day\n(men)",ha="left",va="center",fontsize=10,color=MALE)
ax.text(5.6,9.8,"One assembly line, two sexes, different dial settings",fontsize=15,fontweight="bold")
ax.text(5.6,9.25,"Same enzymes in testis and ovary — which steps are switched on decides the output.",fontsize=11,color=GREY)
ax.text(0.2,0.55,"●  both sexes / shared steps",color=BOTH,fontsize=11,fontweight="bold")
ax.text(4.4,0.55,"●  androgen end (Leydig cells dominate)",color=MALE,fontsize=11,fontweight="bold")
ax.text(10.4,0.55,"●  estrogen / progestin end (ovary dominates)",color=FEMALE,fontsize=11,fontweight="bold")
fig.savefig("biology-chemistry-steroid-pathway.png",transparent=True,dpi=200,bbox_inches="tight")
