# Сцена 11 «Кабинет»: Лене 25. Кабинет психолога днём; два кресла, Лена и психолог.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(71)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=168
env.rect(0,0,W-1,FL-1,'green',1.5)
for x in range(0,W,16): env.rect(x,0,x+7,FL-1,'green',1.75)
env.rect(0,FL-4,W-1,FL-1,'wood',0.8)
for y in range(FL,H):
    for x in range(W): env.put(x,y,'wood',0.7 if ((x+(y-FL)*2)//22)%2 else 0.4)
env.ell(196,196,120,14,'red',0.3); env.ell(196,196,110,11,'red',0.8)
# окно слева
WX0,WY0,WX1,WY1=24,34,96,112
env.rect(WX0-4,WY0-4,WX1+4,WY1+4,'white',3.2)
for y in range(WY0,WY1+1): env.rect(WX0,y,WX1,y,'daysky',min(5,1.6+(y-WY0)/(WY1-WY0)*2.6))
for (cx,cy,rx) in [(44,50,8),(56,46,6),(80,60,7)]: env.ell(cx,cy,rx,2.5,'daysky',5)
env.rect(59,WY0,61,WY1,'white',3.2); env.rect(WX0,72,WX1,73,'white',3.2)
env.rect(WX0-8,WY1+4,WX1+8,WY1+7,'white',3.6)
# растение у окна
env.rect(104,136,122,FL,'red',1.4); env.rect(102,134,124,136,'red',2.2)
for (dx,dy,h) in [(-10,-34,2),(0,-44,3),(10,-36,2),(-14,-18,1.4),(14,-20,1.6),(4,-26,2.4)]:
    env.line(113,134,113+dx,134+dy,'green',h-1,1); env.ell(113+dx,134+dy,4,2.4,'green',h)
# книжная полка справа
env.rect(318,40,376,FL-1,'wood',1.0); env.rect(321,43,373,FL-3,'wood',0.2)
for row,y0 in enumerate((44,74,104,134)):
    env.rect(321,y0+26,373,y0+28,'wood',1.4)
    x=323
    while x<370:
        w=random.randint(3,6);h=random.randint(16,24);c=random.choice(['red','blue','green','yel','mag','teal'])
        env.rect(x,y0+26-h,x+w,y0+25,c,random.choice([1.2,1.8,2.4])); x+=w+1
# картина на стене
env.rect(178,40,238,82,'wood',1.4); env.rect(181,43,235,79,'daysky',3.6)
env.poly([(181,79),(196,58),(210,70),(222,54),(235,79)],'green',2.0); env.ell(224,52,3,3,'yel',4)
# торшер
env.rect(290,76,292,FL+4,'hair',0.6); env.poly([(282,64),(300,64),(304,78),(278,78)],'white',2.6)
# кресла
def armchair(x0,x1,col):
    env.rect(x0,110,x1,150,col,0.6); env.rect(x0,110,x1,112,col,1.4)
    env.rect(x0-6,124,x0+2,162,col,1.0); env.rect(x1-2,124,x1+6,162,col,1.0)
    env.rect(x0,150,x1,160,col,1.2); env.rect(x0,150,x1,150,col,2.0)
    env.rect(x0-4,162,x0-1,FL+10,'wood',-0.4); env.rect(x1+1,162,x1+4,FL+10,'wood',-0.4)
armchair(126,170,'mag')        # кресло Лены
armchair(242,286,'teal')       # кресло психолога
# Лена (25): сидит, руки на коленях, смотрит на психолога
seated(env,ch,146,1,'yel','blue','hair','pony',0.6,'table',expr='look',with_chair=False)
# психолог: короткая стрижка, блокнот на коленях
hand=seated(env,ch,266,-1,'blue','hair','hair','short',1.4,'phone',expr='soft',with_chair=False)
front.rect(hand[0]-6,hand[1]+2,hand[0]+2,hand[1]+12,'white',2.6); front.rect(hand[0]-6,hand[1]+2,hand[0]+2,hand[1]+3,'red',2)
for y in range(hand[1]+5,hand[1]+12,2): front.rect(hand[0]-5,y,hand[0]+1,y,'white',1.2)
# столик между креслами: салфетки, вода
front.rect(186,146,226,149,'wood',1.6); front.rect(190,150,193,FL+12,'wood',0.4); front.rect(219,150,222,FL+12,'wood',0.4)
front.rect(190,138,204,145,'white',2.6); front.poly([(195,138),(198,132),(201,138)],'white',3.4)
front.rect(212,134,218,145,'daysky',3.0); front.rect(212,134,218,135,'white',3.4)
# ── свет: день из окна слева + торшер
def L(x,y):
    l=0.40+0.12*max(0,1-x/W)
    if y>=FL:
        t=(y-FL)/(H-FL)
        if 60+30*t<=x<=170+60*t: l+=0.12
    if ch.get(x,y) is not None or front.get(x,y) is not None: l=max(l,0.56)
    return l
img=render([env,ch,front],L)
img.save('scene11_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene11_5x.png')
print('ok')
