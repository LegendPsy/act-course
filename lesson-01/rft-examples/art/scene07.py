# Сцена 7 «ЕГЭ»: Лене 16–17. Ночь, её комната; учёба за столом под лампой, мама с чашкой.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(41)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=168
env.rect(0,0,W-1,FL-1,'wall',0)
for x in range(0,W,12): env.rect(x,0,x,FL-1,'wall',-0.5)
env.rect(0,FL-4,W-1,FL-1,'wood',-1.2); env.rect(0,FL,W-1,H-1,'wood',-0.4)
yy=FL;step=4
while yy<H: env.rect(0,yy,W-1,yy,'wood',-1.3); yy+=step; step+=3
# окно над столом
WX0,WY0,WX1,WY1=290,30,350,96
env.rect(WX0-4,WY0-4,WX1+4,WY1+3,'wood',0)
for y in range(WY0,WY1+1):
    for x in range(WX0,WX1+1): env.put(x,y,'sky',(y-WY0)/(WY1-WY0)*3.4)
for k in range(12): env.put(random.randint(WX0,WX1),random.randint(WY0,WY0+34),'moon')
env.ell(302,42,4,4,'moon')
bx=WX0
while bx<WX1:
    w=random.randint(5,10);h=random.randint(10,24); env.rect(bx,WY1-h,min(bx+w,WX1),WY1,'hall',-1)
    for wy in range(WY1-h+3,WY1-2,4):
        for wx in range(bx+2,min(bx+w,WX1)-1,3):
            if random.random()<0.25: env.put(wx,wy,'city')
    bx+=w+1
env.rect((WX0+WX1)//2,WY0,(WX0+WX1)//2+1,WY1,'wood',0)
for (x0,x1) in ((WX0-14,WX0-2),(WX1+2,WX1+14)):
    env.rect(x0,22,x1,WY1+14,'mag',0.4)
    for x in range(x0,x1+1,3): env.rect(x,22,x,WY1+14,'mag',-0.6)
env.rect(WX0-16,20,WX1+16,21,'wood',0.6)
# кровать слева, зайка, детские рисунки и постер
env.rect(14,96,20,FL+12,'wood',0.2)
env.rect(20,140,130,158,'white',0.4); env.rect(20,159,130,162,'wood',0.2)
front.poly([(60,137),(132,134),(134,160),(58,160)],'blue',0.6)
env.ell(38,136,16,6,'white',1.2)
front.ell(110,128,5,5,'white',0.8); front.ell(107,120,1.4,4,'white',0.8); front.ell(112,119,1.4,4,'white',0.6); front.put(108,128,'eye'); front.put(112,128,'eye')
for (x,y) in [(30,58),(56,52)]:
    env.rect(x,y,x+20,y+15,'white',0.6); env.rect(x+9,y-1,x+11,y,'red',1)
env.ell(35,63,2,2,'yel',2); env.poly([(40,71),(40,67),(44,63),(48,67),(48,71)],'red',1.4)
env.ell(66,60,5,4,'wood',2.2); env.ell(61,57,1.5,3,'wood',1.2); env.ell(71,57,1.5,3,'wood',1.2)
env.rect(96,40,136,92,'blue',0.2); env.rect(98,42,134,90,'mag',0.6); env.ell(116,60,10,10,'yel',1.6)
# календарь с зачёркнутыми днями
env.rect(160,52,190,80,'white',1.2); env.rect(160,52,190,56,'red',1.8)
for r in range(4):
    for c in range(5):
        x=163+c*5;y=59+r*5
        if r*5+c<13: env.line(x,y,x+3,y+3,'red',1.4); env.line(x+3,y,x,y+3,'red',1.4)
        else: env.put(x+1,y+1,'white',-0.4)
# стол и лампа
DY=134
env.rect(262,DY+6,265,FL+14,'wood',-0.5); env.rect(368,DY+6,371,FL+14,'wood',-0.5)
seated(env,ch,252,1,'yel','blue','hair','pony',0.6,'table',expr='down')
front.rect(258,DY,376,DY+5,'wood',0.4); front.rect(258,DY,376,DY+1,'wood',1.3); front.rect(258,DY+5,376,DY+5,'wood',-1.5)
# стопки учебников
for (x,n) in [(300,5),(318,3),(334,6)]:
    for k in range(n):
        c=['red','blue','green','yel','mag','teal'][(k+x)%6]
        front.rect(x+(k%2),DY-4-k*4,x+13+(k%2),DY-1-k*4,c,0.6); front.rect(x+(k%2),DY-4-k*4,x+13+(k%2),DY-4-k*4,c,1.6)
# пробник с красными пометками
front.rect(270,DY-3,292,DY-1,'white',1.6)
for x in (274,281,287): front.line(x,DY-3,x+2,DY-1,'red',2.4)
# лампа
LPX,LPY=356,100
front.rect(354,DY-3,362,DY-1,'hair',0.6); front.line(358,DY-3,352,DY-22,'hair',0.6); front.line(352,DY-22,358,DY-32,'hair',0.6)
front.poly([(352,DY-36),(364,DY-36),(368,DY-28),(348,DY-28)],'yel',1.4); front.rect(350,DY-28,366,DY-27,'bulb')
# мама стоит позади с чашкой
hand=standing(env,ch,192,1,'blue','hair','hair','bob',1.4,'look',feet=176,arm='give',tall=100)
front.rect(hand[0]-1,hand[1]-4,hand[0]+4,hand[1]+1,'white',1.4); front.rect(hand[0]+5,hand[1]-3,hand[0]+6,hand[1]-1,'white',0.8)
for (x,y) in [(hand[0]+1,hand[1]-7),(hand[0]+2,hand[1]-9)]: front.put(x,y,'white',1.6)
# ── свет: настольная лампа + ночь
LAX,LAY=358,DY-26
def L(x,y):
    l=0.15
    d=math.hypot(x-LAX,(y-LAY)*(1.6 if y<LAY else 0.9))
    isc=ch.get(x,y) is not None
    k=1.0 if (isc or front.get(x,y) is not None) else 0.75
    l+=0.85*k*max(0,1-d/200)**1.4
    if isc: l=max(l,0.40)
    return l
img=render([env,ch,front],L)
img.save('scene07_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene07_5x.png')
print('ok')
