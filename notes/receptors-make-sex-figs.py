# Run from figures/receptors/:  python3 ../../notes/receptors-make-sex-figs.py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, RegularPolygon
INK="#2b2d42"; OXT="#e76f51"; REC="#2a9d8f"; GQ="#e9c46a"; CA="#264653"; SOFT="#8d99ae"; MAUVE="#b5838d"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK})
def save(fig,name):
    fig.savefig(name,transparent=True,dpi=200,bbox_inches="tight",pad_inches=0.15); plt.close(fig)
def arrow(ax,a,b,c=INK,lw=2,rad=0.0,ls="-"):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,lw=lw,color=c,linestyle=ls,connectionstyle=f"arc3,rad={rad}"))
def box(ax,x,y,w,h,c,a=0.18):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.15",fc=c,ec=c,alpha=a,lw=0))
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.15",fc="none",ec=c,lw=2))

# ---- 1. sex-steroid cast
cards=[("AR","NR3C4 · gene on X","testosterone, DHT","nuclear",
        "♂ Sertoli, Leydig, prostate,\n   seminal vesicle, penis\n♀ theca, uterus, breast\n◎ muscle, bone, brain","Same lock in all;\nmore key in males"),
       ("ERα","ESR1 · NR3A1","estradiol","nuclear",
        "♀ uterus, cervix, vagina,\n   breast ducts\n♂ efferent ducts\n◎ hypothalamus, bone","Builds tissue;\ncloses growth plates"),
       ("ERβ","ESR2 · NR3A2","estradiol","nuclear",
        "♀ granulosa cells\n♂ prostate lining\n◎ brain, other tissues","Found 1996;\nfine-tunes ERα"),
       ("GPER1","old name GPR30","estradiol","gpcr",
        "◎ reproductive tract,\n   brain, vessels,\n   immune cells","Fast: Ca²⁺ + PIP₃\nin seconds"),
       ("PR","PGR · PR-A / PR-B","progesterone","nuclear",
        "♀ uterus (A), ovary (A),\n   breast (B), cervix\n◎ brain","Made on ERα's\norder: 'get ready'")]
fig,ax=plt.subplots(figsize=(14,6.2)); ax.set_xlim(0,14); ax.set_ylim(0,6.2); ax.axis("off")
ax.text(7,5.95,"Same locks, different keys — the sex-steroid receptor cast",ha="center",fontsize=16,weight="bold")
for i,(n,code,lig,kind,where,why) in enumerate(cards):
    x=0.2+i*2.78; c=REC if kind=="nuclear" else GQ
    box(ax,x,0.35,2.55,5.1,c)
    if kind=="nuclear": ax.add_patch(Circle((x+0.35,5.05),0.17,color=c))
    else: ax.add_patch(RegularPolygon((x+0.35,5.05),4,radius=0.22,color=c))
    ax.text(x+0.65,5.05,n,fontsize=18,weight="bold",va="center")
    ax.text(x+0.15,4.55,code,fontsize=9,color=SOFT)
    ax.text(x+0.15,4.15,"key: "+lig,fontsize=10,color=OXT,weight="bold")
    ax.text(x+0.15,3.75,"nuclear · slow (hours)" if kind=="nuclear" else "membrane GPCR · fast",fontsize=9,color=CA)
    ax.text(x+0.15,3.45,where,fontsize=9.5,va="top",linespacing=1.35)
    ax.text(x+1.275,0.75,why,fontsize=9.5,ha="center",va="center",style="italic",color=MAUVE)
ax.add_patch(Circle((0.4,0.05),0.1,color=REC)); ax.text(0.6,0.05,"nuclear receptor (binds DNA, switches genes)",fontsize=9,va="center")
ax.add_patch(RegularPolygon((5.6,0.05),4,radius=0.13,color=GQ)); ax.text(5.8,0.05,"GPCR (fast signal)",fontsize=9,va="center")
ax.text(8.2,0.05,"♂ male   ♀ female   ◎ both sexes",fontsize=9,va="center")
save(fig,"receptors-sex-steroid-cast.png")

