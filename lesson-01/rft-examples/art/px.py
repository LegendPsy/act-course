# Пиксельный рендерер: слой материалов (рампа + локальный сдвиг) × карта света, Bayer-дизеринг.
import math, random
from PIL import Image
W,H=384,216
def hx(h): return tuple(int(h[i:i+2],16) for i in (1,3,5))
R={k:[hx(c) for c in v.split()] for k,v in dict(
 wall='#120f1a #1d1828 #2c2235 #43303d #5f4243 #845a4b #a87754 #c9975f #e2b874 #f2d595',
 hall='#060509 #0c0a12 #13101c #1c1828 #262036 #312a44',
 wood='#0d0a0d #1f1418 #33201f #4d2f26 #6c4330 #8f5b3a #b17845 #cf9a5a #e6bb79',
 teal='#0b1013 #142024 #1d3236 #2a4748 #3c605d #557c73 #73998a #98b8a2',
 tile='#1a1720 #2e2a33 #4a4448 #6e6660 #958a7c #b8aa95 #d6c8ad #ede0c4 #fbf1d8',
 skin='#2a1716 #4a2a26 #73413a #9b5c4c #c27f64 #dfa080 #f2c3a0 #fde0c6',
 hair='#0c0809 #1a1012 #2a1a19 #3d2621 #54352a #6e4734 #8a5d40',
 yel='#2a1a0c #4f3212 #7d5216 #a8751c #d19c25 #f0c23e #fde27a #fff2b8',
 blue='#0c1120 #152038 #1f3256 #2c4a78 #3e679a #5b88b8 #86afd6',
 mag='#150a14 #2a1226 #45203d #66304f #8a4565 #ad5f7c #cf8299',
 blond='#1f170f #3d2d19 #634a26 #8c6a35 #b38d4a #d4b064 #ecd38e #f7e8b8',
 red='#1a0b0d #3a1215 #631c1d #8f2c25 #b8452f #d9673d #f08e55 #ffb27a',
 white='#2a2730 #4b4650 #757078 #a19b9c #c9c2ba #e6dfd2 #fbf6ea #ffffff',
 green='#0b120d #15241a #20382a #2f5038 #436c45 #5f8a55 #84ab6c',
 sky='#05060d #0a0d1c #10162c #18203d #22294d #2f3560',
 daysky='#5f86b8 #7aa2cf #97bde0 #b8d6ee #d9eaf6 #f4f9fd',
 stone='#5b6070 #737889 #8d91a0 #a8abb7 #c3c5ce',
).items()}
FIX={'eye':hx('#160c0e'),'mouth':hx('#8a2e2a'),'mouthd':hx('#3a1012'),'cheek':hx('#e38a76'),'screen':hx('#d6f4ff'),
     'glow':hx('#8fd0ff'),'city':hx('#ffd56b'),'city2':hx('#ff9f4a'),'moon':hx('#f4eccf'),'bulb':hx('#fff6d6'),'black':hx('#07060a')}
NOLIGHT={'daysky','stone'}
BAYER=[[0,8,2,10],[12,4,14,6],[3,11,1,9],[15,7,13,5]]
class Layer:
    def __init__(s): s.m=[[None]*W for _ in range(H)]
    def put(s,x,y,ramp,sh=0):
        x,y=int(round(x)),int(round(y))
        if 0<=x<W and 0<=y<H: s.m[y][x]=(ramp,sh)
    def get(s,x,y):
        return s.m[y][x] if 0<=x<W and 0<=y<H else None
    def rect(s,x0,y0,x1,y1,ramp,sh=0):
        for y in range(int(y0),int(y1)+1):
            for x in range(int(x0),int(x1)+1): s.put(x,y,ramp,sh)
    def ell(s,cx,cy,rx,ry,ramp,sh=0,clip=None):
        for y in range(int(cy-ry-1),int(cy+ry+2)):
            for x in range(int(cx-rx-1),int(cx+rx+2)):
                if ((x-cx)/(rx+.35))**2+((y-cy)/(ry+.35))**2<=1 and (clip is None or clip(x,y)): s.put(x,y,ramp,sh)
    def poly(s,pts,ramp,sh=0):
        ys=[p[1] for p in pts]
        for y in range(int(min(ys)),int(max(ys))+1):
            xs=[]
            n=len(pts)
            for i in range(n):
                (x1,y1),(x2,y2)=pts[i],pts[(i+1)%n]
                if (y1<=y+.5<y2) or (y2<=y+.5<y1):
                    xs.append(x1+(y+.5-y1)*(x2-x1)/(y2-y1))
            xs.sort()
            for i in range(0,len(xs)-1,2):
                for x in range(int(math.ceil(xs[i]-.5)),int(math.floor(xs[i+1]-.5))+1): s.put(x,y,ramp,sh)
    def line(s,x0,y0,x1,y1,ramp,sh=0,w=1):
        n=int(max(abs(x1-x0),abs(y1-y0)))+1
        for i in range(n+1):
            t=i/max(n,1);x=x0+(x1-x0)*t;y=y0+(y1-y0)*t
            for dx in range(w):
                for dy in range(w): s.put(x+dx-w//2,y+dy-w//2,ramp,sh)
def render(layers,L,dither=True,rim=None):
    img=Image.new('RGB',(W,H))
    px=img.load()
    for y in range(H):
        for x in range(W):
            c=None
            for li,lay in enumerate(layers):
                v=lay.m[y][x]
                if v is not None: c=(li,v)
            if c is None: px[x,y]=(0,0,0);continue
            li,(ramp,sh)=c
            if ramp in FIX: px[x,y]=FIX[ramp];continue
            r=R[ramp];n=len(r)
            l=L(x,y)
            if rim and rim(li,x,y): l+=0.28
            f=sh if ramp in NOLIGHT else max(0,min(1,l))*(n-1)*0.92+sh
            base=math.floor(f);fr=f-base
            if dither and getattr(layers[li],'dither',True):
                if fr>0.68: base+=1
                elif fr>0.32 and (x+y)%2==0: base+=1
            else:
                base=round(f)
            px[x,y]=r[max(0,min(n-1,base))]
    return img
