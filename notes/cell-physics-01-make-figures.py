"""Generates the two Cell Physics paper-01 figures (transparent PNG).
Run from repo root:  python3 notes/cell-physics-01-make-figures.py"""
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch
OUT=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","cell-physics")
rng=np.random.default_rng(11)
INK="#2b2d42"; C=["#ef8354","#4f9da6","#f4c95d","#9b5de5","#8ac926"]

# ---- Figure A: crowding scale ----
fig,axs=plt.subplots(1,2,figsize=(10,5.2))
def panel(ax,title,n,seed):
    r=np.random.default_rng(seed)
    ax.set_xlim(0,100);ax.set_ylim(0,100);ax.set_aspect("equal");ax.axis("off")
    ax.add_patch(FancyBboxPatch((1,1),98,98,boxstyle="round,pad=0,rounding_size=6",fill=False,lw=2.2,ec=INK))
    placed=[];tries=0
    while len(placed)<n and tries<20000:
        tries+=1
        rad=r.choice([2.5,3.5,4.5,6,8],p=[.3,.3,.2,.12,.08])
        x,y=r.uniform(4+rad,96-rad,2)
        if all((x-a)**2+(y-b)**2>(rad+c+0.6)**2 for a,b,c in placed) and (x-50)**2+(y-50)**2>(rad+3)**2:
            placed.append((x,y,rad))
    for x,y,rad in placed:
        col=C[r.integers(len(C))]
        ax.add_patch(Ellipse((x,y),2*rad*r.uniform(.85,1.15),2*rad*r.uniform(.85,1.15),angle=r.uniform(0,180),fc=col,ec=INK,lw=0.8,alpha=0.85))
    ax.add_patch(Circle((50,50),2.2,fc="white",ec="#d62828",lw=2.2,zorder=5))
    ax.set_title(title,color=INK,fontsize=14,fontweight="bold",pad=8)
panel(axs[0],"Dilute test tube",9,1)
panel(axs[1],"Crowded cytoplasm",400,2)
for ax in axs:
    ax.plot([8,28],[-6,-6],color=INK,lw=3,solid_capstyle="butt",clip_on=False)
    ax.text(18,-11,"~10 nm",ha="center",va="top",color=INK,fontsize=11,clip_on=False)
axs[0].text(34,-11,"macromolecules: well under 1% of volume",ha="left",va="top",fontsize=9.5,color=INK,clip_on=False)
axs[1].text(34,-11,"macromolecules: ~20–30% of volume",ha="left",va="top",fontsize=9.5,color=INK,clip_on=False)
fig.text(0.5,0.015,"○ red ring = a tracer protein (e.g. GFP, a few nm across). Blobs = proteins, ribosomes, RNA (soft, sticky, varied sizes). Schematic, not to exact scale.",ha="center",fontsize=8.5,color=INK)
plt.subplots_adjust(bottom=0.17,top=0.9,wspace=0.08)
fig.savefig(os.path.join(OUT,"cell-physics-crowding-scale.png"),dpi=200,transparent=True)
plt.close(fig)

# ---- Figure B: diffusion paths ----
N=3000
free=np.cumsum(rng.normal(0,1,(N,2)),axis=0)
pos=np.zeros(2);cage=np.zeros(2);tr=[];L=8.0
for i in range(N):
    step=rng.normal(0,1,2);new=pos+step
    if np.any(np.abs(new-cage)>L):
        if rng.random()<0.02:  # rare escape: hop to neighbouring cage
            d=np.sign(new-cage)*(np.abs(new-cage)>L);cage=cage+2*L*d
        else:
            new=pos-0.5*step
    pos=new;tr.append(pos.copy())
crowd=np.array(tr)
fig=plt.figure(figsize=(11,5.2))
ax1=fig.add_axes([0.02,0.12,0.3,0.75]);ax2=fig.add_axes([0.35,0.12,0.3,0.75]);ax3=fig.add_axes([0.73,0.2,0.24,0.6])
lim=max(np.abs(free).max(),np.abs(crowd).max())*1.08
for ax,path,col,t in [(ax1,free,"#4f9da6","Normal Brownian\n(open water)"),(ax2,crowd,"#ef8354","Anomalous / crowded\n(caged, then hops)")]:
    if path is crowd:
        for g in np.arange(-L-20*L,20*L,2*L):
            ax.axvline(g,color=INK,lw=0.5,alpha=0.25,ls=':');ax.axhline(g,color=INK,lw=0.5,alpha=0.25,ls=':')
    ax.plot(path[:,0],path[:,1],color=col,lw=0.8)
    ax.plot(*path[0],"o",color=INK,ms=6);ax.plot(*path[-1],"s",color=INK,ms=6)
    ax.set_xlim(-lim,lim);ax.set_ylim(-lim,lim);ax.set_aspect("equal");ax.axis("off")
    ax.set_title(t,color=INK,fontsize=13,fontweight="bold")
ax1.text(0,-lim*1.02,"● start   ■ end   (same number of steps)",ha="center",va="top",fontsize=9,color=INK)
ax2.text(0,-lim*1.02,"rattles inside a cage (dotted), now and then hops out",ha="center",va="top",fontsize=9,color=INK)
t=np.logspace(0,3,50)
ax3.loglog(t,t,color="#4f9da6",lw=2.5,label="MSD ∝ t  (α = 1)")
ax3.loglog(t,t**0.6,color="#ef8354",lw=2.5,label="MSD ∝ t^α  (α < 1)")
ax3.set_xlabel("time lag (log)",color=INK);ax3.set_ylabel("mean squared\ndisplacement (log)",color=INK)
ax3.set_xticks([]);ax3.set_yticks([]);ax3.minorticks_off()
for sp in ax3.spines.values(): sp.set_color(INK)
ax3.patch.set_alpha(0)
ax3.legend(frameon=False,fontsize=9,loc="upper left")
ax3.set_title("How spreading grows",color=INK,fontsize=12,fontweight="bold")
fig.text(0.5,0.02,"Simulated toy walks for illustration only (exponent 0.6 is an illustrative value, not a measurement).",ha="center",fontsize=8.5,color=INK)
fig.savefig(os.path.join(OUT,"cell-physics-diffusion-paths.png"),dpi=200,transparent=True)
plt.close(fig)
