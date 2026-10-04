# Общие части сцен истории Лены: кухня, головы, фигуры. Пиксельный стиль — px.py
import math, random
from px import *
FLOOR=168
TX0,TX1,TY=106,206,134
LX,LY=150,50

def kitchen_env(env, day=False, table=True):
    random.seed(7)
    env.rect(0,0,W-1,FLOOR-1,'wall')
    env.rect(0,FLOOR-4,W-1,FLOOR-1,'wood',-1.2); env.rect(0,FLOOR-4,W-1,FLOOR-4,'wood',-0.4)
    env.rect(0,FLOOR,W-1,H-1,'wood',0)
    yy=FLOOR;step=4
    while yy<H:
        env.rect(0,yy,W-1,yy,'wood',-0.9); yy+=step; step+=3
    for i in range(-20,30):
        x0=192+i*9
        for y in range(FLOOR,H):
            t=(y-FLOOR)/(H-FLOOR); x=192+(x0-192)*(1+t*2.2)
            if random.random()<0.75: env.put(x,y,'wood',-0.7)
    # дверной проём и коридор
    env.rect(18,40,94,FLOOR-1,'wood',-0.6); env.rect(19,41,93,41,'wood',0.6)
    env.rect(26,48,86,FLOOR-1,'hall',0); env.rect(26,150,86,FLOOR-1,'hall',1); env.rect(26,148,86,149,'hall',-0.5)
    env.rect(40,64,64,148,'hall',0.8); env.rect(41,65,63,147,'hall',0.3)
    if not day: env.rect(42,147,62,147,'yel',-1.5)
    env.rect(60,104,61,106,'hall',2)
    for (x,y) in [(74,60),(80,60)]: env.rect(x,y,x+1,y+2,'hall',2)
    env.poly([(70,63),(84,63),(86,110),(68,110)],'hall',1.4); env.poly([(72,63),(82,63),(82,72),(72,72)],'hall',2.2)
    # окно
    WX0,WY0,WX1,WY1=196,36,256,102
    env.rect(WX0-4,WY0-4,WX1+4,WY1+2,'wood',0.2)
    for y in range(WY0,WY1+1):
        for x in range(WX0,WX1+1):
            t=(y-WY0)/(WY1-WY0)
            if day: env.put(x,y,'daysky',2.8-t*1.6)
            else: env.put(x,y,'sky',t*3.2)
    random.seed(3); bx=WX0
    while bx<WX1:
        w=random.randint(6,13);h=random.randint(14,40)
        env.rect(bx,WY1-h,min(bx+w,WX1),WY1,'stone' if day else 'hall',(random.random()*1.2) if day else -1)
        for wy in range(WY1-h+3,WY1-2,4):
            for wx in range(bx+2,min(bx+w,WX1)-1,3):
                if random.random()<(0.5 if day else 0.32):
                    if day: env.put(wx,wy,'stone',-1.5)
                    else: env.put(wx,wy,'city' if random.random()<.8 else 'city2')
        bx+=w+random.randint(0,2)
    if day:
        for (cx,cy,rx) in [(214,48,7),(222,45,6),(232,50,5),(244,58,6)]:
            env.ell(cx,cy,rx,2.5,'daysky',4.2)
    else:
        env.ell(246,46,3,3,'moon')
    env.rect((WX0+WX1)//2-1,WY0,(WX0+WX1)//2+1,WY1,'wood',0); env.rect(WX0,(WY0+WY1)//2-1,WX1,(WY0+WY1)//2,'wood',0)
    env.rect(WX0-6,WY1+2,WX1+6,WY1+5,'wood',1); env.rect(WX0-6,WY1+6,WX1+6,WY1+6,'wood',-1.5)
    env.rect(240,WY1-4,248,WY1+1,'red',0.5); env.rect(240,WY1-4,248,WY1-4,'red',1.5)
    for dx,dy,h in [(-3,-14,0),(0,-18,1),(4,-13,0),(6,-9,1),(-5,-8,0)]:
        env.line(244,WY1-5,244+dx,WY1-5+dy,'green',h,1); env.ell(244+dx,WY1-5+dy,1.6,1.2,'green',h+0.5)
    # гарнитур
    env.rect(270,22,383,74,'teal',0)
    for x0 in (272,302,332,360):
        env.rect(x0,24,x0+26,72,'teal',-0.9); env.rect(x0+2,26,x0+24,70,'teal',0.3); env.rect(x0+2,26,x0+24,26,'teal',1.2); env.rect(x0+20,46,x0+21,50,'white',1)
    env.rect(270,74,383,75,'teal',-2)
    env.rect(262,76,383,117,'tile',0)
    for y in range(76,118):
        for x in range(262,384):
            if (y-76)%8==0 or (x-262+(5 if ((y-76)//8)%2 else 0))%10==0: env.put(x,y,'tile',-2.6)
            elif (y-76)%8==1: env.put(x,y,'tile',0.8)
    env.rect(258,116,383,121,'wood',0.6); env.rect(258,116,383,116,'wood',1.8); env.rect(258,121,383,121,'wood',-1)
    env.rect(260,122,383,FLOOR-1,'teal',-0.3)
    for x0 in (262,292,322,352):
        env.rect(x0,124,x0+27,FLOOR-6,'teal',-1); env.rect(x0+2,126,x0+25,FLOOR-8,'teal',0.2); env.rect(x0+12,130,x0+15,131,'white',1)
    env.ell(300,108,8,7,'white',0.4,clip=lambda x,y:y>=102); env.rect(293,110,307,115,'white',0.2)
    env.rect(296,100,304,102,'white',0.8); env.rect(298,98,302,99,'white',1.4)
    env.line(308,106,314,100,'white',0.2); env.line(291,104,288,110,'white',-1); env.rect(293,115,307,115,'white',-1.2)
    if not day:
        for (x,y,h) in [(315,97,1.4),(316,95,1.2),(316,93,1.0),(315,91,0.8),(314,89,0.6),(315,87,0.4),(317,85,0.2),(318,83,0)]: env.put(x,y,'white',h)
    for (x,c) in [(330,'red'),(340,'yel'),(350,'green')]:
        env.rect(x,105,x+6,115,c,-0.2); env.rect(x,104,x+6,105,'white',0.5); env.rect(x+1,107,x+1,113,c,1.2)
    # часы
    env.ell(110,66,8,8,'white',0.8); env.ell(110,66,6,6,'white',1.6)
    env.line(110,66,110,61,'hair',-1); env.line(110,66,114,66,'hair',-1); env.put(110,66,'red',2)
    # лампа
    env.line(LX,0,LX,37,'hair',0)
    env.poly([(LX-9,37),(LX+9,37),(LX+17,50),(LX-17,50)],'red',0); env.rect(LX-8,38,LX+8,38,'red',1.5)
    if day: env.rect(LX-12,49,LX+12,51,'white',0.5)
    else: env.rect(LX-12,49,LX+12,51,'bulb')
    # ножки стола
    for lx in ((118,190) if table else ()):
        env.rect(lx,TY+6,lx+4,FLOOR+20,'wood',-0.4); env.rect(lx+4,TY+6,lx+4,FLOOR+20,'wood',-1.4)

def table_top(front):
    front.rect(TX0,TY,TX1,TY+5,'wood',0.4); front.rect(TX0,TY,TX1,TY+1,'wood',1.3)
    front.rect(TX0,TY+5,TX1,TY+5,'wood',-1.5); front.rect(TX0+2,TY+6,TX1-2,TY+8,'wood',-0.9)

def head(L,cx,cy,f,hairr,style,expr,hairsh=0):
    if style=='bob':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.rect(cx-f*8 if f>0 else cx+1,cy,cx-1 if f>0 else cx+f*-8,cy+6,hairr,hairsh-0.5)
    elif style=='long':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.poly([(cx-f*9,cy-2),(cx-f*2,cy-2),(cx-f*3,cy+18),(cx-f*10,cy+16)],hairr,hairsh-0.3)
    elif style=='pony':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.ell(cx-f*10,cy+5,3,6,hairr,hairsh-0.2); L.ell(cx-f*12,cy+11,2,3,hairr,hairsh-0.5)
        L.rect(cx-f*8,cy-1,cx-f*8+1*(-f if f<0 else 1)-(1 if f<0 else 0),cy,'yel',2.6)
    elif style=='short':
        L.ell(cx-f*1,cy-2,8.2,7.6,hairr,hairsh)
    L.ell(cx+f*1,cy+1,6.8,7.6,'skin',0.6); L.ell(cx+f*1,cy+6,4.5,2.5,'skin',0.6)
    L.put(cx+f*8,cy+2,'skin',0.6)
    L.put(cx-f*4,cy+7,'skin',-0.6); L.put(cx-f*3,cy+8,'skin',-0.6)
    L.put(cx-f*3,cy+2,'skin',-0.2); L.put(cx-f*3,cy+3,'skin',-0.6)
    for x in range(-7,8):
        top=cy-8+int(abs(x)/3)
        bottom=cy-3 if style!='long' else cy-4
        if style=='short': bottom=cy-6
        if f*x>3: bottom=cy-5 if style=='bob' else (cy-7 if style=='short' else cy-4)
        if f*x<-3: bottom=cy+(5 if style not in ('pony','short') else (1 if style=='pony' else 0))
        for y in range(top,bottom+1): L.put(cx+x,y,hairr,hairsh+(0.8 if y==top else 0))
    L.put(cx-f*2,cy-7,hairr,hairsh+2); L.put(cx-f*1,cy-7,hairr,hairsh+1.6); L.put(cx+f*1,cy-8,hairr,hairsh+1.2)
    e1,e2=cx+f*2,cx+f*6; ey=cy+1
    if expr=='laugh':
        for ex in (e1,e2): L.put(ex-1,ey,'eye');L.put(ex,ey-1,'eye');L.put(ex+1,ey,'eye')
        mx=cx+f*4
        L.rect(mx-1,cy+5,mx+1,cy+6,'mouthd'); L.rect(mx-1,cy+5,mx+1,cy+5,'white',2.5); L.put(mx,cy+7,'mouth')
        L.put(e2+f*1,cy+4,'cheek'); L.put(e1-f*1,cy+4,'cheek')
    elif expr=='stern':
        for ex in (e1,e2): L.put(ex,ey,'eye'); L.put(ex,ey+1,'eye')
        L.put(e1-f*1,ey-2,hairr,hairsh-0.6); L.put(e1,ey-1,hairr,hairsh-0.6)        # брови к переносице
        L.put(e2+f*1,ey-2,hairr,hairsh-0.6); L.put(e2,ey-1,hairr,hairsh-0.6)
        L.rect(min(cx+f*3,cx+f*6),cy+6,max(cx+f*3,cx+f*6),cy+6,'mouthd')
    elif expr=='soft':
        for ex in (e1,e2): L.put(ex,ey,'eye'); L.put(ex,ey+1,'eye')
        L.put(cx+f*4,cy+6,'mouth'); L.put(cx+f*5,cy+5,'mouth'); L.put(cx+f*3,cy+5,'mouth')
        L.put(e1-f*1,cy+4,'cheek')
    elif expr=='down':   # смотрит вниз (рисует)
        for ex in (e1,e2): L.put(ex,ey+1,'eye'); L.put(ex+f*1,ey+1,'eye')
        L.put(cx+f*4,cy+6,'mouth'); L.put(e1-f*1,cy+4,'cheek')
    elif expr=='sleep':  # глаза закрыты, спокойна
        for ex in (e1,e2): L.put(ex-1,ey,'eye'); L.put(ex,ey+1,'eye'); L.put(ex+1,ey,'eye')
        L.put(cx+f*4,cy+6,'mouth'); L.put(e1-f*1,cy+4,'cheek'); L.put(e2+f*1,cy+4,'cheek')
    elif expr=='smile':  # открытые глаза + улыбка
        for ex in (e1,e2): L.put(ex,ey,'eye'); L.put(ex,ey+1,'eye'); L.put(ex+f*1 if f<0 else ex,ey,'white',3)
        mx=cx+f*4
        L.rect(mx-1,cy+5,mx+1,cy+5,'mouthd'); L.put(mx-f*2,cy+4,'mouthd'); L.put(mx,cy+6,'mouth')
        L.put(e1-f*1,cy+4,'cheek'); L.put(e2+f*1,cy+4,'cheek')
    else:  # look / up (взгляд вверх)
        dy=-1 if expr=='up' else 0
        for ex in (e1,e2):
            L.put(ex,ey+dy,'eye');L.put(ex,ey+1+dy,'eye');L.put(ex+f*1 if f<0 else ex,ey+dy,'white',3)
        L.put(e1-f*1,ey-2,hairr,hairsh-0.5); L.put(e2,ey-2,hairr,hairsh-0.5)
        L.put(cx+f*4,cy+6,'mouth'); L.put(cx+f*5,cy+6,'mouth')
        L.put(e1-f*1,cy+4,'cheek')
    L.rect(cx+f*1-1,cy+9,cx+f*1+1,cy+11,'skin',-0.3)

PSH={'hair':0.4,'blue':-1.6}
def chair(env,cx,f,seat=153,back_top=110):
    X=lambda d:cx+f*d
    env.rect(min(X(-11),X(-10)),back_top+2,max(X(-11),X(-10)),FLOOR+16,'wood',-0.2)
    env.rect(min(X(-12),X(-9)),back_top,max(X(-12),X(-9)),back_top+2,'wood',0.8)
    env.rect(min(X(-11),X(8)),seat,max(X(-11),X(8)),seat+2,'wood',0.3); env.rect(min(X(-11),X(8)),seat,max(X(-11),X(8)),seat,'wood',1.2)
    env.rect(min(X(7),X(8)),seat+3,max(X(7),X(8)),FLOOR+16,'wood',-0.7)

def seated(env,ch,cx,f,top,pants,hairr,style,hairsh,arm,expr='laugh',with_chair=True):
    """Взрослый сидит в профиль. Возвращает точку кисти."""
    X=lambda d:cx+f*d; hy=100; ps=PSH.get(pants,0)
    if with_chair: chair(env,cx,f)
    for off,sh in ((-2,-0.9),(0,0)):
        ch.rect(min(X(17+off),X(20+off)),150,max(X(17+off),X(20+off)),FLOOR+10,pants,ps+sh)
        ch.rect(min(X(16+off),X(24+off)),FLOOR+11,max(X(16+off),X(24+off)),FLOOR+12,'hair',-0.3+sh)
    ch.poly([(X(-8),146),(X(20),146),(X(22),149),(X(20),152),(X(-8),153)],pants,ps)
    ch.rect(min(X(-6),X(20)),146,max(X(-6),X(20)),146,pants,ps+1.1)
    ch.poly([(X(-5),111),(X(5),111),(X(7),117),(X(6),136),(X(7),146),(X(-8),147),(X(-7),126),(X(-6),116)],top,0)
    ch.rect(min(X(-4),X(4)),111,max(X(-4),X(4)),111,top,0.9)
    for yy in range(116,146): ch.put(X(-7),yy,top,-0.8)
    ch.rect(min(X(0),X(2)),108,max(X(0),X(2)),111,'skin',-0.3)
    head(ch,X(2),hy,f,hairr,style,expr,hairsh=hairsh)
    if arm=='table':
        ch.line(X(1),114,X(5),127,top,-0.3,3); ch.line(X(5),127,X(17),131,top,0.1,3); ch.ell(X(20),131,2.2,1.8,'skin',0.6); return (X(20),131)
    if arm=='phone':
        ch.line(X(1),114,X(4),126,top,-0.3,3); ch.line(X(4),126,X(12),119,top,0.1,3); ch.ell(X(14),118,2.2,2,'skin',0.6); return (X(14),118)
    if arm=='stop':   # рука вытянута вперёд, ладонь вертикально: «хватит»
        ch.line(X(1),114,X(8),123,top,-0.3,3); ch.line(X(8),123,X(17),116,top,0.1,3)
        ch.rect(min(X(18),X(20)),108,max(X(18),X(20)),116,'skin',0.6)      # ладонь
        for k in range(4): ch.put(X(21),109+k*2,'skin',0.2)                 # пальцы
        ch.put(X(17),111,'skin',0.2); ch.put(X(17),112,'skin',0.2)           # большой палец
        return (X(19),112)

def standing(env,ch,cx,f,top,pants,hairr,style,hairsh,expr,feet=176,arm='give',tall=100,skirt=False):
    """Взрослый стоит в профиль, чуть наклонён вперёд. feet — уровень стоп."""
    X=lambda d:cx+f*d; ps=PSH.get(pants,0)
    hy=feet-tall
    for off,sh in ((-3,-0.9),(1,0)):
        ch.rect(min(X(-3+off),X(0+off)),hy+46,max(X(-3+off),X(0+off)),feet-1,pants,ps+sh)
        ch.rect(min(X(-4+off),X(4+off)),feet,max(X(-4+off),X(4+off)),feet+1,'hair',-0.3+sh)
    ch.poly([(X(-7),hy+40),(X(6),hy+40),(X(5),hy+48),(X(-6),hy+48)],pants,ps)
    ch.poly([(X(-4),hy+11),(X(6),hy+11),(X(8),hy+17),(X(6),hy+30),(X(6),hy+42),(X(-7),hy+43),(X(-6),hy+28),(X(-5),hy+16)],top,0)
    ch.rect(min(X(-3),X(5)),hy+11,max(X(-3),X(5)),hy+11,top,0.9)
    for yy in range(hy+16,hy+42): ch.put(X(-6),yy,top,-0.8)
    ch.rect(min(X(1),X(3)),hy+8,max(X(1),X(3)),hy+11,'skin',-0.3)
    head(ch,X(3),hy,f,hairr,style,expr,hairsh=hairsh)
    if skirt:
        ch.poly([(X(-7),hy+40),(X(6),hy+40),(X(9),hy+56),(X(-10),hy+56)],pants,ps+0.3)
        for k in range(-9,9,3): ch.put(X(k),hy+56,pants,ps-0.8)
    if arm=='give':
        ch.line(X(2),hy+14,X(8),hy+26,top,-0.3,3); ch.line(X(8),hy+26,X(19),hy+33,top,0.1,3)
        ch.ell(X(21),hy+33,2.2,2,'skin',0.6); return (X(22),hy+32)
    if arm=='down':
        ch.line(X(0),hy+14,X(1),hy+38,top,-0.2,3); ch.ell(X(1),hy+40,1.8,2,'skin',0.6); return (X(1),hy+40)
    if arm=='hold':   # рука вперёд-вниз: держит за руку
        ch.line(X(1),hy+14,X(5),hy+30,top,-0.2,3); ch.line(X(5),hy+30,X(11),hy+40,'skin',0.4,2); return (X(12),hy+41)
    if arm=='back':   # рука назад-вниз: держит за руку того, кто сзади
        ch.line(X(-1),hy+14,X(-5),hy+30,top,-0.2,3); ch.line(X(-5),hy+30,X(-11),hy+40,'skin',0.4,2); return (X(-12),hy+41)
    if arm=='talk':   # жест у груди
        ch.line(X(1),hy+14,X(6),hy+28,top,-0.2,3); ch.line(X(6),hy+28,X(10),hy+22,'skin',0.4,2); return (X(10),hy+21)

def child_seated(env,ch,cx,f,top,hairr,hairsh,arm='reach',expr='up',hy=112):
    """Ребёнок 6–8 лет сидит в профиль; ноги не достают до пола."""
    X=lambda d:cx+f*d
    seat=hy+33
    chair(env,cx,f,seat=seat+1,back_top=hy+8)
    env.rect(min(X(-9),X(6)),seat-1,max(X(-9),X(6)),seat,'red',0.2)      # подушка на стуле
    for off,sh in ((-2,-0.9),(0,0)):
        ch.rect(min(X(11+off),X(13+off)),seat,max(X(11+off),X(13+off)),seat+16,'skin',0.2+sh)
        ch.rect(min(X(11+off),X(13+off)),seat+13,max(X(11+off),X(13+off)),seat+15,'white',0.6+sh)
        ch.rect(min(X(10+off),X(15+off)),seat+16,max(X(10+off),X(15+off)),seat+17,'red',-0.6+sh)
    ch.poly([(X(-6),seat-5),(X(13),seat-5),(X(14),seat-2),(X(12),seat),(X(-6),seat)],'blue',-0.6)   # шорты/юбка
    ch.poly([(X(-4),hy+11),(X(4),hy+11),(X(6),hy+16),(X(5),seat-4),(X(-6),seat-4),(X(-5),hy+15)],top,0)
    ch.rect(min(X(-3),X(3)),hy+11,max(X(-3),X(3)),hy+11,top,0.9)
    for yy in range(hy+15,seat-4): ch.put(X(-5),yy,top,-0.8)
    head(ch,X(1),hy,f,hairr,'pony',expr,hairsh=hairsh)
    if arm=='reach':
        ch.line(X(1),hy+14,X(8),hy+17,top,-0.2,2)
        ch.line(X(8),hy+17,X(14),hy+11,'skin',0.2,2)
        ch.ell(X(15),hy+10,1.6,1.6,'skin',0.6); return (X(16),hy+9)
