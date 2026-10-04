# Сцена 9 «Своя квартира»: Лене 19. Ночь, съёмная квартира, коробки, дождь; диван, ноутбук, еда навынос, телефон.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(51)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=168
env.rect(0,0,W-1,FL-1,'tile',0.6)
env.rect(0,FL-3,W-1,FL-1,'tile',-0.6)
for y in range(FL,H):
    for x in range(0,W):
        env.put(x,y,'wood',0.2 if ((x+ (y-FL)*3)//26)%2 else -0.1)
# окно с дождём
WX0,WY0,WX1,WY1=280,34,352,110
env.rect(WX0-4,WY0-4,WX1+4,WY1+4,'tile',1.6)
for y in range(WY0,WY1+1):
    for x in range(WX0,WX1+1): env.put(x,y,'sky',(y-WY0)/(WY1-WY0)*3.0)
bx=WX0
while bx<WX1:
    w=random.randint(6,12);h=random.randint(16,40); env.rect(bx,WY1-h,min(bx+w,WX1),WY1,'hall',-1)
    for wy in range(WY1-h+3,WY1-2,4):
        for wx in range(bx+2,min(bx+w,WX1)-1,3):
            if random.random()<0.3: env.put(wx,wy,'city' if random.random()<.8 else 'city2')
    bx+=w+1
for k in range(60):
    x=random.randint(WX0,WX1);y=random.randint(WY0,WY1-3)
    env.put(x,y,'sky',4.6); env.put(x,y+1,'sky',4.0)
env.rect((WX0+WX1)//2,WY0,(WX0+WX1)//2+1,WY1,'tile',1.6)
# голая лампочка
env.line(150,0,150,26,'hair',0); env.ell(150,29,2.5,3,'white',0.4)
# коробки после переезда
for (x,y,w,h) in [(14,128,40,40),(20,98,32,30),(58,140,34,28),(318,138,44,30)]:
    env.rect(x,y,x+w,y+h,'wood',1.6); env.rect(x,y,x+w,y,'wood',2.6); env.rect(x+w//2-2,y,x+w//2+1,y+h,'yel',1.2)
    env.rect(x,y+h,x+w,y+h,'wood',0.4)
env.rect(24,108,46,112,'white',1.4)   # надпись на коробке
# вешалка с курткой
env.rect(100,52,106,54,'hair',0.6); env.poly([(98,56),(108,56),(112,104),(94,104)],'red',-0.2); env.poly([(100,56),(106,56),(106,66),(100,66)],'red',0.6)
# диван
SX0,SX1=128,236
env.rect(SX0,112,SX1,148,'blue',0.2); env.rect(SX0,112,SX1,114,'blue',1.0)
for x in (164,200): env.rect(x,114,x,146,'blue',-0.6)
env.rect(SX0-8,124,SX0,160,'blue',0.6); env.rect(SX1,124,SX1+8,160,'blue',0.6)
env.rect(SX0,148,SX1,158,'blue',0.8); env.rect(SX0,148,SX1,148,'blue',1.6)
env.rect(SX0-6,160,SX0-3,FL+8,'wood',-0.8); env.rect(SX1+3,160,SX1+6,FL+8,'wood',-0.8)
env.ell(214,138,9,6,'mag',0.8)   # подушка
# Лена сидит на диване с телефоном
seated(env,ch,160,1,'yel','blue','hair','pony',0.6,'phone',expr='down',with_chair=False)
PHX,PHY=176,116
front.rect(PHX-2,PHY-4,PHX+1,PHY+3,'black'); front.rect(PHX-1,PHY-3,PHX,PHY+2,'screen')
# низкий столик: ноутбук, контейнеры, чипсы
front.rect(232,160,300,163,'wood',0.6); front.rect(236,164,239,FL+16,'wood',-0.6); front.rect(293,164,296,FL+16,'wood',-0.6)
front.rect(266,152,290,159,'hair',0.4); front.poly([(268,152),(288,152),(292,134),(272,134)],'hair',0.2)
front.poly([(270,150),(287,150),(290,137),(274,137)],'screen')
front.rect(240,152,252,159,'white',1.4); front.rect(240,152,252,153,'red',2.2)          # контейнер
front.rect(254,154,262,159,'white',1.0)
front.poly([(243,151),(245,141),(257,141),(259,151)],'yel',2.2)   # пачка чипсов
for k in range(0,12,2): front.put(245+k,140,'yel',3.2)
front.rect(246,144,256,147,'red',2.4); front.ell(251,145,2,1,'white',3)
# ── свет: ноутбук + телефон + окно
LAPX,LAPY=281,143
def L(x,y):
    l=0.10
    d=math.hypot(x-LAPX,(y-LAPY)*0.9); isc=ch.get(x,y) is not None or front.get(x,y) is not None
    l+=(0.55 if isc else 0.38)*max(0,1-d/170)**1.4
    pd=math.hypot(x-PHX,y-PHY); l+=(0.35 if isc else 0.1)*max(0,1-pd/50)
    d2=math.hypot(x-316,(y-72)*0.8); l+=0.08*max(0,1-d2/120)
    return l
img=render([env,ch,front],L)
pp=img.load()
for y in range(H):
    for x in range(W):
        r,g,b=pp[x,y];pp[x,y]=(int(r*.86),int(g*.92),min(255,int(b*1.12)))
img.save('scene09_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene09_5x.png')
print('ok')
