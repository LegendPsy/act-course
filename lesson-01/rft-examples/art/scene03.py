# Сцена 3 «Антон»: Лене 12. Ночь, её комната, сидит на кровати и читает ответ в телефоне.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(11)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=168
# стена и пол
env.rect(0,0,W-1,FL-1,'wall',0)
for x in range(0,W,12): env.rect(x,0,x,FL-1,'wall',-0.5)          # обои в полоску
env.rect(0,FL-4,W-1,FL-1,'wood',-1.2)
env.rect(0,FL,W-1,H-1,'wood',-0.4)
yy=FL;step=4
while yy<H: env.rect(0,yy,W-1,yy,'wood',-1.3); yy+=step; step+=3
env.ell(210,190,90,12,'mag',0.6)                                     # коврик
env.ell(210,190,82,9,'mag',1.2)
# окно с луной и шторами
WX0,WY0,WX1,WY1=296,36,352,108
env.rect(WX0-4,WY0-4,WX1+4,WY1+3,'wood',0)
for y in range(WY0,WY1+1):
    for x in range(WX0,WX1+1): env.put(x,y,'sky',(y-WY0)/(WY1-WY0)*3.4)
for k in range(14):
    env.put(random.randint(WX0,WX1),random.randint(WY0,WY0+40),'moon')
env.ell(338,52,5,5,'moon')
random.seed(5);bx=WX0
while bx<WX1:
    w=random.randint(5,10);h=random.randint(10,26)
    env.rect(bx,WY1-h,min(bx+w,WX1),WY1,'hall',-1)
    for wy in range(WY1-h+3,WY1-2,4):
        for wx in range(bx+2,min(bx+w,WX1)-1,3):
            if random.random()<0.25: env.put(wx,wy,'city')
    bx+=w+1
