import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Ellipse
import numpy as np
INK="#2b2d42"; OXT="#e76f51"; REC="#2a9d8f"; GQ="#e9c46a"; CA="#264653"; SOFT="#8d99ae"
plt.rcParams.update({"font.family":"DejaVu Sans","text.color":INK})

def save(fig,name):
    fig.savefig(name,transparent=True,dpi=200,bbox_inches="tight",pad_inches=0.15); plt.close(fig)

def arrow(ax,a,b,c=INK,lw=2,rad=0.0):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=16,lw=lw,color=c,connectionstyle=f"arc3,rad={rad}"))

# 1 membrane knock
fig,ax=plt.subplots(figsize=(10,4.6)); ax.set_xlim(0,10); ax.set_ylim(-0.2,4.6); ax.axis("off")
# membrane band
for x in np.arange(0,10.01,0.25):
    ax.add_patch(Circle((x,2.55),0.09,color=SOFT,alpha=.6)); ax.add_patch(Circle((x,2.05),0.09,color=SOFT,alpha=.6))
ax.text(0.05,2.3,"cell membrane",fontsize=9,color=SOFT,va="center")
ax.text(0.05,4.3,"OUTSIDE",fontsize=9,color=SOFT); ax.text(0.05,0.15,"INSIDE",fontsize=9,color=SOFT)
for i,(x,t,s) in enumerate([(1.9,"1  Knock","a messenger (ligand)\narrives: oxytocin"),(5.0,"2  Answer","the receptor (OXTR)\nchanges shape"),(8.1,"3  Cascade","Gq → PLC → IP₃ → Ca²⁺\nthe cell 'hears' it")]):
    ax.text(x,4.35,t,fontsize=14,weight="bold",ha="center")
    # receptor as 7 loops
    for k in range(7):
        ax.add_patch(FancyBboxPatch((x-0.62+k*0.18,1.85),0.1,0.9,boxstyle="round,pad=0.02,rounding_size=0.05",color=REC,alpha=0.95 if i>0 else 0.55))
    ax.text(x,0.35,s,fontsize=10,ha="center",va="center")
# ligand states
ax.add_patch(Circle((1.9,3.55),0.22,color=OXT)); arrow(ax,(1.9,3.3),(1.9,2.85),OXT)
ax.add_patch(Circle((5.0,2.95),0.22,color=OXT))
ax.add_patch(Circle((8.1,2.95),0.22,color=OXT))
ax.add_patch(Ellipse((5.0,1.45),0.8,0.35,color=GQ)); ax.text(5.0,1.45,"Gq",ha="center",va="center",fontsize=10,weight="bold")
ax.add_patch(Ellipse((8.1,1.45),0.8,0.35,color=GQ)); ax.text(8.1,1.45,"Gq",ha="center",va="center",fontsize=10,weight="bold")
for dx,dy in [(-.6,-.2),(.6,-.15),(-.4,-.5),(.45,-.55),(0,-.35)]:
    ax.add_patch(Circle((8.1+dx*0.9,1.2+dy*0.45),0.06,color=CA))
ax.text(8.95,1.1,"Ca²⁺",fontsize=10,color=CA,weight="bold")
arrow(ax,(2.8,3.6),(4.1,3.6),SOFT); arrow(ax,(5.9,3.6),(7.2,3.6),SOFT)
save(fig,"receptors-membrane-knock.png")

# 2 cast card
cast=[("OXTR","oxytocin receptor","hears: oxytocin","talks via: Gq (mainly)","job: care, bonding,\nsocial salience",OXT),
      ("AVPR1A","vasopressin receptor 1A","hears: vasopressin","talks via: Gq","job: social recognition,\npartner preference",REC),
      ("MOR","µ-opioid receptor","hears: endorphins,\nenkephalins","talks via: Gi/o","job: warmth of contact,\nsting of separation",CA),
      ("D2","dopamine D2 receptor","hears: dopamine","talks via: Gi/o","job: 'do that again'\nfor social cues","#b5838d")]
fig,ax=plt.subplots(figsize=(11,4.4)); ax.set_xlim(0,11); ax.set_ylim(0,4.4); ax.axis("off")
for i,(n,p,h,g,j,c) in enumerate(cast):
    x=0.2+i*2.72
    ax.add_patch(FancyBboxPatch((x,0.15),2.45,4.05,boxstyle="round,pad=0.02,rounding_size=0.2",fc="none",ec=c,lw=2.5))
    # icon: receptor glyph
    for k in range(7): ax.add_patch(FancyBboxPatch((x+0.62+k*0.17,3.25),0.09,0.65,boxstyle="round,pad=0.01,rounding_size=0.04",color=c))
    ax.text(x+1.22,2.85,n,ha="center",fontsize=16,weight="bold",color=c)
    ax.text(x+1.22,2.55,p,ha="center",fontsize=9,style="italic")
    ax.text(x+1.22,2.05,h,ha="center",va="top",fontsize=9.5)
    ax.text(x+1.22,1.45,g,ha="center",va="top",fontsize=9.5)
    ax.text(x+1.22,1.0,j,ha="center",va="top",fontsize=9.5,weight="bold")
