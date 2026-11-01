"""Figures for white paper 01 (theme 1: biology & chemistry in vivo).
Run: python3 src/make_figures.py  (from figures/biology-chemistry/)"""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from PIL import Image, ImageDraw, ImageFont

INK="#1f2a44"; NA="#e0663a"; K="#2f7fc1"; ATP="#e8a317"; GREEN="#3a9d5d"; GREY="#8a94a6"
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"text.color":INK})

def box(ax,x,y,w,h,fc,ec=INK,lw=2,r=0.04,alpha=1):
    p=FancyBboxPatch((x,y),w,h,boxstyle=f"round,pad=0,rounding_size={r}",fc=fc,ec=ec,lw=lw,alpha=alpha)
    ax.add_patch(p); return p
def arrow(ax,a,b,c=INK,lw=2.2,rad=0.0,style="-|>",ms=18):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle=style,mutation_scale=ms,color=c,lw=lw,
                 connectionstyle=f"arc3,rad={rad}"))
def save(fig,name):
    fig.savefig(name,transparent=True,dpi=200,bbox_inches="tight"); plt.close(fig)

# ---------- 1. gradient, not equilibrium ----------
rng=np.random.default_rng(7)
fig,axs=plt.subplots(1,2,figsize=(11,5))
for ax in axs: ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis("off")
ax=axs[0]; ax.set_title("ALIVE: held apart (costs ATP)",color=GREEN,fontweight="bold")
box(ax,0.02,0.1,0.96,0.75,"none",lw=2)
ax.plot([0.5,0.5],[0.1,0.85],color=INK,lw=4)            # membrane
ax.text(0.26,0.88,"outside cell",ha="center",fontsize=11); ax.text(0.74,0.88,"inside cell",ha="center",fontsize=11)
n=lambda k:rng.uniform(size=(k,2))
xs,ys=n(40).T; ax.scatter(0.05+xs*0.42,0.14+ys*0.67,s=28,c=NA)
xs,ys=n(4).T;  ax.scatter(0.05+xs*0.42,0.14+ys*0.67,s=28,c=K)
xs,ys=n(4).T;  ax.scatter(0.53+xs*0.42,0.14+ys*0.67,s=28,c=NA)
xs,ys=n(40).T; ax.scatter(0.53+xs*0.42,0.14+ys*0.67,s=28,c=K)
ax.add_patch(Circle((0.5,0.47),0.06,fc=ATP,ec=INK,lw=2,zorder=5))
ax.text(0.5,0.47,"pump",ha="center",va="center",fontsize=9,zorder=6,fontweight="bold")
arrow(ax,(0.53,0.58),(0.40,0.70),NA); arrow(ax,(0.42,0.30),(0.58,0.22),K)
ax.text(0.5,0.02,"3 Na⁺ out · 2 K⁺ in · per ATP",ha="center",fontsize=11)
ax=axs[1]; ax.set_title("EQUILIBRIUM: all mixed, nothing to do",color=GREY,fontweight="bold")
box(ax,0.02,0.1,0.96,0.75,"none",ec=GREY,lw=2)
ax.plot([0.5,0.5],[0.1,0.85],color=GREY,lw=4,ls=(0,(3,2)))
for c in (NA,K):
    xs,ys=n(44).T; ax.scatter(0.05+xs*0.9,0.14+ys*0.67,s=28,c=c,alpha=0.55)
ax.text(0.5,0.02,"ΔG = 0 → no work, no signal, no life",ha="center",fontsize=11,color=GREY)
fig.text(0.31,-0.03,"● Na⁺",color=NA,fontsize=12,fontweight="bold"); fig.text(0.42,-0.03,"● K⁺",color=K,fontsize=12,fontweight="bold")
fig.text(0.51,-0.03,"● ATP-driven Na⁺/K⁺ pump",color=ATP,fontsize=12,fontweight="bold")
save(fig,"biology-chemistry-gradient-not-equilibrium.png")

