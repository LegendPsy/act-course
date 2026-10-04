# Сцена 6 «Комплименты»: Лене 14. Школьный коридор на перемене.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
random.seed(31)
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
FL=170
env.rect(0,0,W-1,FL-1,'tile',2.4)                      # верх стены — светлый
env.rect(0,112,W-1,FL-1,'teal',1.6); env.rect(0,110,W-1,111,'teal',3.0)   # панель
env.rect(0,FL-3,W-1,FL-1,'teal',0.2)
for y in range(FL,H):                                   # линолеум
    for x in range(W):
        env.put(x,y,'tile',1.8 if ((x//12+ (y-FL)//6)%2) else 1.2)
env.rect(0,FL,W-1,FL,'tile',2)
# окна справа + батареи
for x0 in (262,326):
    env.rect(x0-3,30,x0+45,102,'tile',3.6); env.rect(x0,33,x0+42,99,'daysky',3.0)
    for (cx,cy) in [(x0+12,48),(x0+30,44)]: env.ell(cx,cy,7,2.4,'daysky',5)
    env.rect(x0+20,33,x0+21,99,'tile',3.6); env.rect(x0,64,x0+42,65,'tile',3.6)
    env.rect(x0-5,102,x0+47,104,'tile',4.0)
    env.rect(x0+4,128,x0+38,150,'tile',2.6)
    for x in range(x0+6,x0+38,4): env.rect(x,128,x+1,150,'tile',1.4)
# дверь класса слева и доска объявлений
env.rect(14,52,58,FL-1,'wood',0.6); env.rect(17,55,55,FL-1,'wood',-0.4); env.rect(48,108,51,110,'yel',3)
env.rect(22,60,50,74,'daysky',3.2); env.rect(35,60,36,74,'wood',1.2)
env.rect(80,46,140,90,'wood',0.8); env.rect(83,49,137,87,'wood',2.4)
for (x,y,w,h,c,sh) in [(88,53,14,10,'white',3.8),(106,52,12,14,'yel',3.6),(122,56,12,9,'white',3.8),(90,68,16,12,'mag',3.6),(112,70,18,10,'white',3.8)]:
    env.rect(x,y,x+w,y+h,c,sh); env.put(x+w//2,y,'red',3)
# ── персонажи
FEET=184
# мальчик у стены слева смотрит на Лену
standing(env,ch,118,1,'green','hair','hair','short',2.4,'smile',feet=FEET-6,arm='down',tall=88)
# Лена — смущённо улыбается
standing(env,ch,174,1,'yel','tile','hair','pony',0.6,'smile',feet=FEET,arm='down',tall=86,skirt=True)
# одноклассницы
standing(env,ch,206,-1,'mag','tile','hair','bob',0.2,'laugh',feet=FEET+2,arm='talk',tall=86,skirt=True)
standing(env,ch,234,-1,'blue','tile','hair','long',2.0,'smile',feet=FEET,arm='down',tall=88,skirt=True)
# румянец Лены сильнее
for (x,y) in [(173,FEET-81),(172,FEET-81),(182,FEET-82)]: ch.put(x,y,'cheek')
# ── свет: день из окон справа
def L(x,y):
    l=0.40+0.22*(x/W)
    if y>=FL:   # солнечные пятна от окон на полу
        t=(y-FL)/(H-FL)
        for x0 in (262,326):
            if x0-40*t<=x<=x0+42-40*t: l+=0.16
    if ch.get(x,y) is not None: l=0.54+0.12*(x/W)
    return l
img=render([env,ch,front],L)
img.save('scene06_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene06_5x.png')
print('ok')