save(fig,"receptors-affiliation-cast.png")

# 3 social circuits
fig,ax=plt.subplots(figsize=(10,6.8)); ax.set_xlim(0,10); ax.set_ylim(-0.6,6.2); ax.set_aspect("equal"); ax.axis("off")
nodes={"PVN":(5,1.0,"PVN (hypothalamus)\nmakes oxytocin + vasopressin",OXT),
       "VTA":(2.0,2.4,"VTA\ndopamine source","#b5838d"),
       "NAcc":(2.2,4.4,"NAcc\nsocial reward","#b5838d"),
       "AMY":(7.8,2.6,"Amygdala\nsocial salience",REC),
       "PFC":(5,4.9,"PFC\ncontext & choice",CA),
       "VP":(7.9,4.6,"Ventral pallidum\npair-bond node (voles)",REC)}
for k,(x,y,l,c) in nodes.items():
    ax.add_patch(Circle((x,y),0.42,fc="none",ec=c,lw=2.5)); ax.text(x,y,k,ha="center",va="center",fontsize=11,weight="bold",color=c)
    ax.text(x,y-0.62,l.split("\n")[1],ha="center",va="top",fontsize=8.5,color=INK)
tags={"PVN":"","VTA":"OXTR","NAcc":"OXTR · D2 · MOR","AMY":"OXTR · AVPR1A","PFC":"OXTR · D2 · 5-HT2A/1A","VP":"AVPR1A · MOR"}
for k,t in tags.items():
    x,y,_,c=nodes[k]
    if t: ax.text(x,y+0.52,t,ha="center",fontsize=9,color=INK,bbox=dict(boxstyle="round,pad=0.25",fc="none",ec=SOFT,lw=1))
def link(a,b,c,rad=0.0,ls="-"):
    (x1,y1,_,_),(x2,y2,_,_)=nodes[a],nodes[b]
    v=np.array([x2-x1,y2-y1]); v=v/np.linalg.norm(v)*0.48
    p=FancyArrowPatch((x1+v[0],y1+v[1]),(x2-v[0],y2-v[1]),arrowstyle="-|>",mutation_scale=14,lw=1.8,color=c,linestyle=ls,connectionstyle=f"arc3,rad={rad}")
    ax.add_patch(p)
for t in ["VTA","NAcc","AMY","PFC","VP"]: link("PVN",t,OXT,0.1)
link("VTA","NAcc","#b5838d",-0.2)
ax.text(0.1,-0.5,"orange = oxytocin/vasopressin signaling from PVN (simplified)   ·   mauve = dopamine path",fontsize=8.5,color=SOFT)
ax.text(5,6.05,"A sparse map, not an atlas",ha="center",fontsize=12,weight="bold")
save(fig,"receptors-social-circuits.png")

# 4 GIF
from PIL import Image
frames=[]
for f in range(16):
    fig,ax=plt.subplots(figsize=(4,3)); ax.set_xlim(0,4); ax.set_ylim(0,3); ax.axis("off")
    ax.axhspan(1.4,1.7,color=SOFT,alpha=.35)
    for k in range(7): ax.add_patch(FancyBboxPatch((1.4+k*0.17,1.2),0.09,0.7,boxstyle="round,pad=0.01,rounding_size=0.04",color=REC))
    yl=2.8-min(f,6)*0.14
    ax.add_patch(Circle((2.0,yl),0.15,color=OXT))
    if f>=6: ax.add_patch(Ellipse((2.0,0.95),0.6,0.25,color=GQ,alpha=1 if f%2==0 else .6)); ax.text(2,0.95,"Gq",ha="center",va="center",fontsize=8,weight="bold")
    if f>=9:
        r=(f-8)*0.12
        for a in np.linspace(0,2*np.pi,8,endpoint=False): ax.add_patch(Circle((2+r*2*np.cos(a),0.55+r*np.sin(a)*0.6),0.05,color=CA))
        ax.text(3.2,0.3,"Ca²⁺",fontsize=9,color=CA,weight="bold")
    ax.text(0.1,2.75,["knock","knock","knock","knock","knock","knock","answer","answer","answer","cascade"][min(f,9)],fontsize=11,weight="bold",color=INK)
    fig.savefig("/tmp/f.png",dpi=90,transparent=True); plt.close(fig)
    frames.append(Image.open("/tmp/f.png").convert("RGBA"))
pal=[]
out=[]
for im in frames:
    alpha=im.split()[3]
    p=im.convert("RGB").convert("P",palette=Image.ADAPTIVE,colors=255)
    mask=Image.eval(alpha,lambda a:255 if a<=128 else 0)
    p.paste(255,mask); out.append(p)
out[0].save("receptors-oxtr-path.gif",save_all=True,append_images=out[1:],duration=180,loop=0,transparency=255,disposal=2)