# ---------- 2. ATP energy flow ----------
fig,ax=plt.subplots(figsize=(12,6)); ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis("off")
def node(x,y,w,h,t,fc,fs=12,bold=True):
    box(ax,x,y,w,h,fc,r=0.15); ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs,fontweight="bold" if bold else "normal")
node(0.2,3.9,2.2,1.3,"Food fuel\nglucose · fat ·\namino acids","#f6d7c3",11)
node(0.2,0.8,2.2,1.1,"O₂\nfrom lungs → blood","#d4e6f5",11)
node(3.3,4.2,2.6,1.1,"Glycolysis (cytosol)\nfast · ~2 ATP/glucose","#fbe7b0",11)
node(3.3,1.6,2.6,1.6,"Mitochondria\nO₂-dependent\n~30–32 ATP/glucose","#cfe8d6",11)
node(6.9,2.6,1.8,1.4,"ATP","#f5c242",20)
node(6.6,0.2,2.4,1.1,"Creatine phosphate\nfew-second buffer","#fbe7b0",11)
node(9.6,4.4,2.3,0.9,"Pumps (Na⁺/K⁺, Ca²⁺)","#eeeeee",11,False)
node(9.6,3.0,2.3,0.9,"Muscle contraction","#eeeeee",11,False)
node(9.6,1.45,2.3,1.05,"Building proteins,\nRNA, DNA","#eeeeee",11,False)
arrow(ax,(2.4,4.6),(3.3,4.75)); arrow(ax,(4.6,4.2),(4.6,3.2)); ax.text(4.7,3.7,"pyruvate",fontsize=10)
arrow(ax,(2.4,1.35),(3.3,2.0),K)
arrow(ax,(5.9,4.6),(6.95,3.9),ATP,ms=14); arrow(ax,(5.9,2.5),(6.9,3.0),ATP,lw=4,ms=24)

for y in (4.85,3.45,2.05): arrow(ax,(8.7,3.3),(9.6,y),ATP)
arrow(ax,(7.5,2.6),(7.5,1.3),INK,style="<|-|>",ms=14); ax.text(7.62,1.9,"creatine kinase",fontsize=10)
arrow(ax,(10.7,1.55),(8.2,2.65),GREY,rad=-0.35,lw=1.6); ax.text(9.1,0.95,"ADP + Pᵢ → recharge",fontsize=10,color=GREY)
ax.text(6,5.75,"You turn over roughly your body weight in ATP per day — from a pool of only a few mM",ha="center",fontsize=12,style="italic")
save(fig,"biology-chemistry-atp-energy-flow.png")

# ---------- 3. compartments ----------
fig,ax=plt.subplots(figsize=(11,6.4)); ax.set_xlim(0,11); ax.set_ylim(0,6.4); ax.axis("off")
ax.text(5.5,6.15,"Total body water ≈ 42 L (70 kg adult, ~60% of mass)",ha="center",fontsize=13,fontweight="bold")
box(ax,0.2,0.4,6.0,5.3,"#d4e6f5",r=0.3,alpha=0.85)   # ICF
ax.text(3.2,5.25,"INSIDE CELLS  ≈ 28 L  (⅔)",ha="center",fontsize=13,fontweight="bold")
for i,t in enumerate(["K⁺ ≈ 140 mM","Na⁺ ≈ 10–15 mM","free Ca²⁺ ≈ 0.0001 mM (100 nM)","pH ≈ 7.2","lots of protein & phosphate (−)"]):
    ax.text(0.6,4.5-0.62*i,t,fontsize=12)