# ---- 2. HPG axis
fig,ax=plt.subplots(figsize=(12,8)); ax.set_xlim(0,12); ax.set_ylim(0,8); ax.axis("off")
ax.text(6,7.75,"The HPG axis — a chain of receptors",ha="center",fontsize=16,weight="bold")
def node(x,y,w,h,title,sub,c):
    box(ax,x,y,w,h,c); ax.text(x+w/2,y+h-0.3,title,ha="center",fontsize=12,weight="bold"); ax.text(x+w/2,y+0.35,sub,ha="center",fontsize=9.5,va="bottom")
node(3.5,6.0,5,1.35,"Hypothalamus","kisspeptin → KISS1R ◆ on GnRH neurons\n→ GnRH in pulses",MAUVE)
node(3.5,4.0,5,1.35,"Anterior pituitary","GnRH → GNRHR ◆ (Gq → Ca²⁺) on gonadotropes\n→ releases LH + FSH",GQ)
arrow(ax,(6,6.0),(6,5.4)); ax.text(6.1,5.65,"GnRH pulses",fontsize=9,color=SOFT)
# testis
node(0.2,0.6,5.3,2.6,"Testis ♂","",REC)
ax.text(0.45,2.45,"Leydig cell",fontsize=10.5,weight="bold"); ax.text(0.45,1.95,"LH → LHCGR ◆ (Gs → cAMP)\n→ cholesterol → testosterone",fontsize=9,va="top")
ax.text(3.0,2.45,"Sertoli cell",fontsize=10.5,weight="bold"); ax.text(3.0,1.95,"FSH → FSHR ◆\n+ testosterone → AR ●\n→ sperm making",fontsize=9,va="top")
arrow(ax,(2.55,1.2),(2.95,1.2),OXT); ax.text(1.4,0.8,"testosterone",fontsize=9,color=OXT)
# ovary
node(6.5,0.6,5.3,2.6,"Ovary ♀","",REC)
ax.text(6.75,2.45,"Theca cell",fontsize=10.5,weight="bold"); ax.text(6.75,1.95,"LH → LHCGR ◆\n→ androgens",fontsize=9,va="top")
ax.text(9.3,2.45,"Granulosa cell",fontsize=10.5,weight="bold"); ax.text(9.3,1.95,"FSH → FSHR ◆\n→ aromatase on\n→ estradiol",fontsize=9,va="top")
arrow(ax,(8.6,1.2),(9.2,1.2),OXT); ax.text(7.7,0.8,"androgens",fontsize=9,color=OXT)
# LH/FSH down
arrow(ax,(4.6,4.0),(2.9,3.25),INK); arrow(ax,(7.4,4.0),(9.1,3.25),INK)
ax.text(2.6,3.65,"LH + FSH",fontsize=10,weight="bold"); ax.text(8.6,3.65,"LH + FSH",fontsize=10,weight="bold")
# feedback
arrow(ax,(0.4,3.25),(3.45,6.6),CA,lw=1.8,rad=-0.35,ls="--"); arrow(ax,(11.6,3.25),(8.55,6.6),CA,lw=1.8,rad=0.35,ls="--")
ax.text(0.15,5.3,"feedback:\ntestosterone,\nestradiol on\nAR ● / ERα ●\nslow the drum",fontsize=9,color=CA)
ax.text(10.1,5.3,"mid-cycle:\nhigh estradiol\nbriefly boosts\nthe drum → LH\nsurge",fontsize=9,color=CA)
ax.text(6,0.15,"◆ GPCR (fast)   ● nuclear receptor (slow)   ·   pulses drive the axis; a constant flood shuts it down",ha="center",fontsize=9,color=SOFT)
save(fig,"receptors-hpg-axis.png")
