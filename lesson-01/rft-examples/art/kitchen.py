import math, random
from px import *
random.seed(7)
LX,LY=150,50   # лампа
env=Layer(); chars=Layer(); chars.dither=False; front=Layer(); front.dither=False
FLOOR=168
# ── стена
env.rect(0,0,W-1,FLOOR-1,'wall')
# плинтус
env.rect(0,FLOOR-4,W-1,FLOOR-1,'wood',-1.2)
env.rect(0,FLOOR-4,W-1,FLOOR-4,'wood',-0.4)
# ── пол: доски (горизонтальные швы с перспективой)
env.rect(0,FLOOR,W-1,H-1,'wood',0)
yy=FLOOR;step=4
while yy<H:
    env.rect(0,yy,W-1,yy,'wood',-0.9); yy+=step; step+=3
for i in range(-20,30):  # сходящиеся стыки досок
    x0=192+i*9
    for y in range(FLOOR,H):
        t=(y-FLOOR)/(H-FLOOR)
        x=192+(x0-192)*(1+t*2.2)
        if random.random()<0.75: env.put(x,y,'wood',-0.7)
# ── дверной проём и коридор
env.rect(18,40,94,FLOOR-1,'wood',-0.6)
env.rect(19,41,93,41,'wood',0.6)
env.rect(26,48,86,FLOOR-1,'hall',0)
env.rect(26,150,86,FLOOR-1,'hall',1)            # пол коридора
env.rect(26,148,86,149,'hall',-0.5)
env.rect(40,64,64,148,'hall',0.8)              # дальняя дверь
env.rect(41,65,63,147,'hall',0.3)
env.rect(42,147,62,147,'yel',-1.5)             # полоска света под дальней дверью
env.rect(60,104,61,106,'hall',2)               # ручка
for k,(x,y) in enumerate([(74,60),(80,60)]):   # вешалка с пальто
    env.rect(x,y,x+1,y+2,'hall',2)
env.poly([(70,63),(84,63),(86,110),(68,110)],'hall',1.4)
env.poly([(72,63),(82,63),(82,72),(72,72)],'hall',2.2)
# ── окно
WX0,WY0,WX1,WY1=196,36,256,102
env.rect(WX0-4,WY0-4,WX1+4,WY1+2,'wood',0.2)
for y in range(WY0,WY1+1):
    for x in range(WX0,WX1+1):
        t=(y-WY0)/(WY1-WY0)
        env.put(x,y,'sky',t*3.2)
# город
bx=WX0
random.seed(3)
while bx<WX1:
    w=random.randint(6,13);h=random.randint(14,40)
    env.rect(bx,WY1-h,min(bx+w,WX1),WY1,'hall',-1)
    for wy in range(WY1-h+3,WY1-2,4):
        for wx in range(bx+2,min(bx+w,WX1)-1,3):
            if random.random()<0.32: env.put(wx,wy,'city' if random.random()<.8 else 'city2')
    bx+=w+random.randint(0,2)
