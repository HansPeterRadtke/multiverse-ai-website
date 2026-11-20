#!/usr/bin/env python3
"""Create original Multiverse social artwork using the existing favicon geometry."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "brand"
OUT.mkdir(exist_ok=True, parents=True)
NAVY=(8,14,27); TEAL=(119,232,218); WHITE=(241,249,252); MUTED=(165,191,203)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def face(size, bold=False):
    path = BOLD if bold else FONT
    if not Path(path).is_file():
        raise FileNotFoundError("Install DejaVu Sans before regenerating brand assets")
    return ImageFont.truetype(path, size)

def bg(size):
    w,h=size; image=Image.new("RGB",size,NAVY); pix=image.load()
    for y in range(h):
        for x in range(w):
            glow=max(0,1-math.hypot((x/w-.89)*1.30,(y/h-.24)*1.25)/.92)
            ink=max(0,1-math.hypot((x/w-.12)*1.6,(y/h-1.08)*1.45)/1.0)
            pix[x,y]=(int(8+10*glow+4*ink),int(14+32*glow+11*ink),int(27+40*glow+16*ink))
    return image

def monogram(draw, box, color=TEAL):
    x,y,side=box;scale=side/64
    point=lambda px,py:(round(x+px*scale),round(y+py*scale))
    points=[point(*p) for p in [(12,45),(12,19),(32,41),(52,19),(52,45)]]
    draw.line(points,fill=color,width=max(3,round(5*scale)),joint="curve")
    cx,cy=point(51,14);r=round(4*scale)
    draw.ellipse((cx-r,cy-r,cx+r,cy+r),fill=color)

def write_svg():
    svg='''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="104" viewBox="0 0 620 104" role="img" aria-labelledby="title">
<title id="title">Multiverse — independent software and AI research</title>
<rect width="104" height="104" rx="22" fill="#0b1221"/>
<path d="M19.5 73.1V30.9l32.5 35.75 32.5-35.75v42.2" fill="none" stroke="#77e8da" stroke-width="8.125" stroke-linejoin="round"/>
<circle cx="82.9" cy="22.75" r="6.5" fill="#77e8da"/>
<text x="129" y="64" fill="#f1f9fc" font-family="DejaVu Sans, Arial, sans-serif" font-size="45" font-weight="800" letter-spacing="3">MULTIVERSE</text>
<text x="133" y="89" fill="#a5bfcb" font-family="DejaVu Sans, Arial, sans-serif" font-size="14" letter-spacing="1.7">INDEPENDENT SOFTWARE &amp; AI SYSTEMS</text>
</svg>'''
    (OUT/"multiverse-lockup.svg").write_text(svg+"\n")

def text(draw,xy,s,size,bold=False,color=WHITE):
    font=face(size,bold);x,y=xy
    length=draw.textlength(s,font=font)
    assert x+length<=draw._image.size[0]-25,(s,length,draw._image.size)
    draw.text((x,y),s,font=font,fill=color)
    return length

def add_grid(img,step=54):
    d=ImageDraw.Draw(img,"RGBA");w,h=img.size
    for x in range(0,w,step):d.line((x,0,x,h),fill=(119,232,218,11),width=1)
    for y in range(0,h,step):d.line((0,y,w,y),fill=(119,232,218,11),width=1)

def social():
    img=bg((1200,630));add_grid(img,60);d=ImageDraw.Draw(img)
    monogram(d,(72,66,100))
    text(d,(196,78),"MULTIVERSE",67,True)
    text(d,(75,226),"Independent software",54,True)
    text(d,(75,301),"and AI systems.",54,True,color=TEAL)
    d.line((76,395,500,395),fill=TEAL,width=3)
    text(d,(75,431),"SWAAG  /  KnowMoreDiRT  /  Digital products",26,color=WHITE)
    text(d,(75,488),"Public code, working examples and ongoing research",23,color=MUTED)
    d.rounded_rectangle((75,555,292,598),radius=20,fill=(22,68,80))
    text(d,(98,561),"MULTIVERSE",19,True,color=TEAL)
    img.save(OUT/"multiverse-social-preview.png",optimize=True)

def banner():
    img=bg((1584,396));add_grid(img,66);d=ImageDraw.Draw(img)
    # Personal LinkedIn profile avatars obscure the lower left.
    monogram(d,(512,72,112))
    text(d,(657,78),"MULTIVERSE",73,True)
    text(d,(657,173),"Independent software & AI systems",34,color=WHITE)
    text(d,(657,241),"SWAAG   /   KnowMoreDiRT   /   3D",23,color=TEAL)
    text(d,(657,297),"Research  •  Engineering  •  Digital products",20,color=MUTED)
    img.save(OUT/"multiverse-linkedin-banner.png",optimize=True)

def square():
    img=bg((1024,1024));d=ImageDraw.Draw(img)
    d.rounded_rectangle((95,95,929,929),radius=175,fill=(11,18,33),outline=(32,74,84),width=7)
    monogram(d,(211,211,602))
    img.save(OUT/"multiverse-profile-icon.png",optimize=True)

def main():
    write_svg();social();banner();square()
    for p in sorted(OUT.glob("*")):print(f"{p.relative_to(ROOT)}: {p.stat().st_size} bytes")

if __name__=="__main__":main()
