# Сцена 5 «Диета»: Лене 14. Та же кухня вечером, 19:00. Родители ужинают, Лена со стаканом воды.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
kitchen_env(env, day=False)
# часы: 19:00 — перерисовать стрелки
env.ell(110,66,6,6,'white',1.6)
env.line(110,66,110,60,'hair',-1)          # минутная — на 12
env.line(110,66,107,70,'hair',-1)          # часовая — на 7
env.put(110,66,'red',2)
# мама слева, папа справа — ужинают
seated(env,ch,120,1,'blue','hair','hair','bob',1.4,'table',expr='look')
seated(env,ch,206,-1,'teal','hair','hair','short',0.9,'table',expr='down')
# Лена 14 стоит за столом, повернулась к маме, держит стакан
hand=standing(env,ch,168,-1,'yel','blue','hair','pony',0.6,'look',feet=172,arm='give',tall=94)
table_top(front)
# стакан воды в руке Лены
gx,gy=hand[0]+1,hand[1]-5
front.rect(gx-2,gy,gx+2,gy+7,'white',2.2); front.rect(gx-1,gy+2,gx+1,gy+6,'blue',4.4); front.rect(gx-2,gy,gx+2,gy,'white',3.4)
# еда: тарелки родителей с пастой, кастрюля, пустая тарелка Лены
for x in (134,198):
    front.ell(x,TY-1,9,2,'white',0.8); front.rect(x-8,TY,x+8,TY,'white',-0.4)
    front.ell(x,TY-2,5,1.4,'yel',3.2); front.put(x-2,TY-3,'red',2.4); front.put(x+2,TY-2,'red',2.4)
front.ell(162,TY-1,8,1.6,'white',1.4); front.rect(155,TY,169,TY,'white',-0.4)          # пустая тарелка
front.rect(176,TY-8,188,TY-2,'red',1.2); front.rect(175,TY-9,189,TY-8,'red',2.2)      # кастрюля
front.rect(173,TY-7,175,TY-6,'red',0.4); front.rect(189,TY-7,191,TY-6,'red',0.4)
for (x,y,h) in [(180,TY-12,1.6),(182,TY-15,1.2),(184,TY-13,1.4)]: front.put(x,y,'white',h)
# вилки
for x,f in ((140,1),(192,-1)): front.line(x,TY-1,x+f*5,TY-4,'white',2.4)
# ── свет: лампа (как в первой сцене)
def L(x,y):
    dx=x-LX;dy=y-LY
    d=math.hypot(dx,dy*(2.4 if dy<0 else 0.82))
    l=0.07+0.98*max(0,1-d/185)**1.45
    if 26<=x<=86 and 48<=y<FLOOR: l=0.04+0.12*max(0,(x-50)/36)*(1 if y>90 else 0.4)
    if y>=FLOOR and 108<=x<=204 and y<=FLOOR+22: l*=0.45+0.55*abs(x-156)/50
    if 100<=x<=230 and y>TY+8 and ch.get(x,y) is not None: l*=0.6
    return l
img=render([env,ch,front],L)
img.save('scene05_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene05_5x.png')
print('ok')