env.rect((WX0+WX1)//2,WY0,(WX0+WX1)//2+1,WY1,'wood',0)
env.rect(WX0-8,WY1+3,WX1+8,WY1+6,'wood',0.8)
for (x0,x1) in ((WX0-14,WX0-2),(WX1+2,WX1+14)):                       # шторы
    env.rect(x0,28,x1,WY1+18,'mag',0.4)
    for x in range(x0,x1+1,3): env.rect(x,28,x,WY1+18,'mag',-0.6)
env.rect(WX0-16,26,WX1+16,27,'wood',0.6)
# стол слева с выключенной лампой и книгами
env.rect(16,118,104,121,'wood',0.6); env.rect(16,118,104,118,'wood',1.5)
env.rect(20,122,23,FL+14,'wood',-0.5); env.rect(97,122,100,FL+14,'wood',-0.5)
env.rect(60,122,100,146,'wood',-0.2); env.rect(62,124,98,144,'wood',-0.8); env.rect(78,132,82,133,'white',0.5)
env.rect(30,112,36,117,'hair',0.5); env.line(33,112,40,98,'hair',0.5); env.poly([(36,92),(48,92),(44,100),(38,100)],'yel',0.2)
for k,(c,hh) in enumerate([('red',10),('blue',12),('green',9),('yel',11)]):
    env.rect(70+k*5,118-hh,73+k*5,117,c,0.4); env.rect(70+k*5,118-hh,73+k*5,118-hh,c,1.4)
# детские рисунки над кроватью (мостик к коллажу) и постер
def sheet(x,y,rot=0):
    env.rect(x,y,x+20,y+15,'white',1.0); env.rect(x+9,y-1,x+11,y,'red',1.5)
    return x,y
x,y=sheet(124,52); env.ell(x+5,y+5,2,2,'yel',2.5); env.poly([(x+10,y+13),(x+10,y+9),(x+14,y+5),(x+18,y+9),(x+18,y+13)],'red',1.8)
x,y=sheet(150,46); env.ell(x+10,y+8,5,4,'wood',2.6); env.ell(x+5,y+5,1.5,3,'wood',1.6); env.ell(x+15,y+5,1.5,3,'wood',1.6); env.put(x+10,y+9,'eye')
x,y=sheet(176,56); env.rect(x+8,y+3,x+10,y+12,'green',2.2); env.rect(x+5,y+6,x+13,y+8,'green',2.2)
env.rect(222,38,262,92,'blue',0.2); env.rect(224,40,260,90,'mag',0.6)
env.ell(242,58,10,10,'yel',1.6); env.rect(228,74,256,76,'white',1.2); env.rect(232,80,252,81,'white',0.6)
# кровать
BX0,BX1,BT=110,290,140
env.rect(BX0-6,92,BX0,FL+12,'wood',0.2); env.rect(BX0-6,92,BX0,93,'wood',1.4)          # изголовье
env.rect(BX0,BT,BX1,BT+18,'white',0.4); env.rect(BX0,BT+16,BX1,BT+18,'white',-0.8)      # матрас
env.rect(BX0,BT+19,BX1,BT+22,'wood',0.2); env.rect(BX0+2,BT+23,BX0+5,FL+14,'wood',-0.6); env.rect(BX1-5,BT+23,BX1-2,FL+14,'wood',-0.6)
env.ell(132,BT-4,18,7,'white',1.2); env.ell(132,BT-6,14,4,'white',2)                     # подушка
front.poly([(200,BT-3),(BX1,BT-6),(BX1+2,BT+20),(196,BT+20)],'blue',0.6)               # одеяло в ногах
for y in range(BT,BT+20,5): front.rect(198,y,BX1,y,'blue',-0.4)
front.rect(BX1-1,BT-6,BX1+2,BT+21,'blue',-0.8)
# плюшевый зайка (из детства)
front.ell(256,BT-10,6,6,'white',0.8); front.ell(252,BT-19,1.6,5,'white',0.8); front.ell(258,BT-20,1.6,5,'white',0.6)
front.put(254,BT-11,'eye'); front.put(258,BT-11,'eye'); front.ell(256,BT-2,7,4,'white',0.6)
# ── Лена 12 сидит на кровати, колени подтянуты, телефон в руках
cx,hip=160,BT-2
f=1;X=lambda d:cx+f*d
# дальняя нога
ch.poly([(X(-2),hip-6),(X(22),hip-24),(X(26),hip-20),(X(4),hip)],'tile',1.4)
ch.poly([(X(22),hip-24),(X(26),hip-22),(X(30),hip-2),(X(26),hip)],'tile',1.0)
# торс (худи жёлтое), спина к подушке
ch.poly([(X(-9),hip-36),(X(3),hip-36),(X(6),hip-26),(X(6),hip-4),(X(-10),hip),(X(-12),hip-20)],'yel',0.2)
ch.rect(X(-8),hip-36,X(2),hip-36,'yel',1.2)
for yy in range(hip-30,hip-2): ch.put(X(-11),yy,'yel',-0.9)
ch.poly([(X(-10),hip-38),(X(-2),hip-38),(X(-2),hip-33),(X(-10),hip-33)],'yel',-0.8)       # капюшон
# ближняя нога
ch.poly([(X(-4),hip-8),(X(20),hip-26),(X(25),hip-21),(X(2),hip+1)],'tile',2.2)
ch.poly([(X(20),hip-26),(X(25),hip-24),(X(30),hip-1),(X(25),hip+1)],'tile',1.8)
ch.rect(X(24),hip,X(33),hip+2,'white',1.6)                                               # носок
# руки к телефону у колен
ch.line(X(0),hip-30,X(10),hip-22,'yel',0.6,3); ch.line(X(10),hip-22,X(18),hip-28,'yel',0.8,3)
ch.ell(X(19),hip-29,2,2,'skin',0.6)
ch.rect(X(-1),hip-41,X(1),hip-37,'skin',-0.3)
head(ch,X(1),hip-50,f,'hair','pony','down',hairsh=0.6)
PHX,PHY=X(21),hip-31
front.rect(PHX-2,PHY-4,PHX+1,PHY+3,'black'); front.rect(PHX-1,PHY-3,PHX,PHY+2,'screen')
ch.put(X(6),hip-48,'white',3)    # слеза
# ── свет: ночь, луна из окна, экран телефона
def L(x,y):
    l=0.18
    d=math.hypot(x-324,(y-70)*0.8); l+=0.10*max(0,1-d/170)
    pd=math.hypot(x-PHX,(y-PHY)*1.1)
    if ch.get(x,y) is not None: l+=0.58*max(0,1-pd/60)**1.2       # лицо и руки — в свете экрана
    elif front.get(x,y) is not None: l+=0.30*max(0,1-pd/90)
    else: l+=0.16*max(0,1-pd/110)                                  # стена дальше — свет слабее
    return l
img=render([env,ch,front],L)
pp=img.load()
for y in range(H):
    for x in range(W):
        pd=math.hypot(x-PHX,y-PHY)
        isc=ch.get(x,y) is not None or front.get(x,y) is not None
        if pd<60 and isc:
            r,g,b=pp[x,y];k=.30*(1-pd/60)**1.5
            pp[x,y]=(int(r*(1-k)+120*k),int(g*(1-k)+200*k),int(b*(1-k)+255*k))
        else:   # холодный ночной тон
            r,g,b=pp[x,y];pp[x,y]=(int(r*.88),int(g*.92),min(255,int(b*1.08)))
img.save('scene03_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene03_5x.png')
print('ok')
