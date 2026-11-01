import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle, Rectangle, Polygon, Wedge
from PIL import Image
import os
OUT="/workspace/science-anatomy-biology/figures/bone-volume"
rng=np.random.default_rng(4)
INK="#2b2b2b"; CORT="#d9a441"; TRAB="#e9cf98"; MAR="#f6e7e1"; BLUE="#3b7dd8"; RED="#d8573b"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"text.color":INK,"axes.labelcolor":INK,"xtick.color":INK,"ytick.color":INK})
def save(fig,name):
    fig.savefig(os.path.join(OUT,name),transparent=True,dpi=200,bbox_inches="tight"); plt.close(fig)

# F1
fig,ax=plt.subplots(figsize=(9,7.5)); ax.set_xlim(0,10); ax.set_ylim(0,12); ax.axis("off")
cx=3.0
ax.add_patch(Rectangle((cx-0.75,2.6),1.5,6.8,fc=CORT,ec=INK,lw=1.5))
ax.add_patch(Rectangle((cx-0.38,3.2),0.76,5.6,fc=MAR,ec="none"))
for y0,s in [(9.4,1),(2.6,-1)]:
    ax.add_patch(Polygon([(cx-0.75,y0),(cx+0.75,y0),(cx+1.25,y0+0.9*s),(cx-1.25,y0+0.9*s)],fc=TRAB,ec=INK,lw=1.5))
ax.add_patch(Ellipse((cx,10.85),2.7,1.4,fc=TRAB,ec=INK,lw=1.5))
ax.add_patch(Ellipse((cx,1.15),2.7,1.4,fc=TRAB,ec=INK,lw=1.5))
for (yc,h) in [(10.85,1.1),(1.15,1.1),(9.85,0.8),(2.15,0.8)]:
    for _ in range(70):
        x=cx+rng.uniform(-1.05,1.05); y=yc+rng.uniform(-h/2,h/2)
        ax.plot([x,x+rng.uniform(-.15,.15)],[y,y+rng.uniform(-.15,.15)],color="#a8813a",lw=0.8)
for y in (10.25,1.75): ax.plot([cx-1.2,cx+1.2],[y,y],ls=(0,(3,2)),color=INK,lw=1)
def brk(y0,y1,txt,x=1.0):
    ax.plot([x,x-0.15,x-0.15,x],[y0,y0,y1,y1],color=INK,lw=1.3); ax.text(x-0.3,(y0+y1)/2,txt,ha="right",va="center",fontsize=12,weight="bold")
brk(8.6,11.6,"Proximal"); brk(3.6,8.4,"Midshaft"); brk(0.4,3.4,"Distal")
def lab(y,txt,xt=4.9,xa=cx+1.3):
    ax.annotate(txt,(xa,y),(xt,y),va="center",fontsize=11,arrowprops=dict(arrowstyle="-",color=INK,lw=0.8))
lab(10.85,"Epiphysis  (end: spongy core, thin shell)")
lab(9.85,"Metaphysis  (flare: spongy-rich)",xa=cx+1.0)
lab(7.0,"Diaphysis  (shaft: thick cortical tube\n+ marrow cavity)",xa=cx+0.8)
ax.text(4.9,6.0,"dashed line = growth plate\n(closes in adults)",fontsize=9.5,va="center")
for i,(c,t) in enumerate([(CORT,"Cortical (compact) bone"),(TRAB,"Trabecular (spongy) bone"),(MAR,"Marrow cavity")]):
    ax.add_patch(Rectangle((5.0,4.9-i*0.55),0.4,0.35,fc=c,ec=INK)); ax.text(5.55,5.07-i*0.55,t,va="center",fontsize=10.5)
ax.text(5.0,1.6,"Cortical : trabecular, by site (Clarke 2008)\n• Radial diaphysis  95 : 5\n• Femoral head        50 : 50\n• Vertebra              25 : 75\n• Whole skeleton     80 : 20",fontsize=10.5,va="center",
        bbox=dict(boxstyle="round,pad=0.4",fc="white",ec=INK,alpha=0.85))
ax.text(0,12.0,"One bone, many rooms: where the volume lives",fontsize=14,weight="bold")
save(fig,"bone-volume-sector-map.png")

# F2
fig,axs=plt.subplots(1,2,figsize=(10,5.6))
for a in axs: a.set_xlim(-1.4,1.4); a.set_ylim(-1.6,1.4); a.set_aspect("equal"); a.axis("off")
a=axs[0]
a.add_patch(Circle((0,0),1.0,fc=CORT,ec=INK,lw=1.5)); a.add_patch(Circle((0.04,0.02),0.55,fc=MAR,ec=INK,lw=1))
a.set_title("Midshaft slice (diaphysis)",fontsize=12,weight="bold")
a.text(0,-1.3,"Thick cortical ring = most of the bone volume\nHollow middle = marrow (not counted as BV)",ha="center",fontsize=10)
a.annotate("periosteal\n(outer) surface",(0.71,0.71),(1.05,1.15),fontsize=9,arrowprops=dict(arrowstyle="-",lw=.8))
a.annotate("endosteal\n(inner) surface",(-0.4,-0.38),(-1.4,-0.95),fontsize=9,arrowprops=dict(arrowstyle="-",lw=.8))
a=axs[1]
a.add_patch(Circle((0,0),1.1,fc=MAR,ec=INK,lw=1.5))
a.add_patch(Wedge((0,0),1.1,0,360,width=0.07,fc=CORT,ec=INK,lw=1.2))
for _ in range(260):
    r=np.sqrt(rng.uniform(0,1))*0.98; t=rng.uniform(0,2*np.pi); x,y=r*np.cos(t),r*np.sin(t)
    ang=rng.uniform(0,np.pi); L=rng.uniform(.06,.16)
    a.plot([x,x+L*np.cos(ang)],[y,y+L*np.sin(ang)],color="#a8813a",lw=1.4,solid_capstyle="round")
