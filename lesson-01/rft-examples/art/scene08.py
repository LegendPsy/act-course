# Сцена 8 «Срыв»: Лене 17. Та же кухня глубокой ночью; лампа выключена, светит открытый холодильник.
import px
px.W,px.H=384,216
from lena_lib import *
W,H=px.W,px.H
env=Layer(); ch=Layer(); ch.dither=False; front=Layer(); front.dither=False
kitchen_env(env, day=False, table=False)
T0,T1=150,250
for lx in (T0+8,T1-12):
    env.rect(lx,TY+6,lx+4,FLOOR+20,'wood',-0.4); env.rect(lx+4,TY+6,lx+4,FLOOR+20,'wood',-1.4)
env.rect(LX-12,49,LX+12,51,'white',-0.6)        # лампа выключена
# холодильник слева (закрывает часы), дверца открыта к стене
FX0,FX1,FY0=100,132,64
env.rect(FX0,FY0,FX1,FL_:=FLOOR-1,'white',0.6)
env.rect(FX0+2,FY0+2,FX1-2,FLOOR-3,'bulb')                       # светящееся нутро
for y in (92,112,132): env.rect(FX0+2,y,FX1-2,y+1,'white',1.2)   # полки
for (x,y,w,h,c) in [(104,84,5,8,'red'),(112,86,7,6,'yel'),(122,82,6,10,'green'),(106,104,10,8,'white'),(120,106,8,6,'blue'),(104,124,8,8,'mag'),(116,126,12,6,'yel')]:
    env.rect(x,y,x+w,y+h,c,1.6)
env.poly([(FX0-12,FY0-6),(FX0,FY0),(FX0,FLOOR-1),(FX0-12,FLOOR+6)],'white',-0.2)    # дверца
env.rect(FX0-10,100,FX0-2,101,'white',1.2); env.rect(FX0-10,120,FX0-2,121,'white',1.2)
# Лена сидит у правого края стола, лицом к свету
seated(env,ch,240,-1,'yel','blue','hair','pony',0.6,'table',expr='down')
front.rect(T0,TY,T1,TY+5,'wood',0.4); front.rect(T0,TY,T1,TY+1,'wood',1.3); front.rect(T0,TY+5,T1,TY+5,'wood',-1.5); front.rect(T0+2,TY+6,T1-2,TY+8,'wood',-0.9)
# еда на столе: пачки печенья, бутерброд, крошки, кружка
front.poly([(194,TY-1),(196,TY-9),(210,TY-9),(212,TY-1)],'red',1.4); front.rect(196,TY-9,210,TY-8,'red',2.4)
for x in (199,203,207): front.ell(x,TY-11,2,1,'wood',2.6)
front.poly([(170,TY-1),(172,TY-6),(186,TY-7),(188,TY-1)],'blue',1.2)                 # вторая пачка, открытая
front.ell(222,TY-1,8,1.6,'white',1.0); front.rect(216,TY-4,228,TY-2,'wood',2.4); front.rect(216,TY-4,228,TY-4,'yel',3.2)  # бутерброд
for (x,y) in [(190,TY-1),(214,TY-1),(182,TY),(206,TY),(230,TY-1),(174,TY)]: front.put(x,y,'wood',2.8)
front.rect(160,TY-6,165,TY-1,'white',0.8)
# ── свет: холодильник (холодный) + луна
FLX,FLY=116,110
def L(x,y):
    l=0.07
    d=math.hypot(x-FLX,(y-FLY)*0.9); k=1.0 if (ch.get(x,y) is not None or front.get(x,y) is not None) else 0.8
    l+=0.8*k*max(0,1-d/200)**1.5
    if y>=FLOOR and FX0-30<=x<=FX1+90 and y<=FLOOR+40: l+=0.12*max(0,1-abs(x-150)/120)   # свет на полу
    return l
img=render([env,ch,front],L)
pp=img.load()
for y in range(H):
    for x in range(W):
        d=math.hypot(x-FLX,y-FLY)
        r,g,b=pp[x,y]
        if d<170 and not (FX0+2<=x<=FX1-2 and FY0+2<=y<=FLOOR-3):
            k=.32*(1-d/170)
            pp[x,y]=(int(r*(1-k)+170*k),int(g*(1-k)+215*k),int(b*(1-k)+255*k))
        else: pp[x,y]=(int(r*.85),int(g*.9),min(255,int(b*1.1)))
img.save('scene08_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('scene08_5x.png')
print('ok')
