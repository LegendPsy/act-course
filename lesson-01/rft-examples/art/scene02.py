# Сцена 2 «Конфета»: Лене 7, та же кухня днём. Мама протягивает конфету, папа: «Хватит ей сладкого…»
from lena_lib import *
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
kitchen_env(env, day=True)
# окно днём: значения неба — без света сцены (NOLIGHT), пересчитаем сдвиги
for y in range(36,103):
    for x in range(196,257):
        v=env.get(x,y)
        if v and v[0]=='daysky': env.put(x,y,'daysky',min(5,max(0,(102-y)/66*3.2+1.2)))
        if v and v[0]=='stone': env.put(x,y,'stone',2+v[1])
# Лена (7) сидит слева, тянется к конфете
hand_l=child_seated(env,ch,122,1,'yel','hair',0.6,arm='reach',expr='up')
# мама стоит за столом, протягивает конфету
hand_m=standing(env,ch,166,-1,'blue','hair','hair','bob',1.4,'soft',feet=170,arm='give')
# папа сидит справа, ладонь «хватит»
seated(env,ch,206,-1,'teal','hair','hair','short',0.9,'stop',expr='stern')
table_top(front)
# конфета в руке мамы (красный фантик)
cx,cy=hand_m[0]-3,hand_m[1]
front.ell(cx,cy,2.6,2,'red',1.6); front.rect(cx-1,cy-2,cx+1,cy-2,'red',3)
for dx in (-4,4):
    front.put(cx+dx,cy-2,'red',1.2); front.put(cx+dx,cy+2,'red',1.2); front.put(cx+dx,cy,'red',0.6)
# ваза с конфетами и газета папы
front.ell(150,TY-3,8,3,'white',0.6,clip=lambda x,y:y>=TY-4); front.rect(143,TY-4,157,TY-4,'white',1.4)
for (x,c) in [(146,'red'),(150,'yel'),(154,'red'),(148,'blue'),(152,'green')]: front.put(x,TY-5,c,2.2)
front.rect(170,TY-2,186,TY-1,'white',1.0); front.rect(170,TY-3,186,TY-3,'white',1.8)
for x in range(172,185,3): front.put(x,TY-2,'white',-0.6)
# ── свет: день из окна
WXc,WYc=226,72
def L(x,y):
    d=math.hypot(x-WXc,(y-WYc)*0.9)
    l=0.50+0.30*max(0,1-d/420)
    if 26<=x<=86 and 48<=y<FLOOR: l=0.34+0.10*max(0,(x-50)/36)
    # солнечное пятно на полу слева от окна
    if FLOOR<=y<=FLOOR+30:
        t=(y-FLOOR)/30; x0=150-60*t; x1=232-40*t
        if x0<=x<=x1: l+=0.18
    if y>=FLOOR and 108<=x<=204 and y<=FLOOR+22: l*=0.6+0.4*abs(x-156)/50
    return l
def Lc(x,y):
    l=L(x,y)
    if 100<=x<=230 and y>TY+8 and ch.get(x,y) is not None: l*=0.7
    return l
def rim(li,x,y):
    return li==1 and ch.get(x,y) is not None and ch.get(x+(1 if x<WXc else -1),y) is None and y<TY
img=render([env,ch,front],Lc,rim=rim)
img.save('scene02_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene02_5x.png')
print('ok')