a.set_title("Near-joint slice (metaphysis / vertebra)",fontsize=12,weight="bold")
a.text(0,-1.45,"Thin shell + trabecular lattice\nBV/TV = bone volume ÷ total volume of the box\n(e.g. vertebral shell ≈ 0.38 mm; Eswaran 2006)",ha="center",fontsize=10)
fig.suptitle("Two compartments, two kinds of volume",fontsize=14,weight="bold",y=1.0)
save(fig,"bone-volume-cortical-trabecular.png")

# F3
fig,axs=plt.subplots(1,2,figsize=(11,5.4),gridspec_kw=dict(width_ratios=[1.25,1]))
a=axs[0]
labels=["Humerus\nshaft","Radius\nshaft","Femur\nshaft","Tibia\nshaft"]
vals=[2.98,2.21,-0.49,-0.78]
cols=[BLUE if v>0 else RED for v in vals]
a.barh(labels[::-1],vals[::-1],color=cols[::-1],edgecolor=INK)
a.axvline(0,color=INK,lw=1)
for i,v in enumerate(vals[::-1]): a.text(v+(0.12 if v>0 else -0.12),i,f"{v:+.2f}%",va="center",ha="left" if v>0 else "right",fontsize=10.5)
a.set_xlim(-2,4.2); a.set_xlabel("Median directional asymmetry, (R−L)/mean × 100")
a.set_title("Everyday people: arms lean right,\nlegs lean slightly left",fontsize=12,weight="bold")
a.text(0,-0.2,"Midshaft breadth, 780 adult skeletons (Auerbach & Ruff 2006)",fontsize=8.5,transform=a.transAxes,va="top")
for s in ["top","right"]: a.spines[s].set_visible(False)
a=axs[1]
items=[("Bone mineral content",14,27),("Total area (size)",16,21),("Cortical area",12,32),("Cortical thickness*",5,25),("Volumetric density",-2,0.6)]
for i,(t,lo,hi) in enumerate(items[::-1]):
    a.plot([lo,hi],[i,i],color=BLUE if t!="Volumetric density" else "#888",lw=9,solid_capstyle="butt")
    a.text(hi+1,i,("≈ 0 (one site: −2%)" if t=="Volumetric density" else f"{lo}–{hi}%"),va="center",fontsize=10)
a.set_yticks(range(len(items))); a.set_yticklabels([t for t,_,_ in items[::-1]])
a.axvline(0,color=INK,lw=1); a.set_xlim(-5,42)
a.set_xlabel("Playing arm vs other arm (%)")
a.set_title("Tennis players: the extra is\nmostly SIZE, not density",fontsize=12,weight="bold")
a.text(0,-0.2,"pQCT, humerus + radius sites, 12 men (Haapasalo et al. 2000)\n*significant at humeral & radial shafts and distal humerus",fontsize=8.5,va="top",transform=a.transAxes)
for s in ["top","right"]: a.spines[s].set_visible(False)
fig.tight_layout()
save(fig,"bone-volume-left-right.png")

# F4 GIF
frames=[]; N=24
for k in range(N*2):
    t=k/N if k<N else (2*N-k)/N
    fig,ax=plt.subplots(figsize=(4.6,4.6),dpi=90); ax.set_xlim(-1.5,1.5); ax.set_ylim(-1.7,1.5); ax.set_aspect("equal"); ax.axis("off")
    fig.patch.set_facecolor("white")
    Ro=1.0+0.15*t; Ri=0.55+0.33*t
    ax.add_patch(Circle((0,0),Ro,fc=CORT,ec=INK,lw=1.5)); ax.add_patch(Circle((0,0),Ri,fc=MAR,ec=INK,lw=1))
    ax.add_patch(Circle((0,0),1.0,fill=False,ec=INK,ls=":",lw=1)); ax.add_patch(Circle((0,0),0.55,fill=False,ec=INK,ls=":",lw=1))
    if t>0.15:
        ax.annotate("",(Ro+0.02,0),(1.0,0),arrowprops=dict(arrowstyle="->",color=BLUE,lw=2))
        ax.annotate("",(-Ri,0),(-0.55,0),arrowprops=dict(arrowstyle="->",color=RED,lw=2))
    ax.text(0,1.33,"Outer (periosteal) grows out",ha="center",color=BLUE,fontsize=10,weight="bold")
    ax.text(0,-1.33,"Inner (endosteal) hollows out",ha="center",color=RED,fontsize=10,weight="bold")
    ax.text(0,-1.6,"Wider tube, thinner wall (schematic, not to scale)",ha="center",fontsize=8)
    fig.canvas.draw(); im=Image.frombuffer("RGBA",fig.canvas.get_width_height(),fig.canvas.buffer_rgba()).convert("RGB"); plt.close(fig)
    frames.append(im)
frames[0].save(os.path.join(OUT,"bone-volume-envelopes.gif"),save_all=True,append_images=frames[1:],duration=80,loop=0)
