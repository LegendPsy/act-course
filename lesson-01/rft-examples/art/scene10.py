# Сцена 10 «Давай встретимся?»: Лене 20–24. Та же квартира, обжитая; зеркало завешено, фото перевёрнуты; Лена на полу с телефоном.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(61)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=168
env.rect(0,0,W-1,FL-1,'tile',0.6); env.rect(0,FL-3,W-1,FL-1,'tile',-0.6)
for y in range(FL,H):
    for x in range(0,W): env.put(x,y,'wood',0.2 if ((x+(y-FL)*3)//26)%2 else -0.1)
# окно со шторами (задёрнуты почти полностью)
WX0,WY0,WX1,WY1=280,34,352,110
env.rect(WX0-4,WY0-4,WX1+4,WY1+4,'tile',1.6)
for y in range(WY0,WY1+1):
    for x in range(WX0,WX1+1): env.put(x,y,'sky',(y-WY0)/(WY1-WY0)*3.0)
for k in range(10): env.put(random.randint(310,322),random.randint(70,108),'city')
env.rect(WX0-8,28,312,WY1+16,'mag',0.2); env.rect(320,28,WX1+8,WY1+16,'mag',0.2)
for x in list(range(WX0-8,312,3))+list(range(320,WX1+8,3)): env.rect(x,28,x,WY1+16,'mag',-0.6)
env.rect(WX0-10,26,WX1+10,27,'wood',0.6)
# лампа-торшер (тёплый, но слабый свет)
env.rect(262,70,264,FL+6,'hair',0.4); env.poly([(254,60),(272,60),(276,72),(250,72)],'yel',1.0); env.rect(256,FL+5,270,FL+7,'hair',0.4)
# зеркало, полностью завешенное платком (видна только нижняя рамка)
env.rect(30,40,66,110,'wood',0.8)
env.poly([(26,36),(70,36),(72,104),(64,98),(56,106),(48,98),(40,106),(32,98),(24,104)],'mag',1.2)
for x in range(28,70,4): env.line(x,38,x+1,100,'mag',0.4)
env.rect(26,36,70,38,'mag',2.0)
for x in range(26,72,3): env.put(x,104 if (x//3)%2 else 102,'mag',0.6)
env.rect(30,106,66,110,'wood',0.8)
# полка: цветок и перевёрнутые фото
env.rect(84,74,140,77,'wood',1.0)
for x in (90,104): env.rect(x,71,x+12,73,'hair',1.2); env.rect(x,71,x+12,71,'white',1.2); env.line(x+10,71,x+13,66,'hair',1.2)
env.rect(122,62,132,73,'red',0.8); env.line(127,62,123,52,'green',1.2); env.line(127,62,131,50,'green',1.6); env.ell(124,52,2,1.4,'green',2); env.ell(131,50,2,1.4,'green',2)
# крючок: сумка для бассейна с очками
env.rect(160,50,164,52,'hair',0.6); env.line(162,52,156,62,'hair',0.6); env.line(162,52,170,62,'hair',0.6)
env.poly([(152,62),(174,62),(178,92),(148,92)],'blue',1.2); env.rect(152,62,174,63,'blue',2)
env.ell(158,74,3,2,'daysky',2.4); env.ell(166,74,3,2,'daysky',2.4); env.rect(161,74,163,74,'hair',0.4)
# диван
SX0,SX1=96,212
env.rect(SX0,112,SX1,148,'blue',0.2); env.rect(SX0,112,SX1,114,'blue',1.0)
env.rect(SX0-8,124,SX0,160,'blue',0.6); env.rect(SX1,124,SX1+8,160,'blue',0.6)
env.rect(SX0,148,SX1,158,'blue',0.8); env.rect(SX0,148,SX1,148,'blue',1.6)
env.rect(SX0-6,160,SX0-3,FL+8,'wood',-0.8); env.rect(SX1+3,160,SX1+6,FL+8,'wood',-0.8)
env.ell(196,138,9,6,'mag',0.8)
# ковёр
env.ell(170,196,110,12,'mag',-0.4); env.ell(170,196,100,9,'mag',0.2)
# ── Лена сидит на полу, спиной к дивану, колени подтянуты (как в 12 лет)
cx,hip=150,184
f=1;X=lambda d:cx+f*d
ch.poly([(X(-2),hip-6),(X(22),hip-24),(X(26),hip-20),(X(4),hip)],'blue',-0.4)
ch.poly([(X(22),hip-24),(X(26),hip-22),(X(30),hip-2),(X(26),hip)],'blue',-0.6)
ch.poly([(X(-9),hip-36),(X(3),hip-36),(X(6),hip-26),(X(6),hip-4),(X(-10),hip),(X(-12),hip-20)],'yel',0.2)
ch.rect(X(-8),hip-36,X(2),hip-36,'yel',1.2)
for yy in range(hip-30,hip-2): ch.put(X(-11),yy,'yel',-0.9)
ch.poly([(X(-4),hip-8),(X(20),hip-26),(X(25),hip-21),(X(2),hip+1)],'blue',0.4)
ch.poly([(X(20),hip-26),(X(25),hip-24),(X(30),hip-1),(X(25),hip+1)],'blue',0.1)
ch.rect(X(24),hip,X(33),hip+2,'white',1.6)
ch.line(X(0),hip-30,X(10),hip-22,'yel',0.6,3); ch.line(X(10),hip-22,X(18),hip-28,'yel',0.8,3)
ch.ell(X(19),hip-29,2,2,'skin',0.6)
ch.rect(X(-1),hip-41,X(1),hip-37,'skin',-0.3)
head(ch,X(1),hip-50,f,'hair','pony','down',hairsh=0.6)
PHX,PHY=X(21),hip-31
front.rect(PHX-2,PHY-4,PHX+1,PHY+3,'black'); front.rect(PHX-1,PHY-3,PHX,PHY+2,'screen')
# ── свет: торшер слабый + экран
def L(x,y):
    l=0.13
    d=math.hypot(x-263,(y-70)*0.9); l+=0.32*max(0,1-d/200)**1.3
    isc=ch.get(x,y) is not None or front.get(x,y) is not None
    pd=math.hypot(x-PHX,(y-PHY)*1.1); l+=(0.45 if isc else 0.12)*max(0,1-pd/60)**1.2
    return l
img=render([env,ch,front],L)
pp=img.load()
for y in range(H):
    for x in range(W):
        r,g,b=pp[x,y];pp[x,y]=(int(r*.9),int(g*.92),min(255,int(b*1.08)))
img.save('scene10_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene10_5x.png')
print('ok')