env.ell(246,46,3,3,'moon')
# переплёт
env.rect((WX0+WX1)//2-1,WY0,(WX0+WX1)//2+1,WY1,'wood',0)
env.rect(WX0,(WY0+WY1)//2-1,WX1,(WY0+WY1)//2,'wood',0)
env.rect(WX0-6,WY1+2,WX1+6,WY1+5,'wood',1)      # подоконник
env.rect(WX0-6,WY1+6,WX1+6,WY1+6,'wood',-1.5)
# цветок на подоконнике
env.rect(240,WY1-4,248,WY1+1,'red',0.5); env.rect(240,WY1-4,248,WY1-4,'red',1.5)
for dx,dy,h in [(-3,-14,0),(0,-18,1),(4,-13,0),(6,-9,1),(-5,-8,0)]:
    env.line(244,WY1-5,244+dx,WY1-5+dy,'green',h,1)
    env.ell(244+dx,WY1-5+dy,1.6,1.2,'green',h+0.5)
# ── кухонный гарнитур справа
env.rect(270,22,383,74,'teal',0)
for x0 in (272,302,332,360):
    env.rect(x0,24,x0+26,72,'teal',-0.9)
    env.rect(x0+2,26,x0+24,70,'teal',0.3)
    env.rect(x0+2,26,x0+24,26,'teal',1.2)
    env.rect(x0+20,46,x0+21,50,'white',1)
env.rect(270,74,383,75,'teal',-2)   # тень под шкафами
# фартук-плитка
env.rect(262,76,383,117,'tile',0)
for y in range(76,118):
    for x in range(262,384):
        if (y-76)%8==0 or (x-262+(5 if ((y-76)//8)%2 else 0))%10==0: env.put(x,y,'tile',-2.6)
        elif (y-76)%8==1: env.put(x,y,'tile',0.8)
# столешница и нижние шкафы
env.rect(258,116,383,121,'wood',0.6); env.rect(258,116,383,116,'wood',1.8); env.rect(258,121,383,121,'wood',-1)
env.rect(260,122,383,FLOOR-1,'teal',-0.3)
for x0 in (262,292,322,352):
    env.rect(x0,124,x0+27,FLOOR-6,'teal',-1)
    env.rect(x0+2,126,x0+25,FLOOR-8,'teal',0.2)
    env.rect(x0+12,130,x0+15,131,'white',1)
# чайник с паром
env.ell(300,108,8,7,'white',0.4,clip=lambda x,y:y>=102)
env.rect(293,110,307,115,'white',0.2)
env.rect(296,100,304,102,'white',0.8); env.rect(298,98,302,99,'white',1.4)
env.line(308,106,314,100,'white',0.2); env.line(291,104,288,110,'white',-1)
env.rect(293,115,307,115,'white',-1.2)
for (x,y,h) in [(315,97,1.4),(316,95,1.2),(316,93,1.0),(315,91,0.8),(314,89,0.6),(315,87,0.4),(317,85,0.2),(318,83,0)]:
    env.put(x,y,'white',h)
# банки на полке у плиты
for i,(x,c) in enumerate([(330,'red'),(340,'yel'),(350,'green')]):
    env.rect(x,105,x+6,115,c,-0.2); env.rect(x,104,x+6,105,'white',0.5); env.rect(x+1,107,x+1,113,c,1.2)
# ── картина/часы на стене
env.ell(110,66,8,8,'white',0.8); env.ell(110,66,6,6,'white',1.6)
env.line(110,66,110,61,'hair',-1); env.line(110,66,114,66,'hair',-1); env.put(110,66,'red',2)
# ── лампа
env.line(LX,0,LX,37,'hair',0)
env.poly([(LX-9,37),(LX+9,37),(LX+17,50),(LX-17,50)],'red',0)
env.rect(LX-8,38,LX+8,38,'red',1.5)
env.rect(LX-12,49,LX+12,51,'bulb')
# ── стол
TX0,TX1,TY=106,206,134
for lx in (118,190):
    env.rect(lx,TY+6,lx+4,FLOOR+20,'wood',-0.4); env.rect(lx+4,TY+6,lx+4,FLOOR+20,'wood',-1.4)
# ── персонажи
def head(L,cx,cy,f,hairr,style,expr,hairsh=0):
    # затылок/волосы сзади
    if style=='bob':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.rect(cx-f*8 if f>0 else cx+1,cy,cx-1 if f>0 else cx+f*-8,cy+6,hairr,hairsh-0.5)
    elif style=='long':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.poly([(cx-f*9,cy-2),(cx-f*2,cy-2),(cx-f*3,cy+18),(cx-f*10,cy+16)],hairr,hairsh-0.3)
    elif style=='pony':
        L.ell(cx-f*1,cy-1,8.5,8.5,hairr,hairsh)
        L.ell(cx-f*10,cy+5,3,6,hairr,hairsh-0.2)
        L.ell(cx-f*12,cy+11,2,3,hairr,hairsh-0.5)
        L.rect(cx-f*8,cy-1,cx-f*8+1*(-f if f<0 else 1)-(1 if f<0 else 0),cy,'yel',2.6)
    # лицо
    L.ell(cx+f*1,cy+1,6.8,7.6,'skin',0.6)
    L.ell(cx+f*1,cy+6,4.5,2.5,'skin',0.6)
    L.put(cx+f*8,cy+2,'skin',0.6)                         # нос
    L.put(cx-f*4,cy+7,'skin',-0.6); L.put(cx-f*3,cy+8,'skin',-0.6)   # тень скулы/челюсти
    # ухо
    L.put(cx-f*3,cy+2,'skin',-0.2); L.put(cx-f*3,cy+3,'skin',-0.6)
    # чёлка
    for x in range(-7,8):
        top=cy-8+int(abs(x)/3)
        bottom=cy-3 if style!='long' else cy-4
        if f*x>3: bottom=cy-5 if style=='bob' else cy-4
        if f*x<-3: bottom=cy+ (5 if style!='pony' else 1)
        for y in range(top,bottom+1): L.put(cx+x,y,hairr,hairsh+(0.8 if y==top else 0))
    # пряди-блики
    L.put(cx-f*2,cy-7,hairr,hairsh+2); L.put(cx-f*1,cy-7,hairr,hairsh+1.6); L.put(cx+f*1,cy-8,hairr,hairsh+1.2)
    e1,e2=cx+f*2,cx+f*6
    ey=cy+1
    if expr=='laugh':
        for ex in (e1,e2):
            L.put(ex-1,ey,'eye');L.put(ex,ey-1,'eye');L.put(ex+1,ey,'eye')
        mx=cx+f*4
        L.rect(mx-1,cy+5,mx+1,cy+6,'mouthd'); L.rect(mx-1,cy+5,mx+1,cy+5,'white',2.5); L.put(mx,cy+7,'mouth')
        L.put(e2+f*1,cy+4,'cheek'); L.put(e1-f*1,cy+4,'cheek')
    else:
        for ex in (e1,e2):
            L.put(ex,ey,'eye');L.put(ex,ey+1,'eye');L.put(ex+f*1 if f<0 else ex,ey,'white',3)
        L.put(e1-f*1,ey-2,hairr,hairsh-0.5); L.put(e2,ey-2,hairr,hairsh-0.5)
        L.put(cx+f*4,cy+6,'mouth'); L.put(cx+f*5,cy+6,'mouth')
        L.put(e1-f*1,cy+4,'cheek')
    L.rect(cx+f*1-1,cy+9,cx+f*1+1,cy+11,'skin',-0.3)   # шея
# ── сидящая фигура в профиль: цельная модель, стол потом закрывает её часть
def seated(cx,f,top,pants,hairr,style,hairsh,arm):
    X=lambda d:cx+f*d
    hy=100
    # стул: спинка, сиденье, ножки (за фигурой)
    env.rect(min(X(-11),X(-10)),112,max(X(-11),X(-10)),FLOOR+16,'wood',-0.2)
    env.rect(min(X(-12),X(-9)),110,max(X(-12),X(-9)),112,'wood',0.8)
    env.rect(min(X(-11),X(8)),153,max(X(-11),X(8)),155,'wood',0.3)
    env.rect(min(X(-11),X(8)),153,max(X(-11),X(8)),153,'wood',1.2)
    env.rect(min(X(7),X(8)),156,max(X(7),X(8)),FLOOR+16,'wood',-0.7)
    # голень, стопа (дальняя нога — темнее, чуть сзади)
    for off,sh in ((-2,-0.9),(0,0)):
        chars.rect(min(X(17+off),X(20+off)),150,max(X(17+off),X(20+off)),FLOOR+10,pants,psh_(pants)+sh)
        chars.rect(min(X(16+off),X(24+off)),FLOOR+11,max(X(16+off),X(24+off)),FLOOR+12,'hair',-0.3+sh)
    # бедро и таз
    chars.poly([(X(-8),146),(X(20),146),(X(22),149),(X(20),152),(X(-8),153)],pants,psh_(pants))
    chars.rect(min(X(-6),X(20)),146,max(X(-6),X(20)),146,pants,psh_(pants)+1.1)
    # торс (профиль, чуть наклонён к столу)
    chars.poly([(X(-5),111),(X(5),111),(X(7),117),(X(6),136),(X(7),146),(X(-8),147),(X(-7),126),(X(-6),116)],top,0)
    chars.rect(min(X(-4),X(4)),111,max(X(-4),X(4)),111,top,0.9)
    for yy in range(116,146): chars.put(X(-7) if f>0 else X(-7),yy,top,-0.8)
    # шея
    chars.rect(min(X(0),X(2)),108,max(X(0),X(2)),111,'skin',-0.3)
    head(chars,X(2),hy,f,hairr,style,'laugh',hairsh=hairsh)
    # рука
    if arm=='table':
        chars.line(X(1),114,X(5),127,top,-0.3,3)
        chars.line(X(5),127,X(17),131,top,0.1,3)
        chars.ell(X(20),131,2.2,1.8,'skin',0.6)
    else:
        chars.line(X(1),114,X(4),126,top,-0.3,3)
        chars.line(X(4),126,X(12),119,top,0.1,3)
        chars.ell(X(14),118,2.2,2,'skin',0.6)
def psh_(p): return {'hair':0.4,'blue':-1.6}.get(p,0)
mx,my=120,100
seated(mx,1,'blue','hair','hair','bob',1.4,'table')
fx,fy=192,100
seated(fx,-1,'mag','blue','blond','long',0.3,'phone')
# телефон в руке подруги
front.rect(fx-18,fy+12,fx-14,fy+20,'black'); front.rect(fx-17,fy+13,fx-15,fy+19,'screen')
# Лена (6) в дверях, смотрит вправо
lx,ly=60,113
chars.poly([(lx-7,ly+12),(lx+8,ly+12),(lx+13,ly+36),(lx-11,ly+36)],'yel',0.2)   # платье
chars.rect(lx-6,ly+12,lx+7,ly+13,'yel',0.9)
chars.rect(lx-2,ly+12,lx+3,ly+12,'yel',-1)
for xx in range(lx-10,lx+13,4): chars.put(xx,ly+36,'yel',-1.2)
chars.line(lx-7,ly+14,lx-10,ly+27,'skin',0.2,2)    # руки
chars.line(lx+8,ly+14,lx+9,ly+24,'skin',0.2,2)
# рисунок в руках
chars.rect(lx-2,ly+22,lx+13,ly+33,'white',1.2); chars.rect(lx-2,ly+33,lx+13,ly+33,'white',-0.5)
chars.ell(lx+2,ly+25,1.5,1.5,'yel',3)
chars.poly([(lx+5,ly+31),(lx+5,ly+27),(lx+8,ly+24),(lx+11,ly+27),(lx+11,ly+31)],'red',2)
chars.rect(lx+7,ly+28,lx+8,ly+31,'blue',2)
chars.ell(lx-2,ly+27,1.6,1.6,'skin',0.6); chars.ell(lx+13,ly+27,1.6,1.6,'skin',0.6)
# ноги
for dx in (-5,3):
    chars.rect(lx+dx,ly+37,lx+dx+2,ly+50,'skin',0.2)
    chars.rect(lx+dx,ly+48,lx+dx+2,ly+51,'white',0.5)
    chars.rect(lx+dx-1,ly+52,lx+dx+4,ly+54,'red',-0.6)
head(chars,lx,ly,1,'hair','pony','look',hairsh=0.6)
# тень Лены на полу
env.rect(lx-9,FLOOR+1,lx+11,FLOOR+2,'wood',-2.2)
env.rect(lx-6,FLOOR+3,lx+8,FLOOR+3,'wood',-1.8)
# ── стол сверху (перед людьми)
front.rect(TX0,TY,TX1,TY+5,'wood',0.4)
front.rect(TX0,TY,TX1,TY+1,'wood',1.3)
front.rect(TX0,TY+5,TX1,TY+5,'wood',-1.5)
front.rect(TX0+2,TY+6,TX1-2,TY+8,'wood',-0.9)
# тарелка с печеньем
front.ell(156,TY-1,11,2,'white',0.6); front.rect(146,TY,166,TY,'white',-0.4)
for x in (150,156,162): front.ell(x,TY-2,3,1.4,'wood',2.2); front.put(x-1,TY-3,'wood',3)
# кружки
for x,c in ((130,'white'),(178,'green')):
    front.rect(x,TY-6,x+5,TY-1,c,0.5); front.rect(x,TY-6,x+5,TY-6,c,1.5); front.rect(x+6,TY-5,x+7,TY-3,c,0)
    front.put(x+2,TY-9,'white',1.5); front.put(x+3,TY-11,'white',1)

# ── свет
PHX,PHY=fx-16,fy+16
def L(x,y):
    dx=x-LX;dy=y-LY
    d=math.hypot(dx,dy*(2.4 if dy<0 else 0.82))
    l=0.07+0.98*max(0,1-d/185)**1.45
    if 26<=x<=86 and 48<=y<FLOOR:      # коридор: свет перекрыт стеной
        l=0.04+0.12*max(0,(x-50)/36)*(1 if y>90 else 0.4)
    if y>=FLOOR and 108<=x<=204 and y<=FLOOR+22:    # тень под столом
        l*=0.45+0.55*abs(x-156)/50
    pd=math.hypot(x-PHX,y-PHY)
    if pd<16: l+=0.18*(1-pd/16)
    return l
def Lc(x,y):
    l=L(x,y)
    if 36<=x<=90 and 100<=y<=FLOOR+2 and chars.get(x,y) is not None:   # Лена освещена кухней
        l=0.42+0.22*(x-36)/54
    elif 100<=x<=212 and y>TY+8 and chars.get(x,y) is not None:          # ноги в тени стола
        l*=0.6
    return l
def rim(li,x,y):
    if li!=1: return False
    lay=chars
    sx=1 if x<LX else -1
    nb=lay.get(x+sx,y)
    return nb is None and lay.get(x,y) is not None and (x<90)
img=render([env,chars,front],Lc,rim=rim)
# свечение экрана телефона на лицах (холодный тинт)
px_=img.load()
for y in range(H):
    for x in range(W):
        pd=math.hypot(x-PHX,y-PHY)
        if pd<14 and chars.get(x,y) is not None and front.get(x,y) is None:
            r,g,b=px_[x,y];k=.35*(1-pd/14)
            px_[x,y]=(int(r*(1-k)+143*k),int(g*(1-k)+208*k),int(b*(1-k)+255*k))
img.save('kitchen_1x.png')
img.resize((W*5,H*5),Image.NEAREST).save('kitchen_5x.png')
print('ok')
