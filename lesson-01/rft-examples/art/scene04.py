# Сцена 4 «Антон и Настя»: Лене 13. Школьный двор осенью; Антон и Настя уходят за руку; Лена с одноклассницей смотрят.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(21)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
GY=126   # линия, где школа встречается с асфальтом
# небо
for y in range(0,GY):
    env.rect(0,y,W-1,y,'daysky',min(5,1.8+y/GY*2.8))
for (cx,cy,rx) in [(60,22,14),(78,18,10),(300,30,16),(320,26,10)]: env.ell(cx,cy,rx,4,'daysky',5)
# здание школы
env.rect(120,30,383,GY,'red',1.2)
for y in range(32,GY,4):
    for x in range(120+(4 if (y//4)%2 else 0),384,8): env.put(x,y,'red',0.4)
    env.rect(120,y,383,y,'red',0.6)
env.rect(118,26,383,30,'tile',3.2)
for row,y0 in enumerate((40,80)):
    for x0 in range(132,380,34):
        env.rect(x0,y0,x0+22,y0+26,'tile',4.6); env.rect(x0+2,y0+2,x0+20,y0+24,'daysky',3.6)
        env.rect(x0+11,y0+2,x0+11,y0+24,'tile',4.6); env.rect(x0+2,y0+12,x0+20,y0+12,'tile',4.6)
        env.rect(x0-1,y0+26,x0+23,y0+27,'tile',3.6)
env.rect(330,96,362,GY,'wood',0.6); env.rect(332,98,360,GY,'wood',-0.4); env.rect(345,98,346,GY,'wood',-1)  # двери
env.rect(324,90,368,93,'tile',3.8)
# асфальт и бордюр
for y in range(GY,H): env.rect(0,y,W-1,y,'tile',1.6+(y-GY)/(H-GY)*0.8)
for k in range(260): env.put(random.randint(0,W-1),random.randint(GY,H-1),'tile',0.6)
env.rect(0,GY,W-1,GY+1,'tile',3.2)
# забор слева и деревья
for x in range(0,118,6): env.rect(x,96,x+1,GY,'blue',-0.6)
env.rect(0,100,118,101,'blue',-0.4); env.rect(0,116,118,117,'blue',-0.4)
def tree(x,y,s=1.0):
    env.rect(x-2,y,x+2,y+int(46*s),'wood',-0.4); env.line(x,y+12,x-10,y+2,'wood',-0.4,2); env.line(x,y+16,x+9,y+6,'wood',-0.4,2)
    for (dx,dy,r,c,h) in [(-12,-4,12,'yel',2.6),(8,-10,13,'red',4.2),(0,-18,12,'yel',3.6),(-16,-16,9,'red',3.6),(14,2,9,'yel',2.2)]:
        env.ell(x+dx*s,y+dy*s,r*s,r*0.8*s,c,h)
tree(40,70); tree(366,64,0.8)
for k in range(40): env.put(random.randint(0,W-1),random.randint(GY+4,H-1),random.choice(['yel','red']),random.choice([2.4,3.2,4]))
# скамейка слева
env.rect(14,150,62,153,'wood',0.8); env.rect(16,154,19,166,'wood',-0.4); env.rect(57,154,60,166,'wood',-0.4); env.rect(14,142,62,145,'wood',0.4)
# ── персонажи
# Лена 13: жёлтая кофта, серая юбка, красный рюкзак; смотрит вправо на пару
LX_=92; LF=184
standing(env,ch,LX_,1,'yel','tile','hair','pony',0.6,'look',feet=LF,arm='down',tall=84,skirt=True)
ch.rect(LX_-11,LF-74,LX_-7,LF-52,'red',1.2); ch.rect(LX_-12,LF-72,LX_-11,LF-54,'red',0.2)   # рюкзак
ch.line(LX_-6,LF-72,LX_+3,LF-70,'red',1.8)
# одноклассница рядом, поворачивается к Лене и говорит
standing(env,ch,LX_-30,1,'mag','tile','hair','bob',0.2,'smile',feet=LF-2,arm='talk',tall=84,skirt=True)
# Антон и Настя уходят вправо, держась за руки
standing(env,ch,262,1,'blue','tile','hair','short',3.0,'smile',feet=178,arm='back',tall=88)
standing(env,ch,240,1,'green','tile','red','long',1.4,'smile',feet=176,arm='hold',tall=84,skirt=True)
# тени на асфальте (солнце справа — тени влево)
for (x,fy) in [(LX_,LF),(LX_-30,LF-2),(262,178),(240,176)]:
    env.poly([(x-3,fy),(x+4,fy),(x-14,fy+5),(x-24,fy+5)],'tile',-1.0)
# ── свет: дневной, тёплое солнце справа
def L(x,y):
    l=0.5
    if y>GY: l=0.42
    if ch.get(x,y) is not None: l=0.56
    return l
img=render([env,ch,front],L)
img.save('scene04_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene04_5x.png')
print('ok')