box(ax,6.6,0.4,4.2,5.3,"#f6d7c3",r=0.3,alpha=0.85)    # ECF
ax.text(8.7,5.25,"OUTSIDE CELLS ≈ 14 L (⅓)",ha="center",fontsize=13,fontweight="bold")
box(ax,6.85,2.85,3.7,2.0,"#fbe7b0",r=0.2,alpha=0.9); ax.text(8.7,4.45,"between cells ≈ 10.5 L",ha="center",fontsize=11,fontweight="bold")
ax.text(7.05,3.6,"Na⁺ ≈ 140 mM · K⁺ ≈ 4 mM\nCl⁻ ≈ 110 · HCO₃⁻ ≈ 24 mM",fontsize=10.5)
box(ax,6.85,0.6,3.7,2.0,"#f3b8a8",r=0.2,alpha=0.9); ax.text(8.7,2.2,"blood plasma ≈ 3.5 L",ha="center",fontsize=11,fontweight="bold")
ax.text(7.05,0.85,"pH 7.35–7.45\nfree Ca²⁺ ≈ 1.2 mM\nglucose ≈ 5 mM",fontsize=10.5)
ax.plot([6.4,6.4],[0.4,5.7],color=INK,lw=5); ax.text(6.4,0.12,"cell membrane\n(oil film + pumps/channels)",ha="center",va="top",fontsize=10)
ax.plot([6.85,10.55],[2.72,2.72],color=INK,lw=2,ls=(0,(4,3))); ax.text(10.6,2.72," capillary\n wall",va="center",fontsize=9)
save(fig,"biology-chemistry-compartments.png")

# ---------- 4. buffer loop GIF (simple motion) ----------
W,H=760,360
try: F=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",22); f=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",16)
except Exception: F=f=ImageFont.load_default()
st=[(95,170,"CO₂ + H₂O"),(380,170,"H₂CO₃"),(665,170,"H⁺ + HCO₃⁻")]
frames=[]; N=36
for i in range(N):
    im=Image.new("RGBA",(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.text((W//2,22),"Bicarbonate buffer: a two-way street",fill=INK,font=F,anchor="mm")
    for x,y,t in st:
        d.rounded_rectangle((x-85,y-30,x+85,y+30),14,fill=(255,255,255,255),outline=INK,width=3)
        d.text((x,y),t,fill=INK,font=F,anchor="mm")
    for a,b in ((180,295),(465,580)):
        d.line((a,155,b,155),fill=INK,width=3); d.polygon([(b,155),(b-10,149),(b-10,161)],fill=INK)
        d.line((a,185,b,185),fill=INK,width=3); d.polygon([(a,185),(a+10,179),(a+10,191)],fill=INK)
    d.text((237,128),"carbonic",fill=GREY,font=f,anchor="mm"); d.text((237,212),"anhydrase",fill=GREY,font=f,anchor="mm")
    d.text((95,255),"lungs blow off CO₂\n(minutes)",fill=K,font=f,anchor="ma",align="center")
    d.text((665,255),"kidneys tune HCO₃⁻\n(hours–days)",fill=NA,font=f,anchor="ma",align="center")
    d.text((380,335),"pH = 6.1 + log([HCO₃⁻] / 0.03·pCO₂)  ≈ 6.1 + log 20 ≈ 7.4",fill=INK,font=f,anchor="mm")
    t=i/N; fwd=t<0.5; s=(t*2) if fwd else (t-0.5)*2
    x=180+s*(580-180) if fwd else 580-s*(580-180); y=155 if fwd else 185
    if 295<x<465: y=170-(1 if fwd else -1)*0  # pass through middle box
    col=(232,163,23,255)
    if not (290<x<470): d.ellipse((x-9,y-9,x+9,y+9),fill=col,outline=INK)
    frames.append(im)
# convert RGBA -> P with transparency
pal=[]
out=[]
for im in frames:
    alpha=im.split()[3]
    p=im.convert("RGB").quantize(colors=255,method=Image.Quantize.MEDIANCUT)
    mask=Image.eval(alpha,lambda a:255 if a<=40 else 0)
    p.paste(255,mask); out.append(p)
out[0].save("biology-chemistry-buffer-loop.gif",save_all=True,append_images=out[1:],duration=80,loop=0,transparency=255,disposal=2)
print("ok")
