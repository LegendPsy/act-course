# Коллаж «Это Лена» (6 лет): 9 сцен-выходов. Холст 300×174, панели 96×54.
import px
px.W,px.H=300,174
from lena_lib import *
import lena_lib
W,H=px.W,px.H
PW,PH,G=96,54,4
def O(i): return (2+(i%3)*(PW+G), 2+(i//3)*(PH+G))
bg=px.Layer(); ch=px.Layer(); ch.dither=False; fr=px.Layer(); fr.dither=False
def R(i,x0,y0,x1,y1,ramp,sh=0,L=bg): ox,oy=O(i); L.rect(ox+x0,oy+y0,ox+x1,oy+y1,ramp,sh)
def E(i,cx,cy,rx,ry,ramp,sh=0,L=bg): ox,oy=O(i); L.ell(ox+cx,oy+cy,rx,ry,ramp,sh)
def P(i,x,y,ramp,sh=0,L=fr): ox,oy=O(i); L.put(ox+x,oy+y,ramp,sh)
def Hd(i,cx,cy,f,hair,style,expr,hs=0.6): ox,oy=O(i); head(ch,ox+cx,oy+cy,f,hair,style,expr,hairsh=hs)
def body(i,cx,top,f,col,w=7,h=30,sh=0):
    ox,oy=O(i); h=min(h,PH-1-top); ch.poly([(ox+cx-w,oy+top),(ox+cx+w,oy+top),(ox+cx+w+3,oy+top+h),(ox+cx-w-3,oy+top+h)],col,sh)
    ch.rect(ox+cx-w+1,oy+top,ox+cx+w-1,oy+top,col,sh+0.9)
LENA=lambda i,cx,cy,f,expr: Hd(i,cx,cy,f,'hair','pony',expr,0.6)

# 1 РИСОВАТЬ — комната, стол, бумага, мелки
i=0; R(i,0,0,95,53,'wall',0.3); R(i,0,40,95,53,'wood',0.6); R(i,0,40,95,40,'wood',1.6)
body(i,36,30,1,'yel'); LENA(i,36,19,1,'down')
R(i,40,37,74,44,'white',1.6,fr); R(i,40,44,74,44,'white',0.2,fr)
E(i,46,39,1.5,1.5,'yel',3,fr); 
ox,oy=O(i)
fr.poly([(ox+56,oy+43),(ox+56,oy+40),(ox+60,oy+37),(ox+64,oy+40),(ox+64,oy+43)],'red',2.2); fr.rect(ox+59,oy+41,ox+60,oy+43,'blue',2)
for k,c in enumerate(['red','blue','green','yel']): R(i,78+k*3,41,79+k*3,46,c,2,fr)
ch.line(ox+44,oy+33,ox+54,oy+38,'skin',0.3,2); R(i,54,36,55,39,'red',2.5,fr)
# 2 ИГРАТЬ С ДРУЗЬЯМИ — двор, мяч
i=1
for y in range(0,36): R(i,0,y,95,y,'daysky',4.2-y/36*2.2)
R(i,0,36,95,53,'green',1.2); 
for x in range(0,96,5): P(i,x,36,'green',2.4,bg)
E(i,10,30,7,9,'green',0.6); R(i,9,30,11,36,'wood',0.8)
body(i,34,30,1,'yel'); LENA(i,34,20,1,'laugh')
body(i,64,30,-1,'blue'); Hd(i,64,20,-1,'hair','short','laugh',3.2)
E(i,50,8,4,4,'red',2.4,fr); P(i,49,6,'white',3); P(i,51,10,'white',2)
ch.line(O(i)[0]+40,O(i)[1]+33,O(i)[0]+46,O(i)[1]+24,'skin',0.4,2)
# 3 БАССЕЙН — вода, круг
i=2
for y in range(0,54): R(i,0,y,95,y,'daysky',2.8-y/54*1.2) if y<14 else None
R(i,0,0,95,13,'tile',4.2); 
for x in range(0,96,8): R(i,x,0,x,13,'tile',2.6)
R(i,0,14,95,53,'blue',2.8)
body(i,48,30,1,'yel',6,10); LENA(i,48,22,1,'laugh')
for y in range(31,54):
    for x in range(0,96):
        if (x+ (y//3)*5)%14<9: P(i,x,y,'blue',3.4 if y%3==0 and x%7<3 else 2.8,fr)
ox,oy=O(i)
fr.ell(ox+48,oy+32,15,4,'red',2.6); 
for dx in (-12,-4,4,12): fr.rect(ox+48+dx,oy+29,ox+48+dx+2,oy+35,'white',2)
fr.ell(ox+48,oy+32,9,1.6,'blue',2.8)
for (x,y) in [(30,26),(28,22),(68,25),(70,21),(66,18)]: P(i,x,y,'white',3)
# 4 ФОТОГРАФИРОВАТЬСЯ — видоискатель, вспышка
i=3; R(i,0,0,95,53,'mag',4.6)
for y in range(0,54,6): R(i,0,y,95,y,'mag',5.2)
body(i,48,32,1,'yel'); LENA(i,46,22,1,'smile')
ox,oy=O(i)
ch.line(ox+56,oy+36,ox+60,oy+26,'skin',0.4,2); ch.rect(ox+59,oy+20,ox+59,oy+25,'skin',0.6); ch.rect(ox+62,oy+20,ox+62,oy+25,'skin',0.6)
for (x,y,dx,dy) in [(4,4,1,1),(91,4,-1,1),(4,49,1,-1),(91,49,-1,-1)]:
    for k in range(7): P(i,x+dx*k,y,'white',3); P(i,x,y+dy*k,'white',3)
E(i,84,12,1.6,1.6,'red',4,fr); 
for (x,y) in [(14,12),(16,10),(18,12),(16,14),(16,12)]: P(i,x,y,'yel',5)
# 5 ЕСТЬ, ЧТО ХОЧЕТСЯ — мороженое
i=4; R(i,0,0,95,53,'yel',4.4)
for x in range(0,96,10): R(i,x,0,x+4,53,'yel',5)
body(i,40,32,1,'blue',7,30,0.6); LENA(i,40,22,1,'laugh')
ox,oy=O(i)
fr.poly([(ox+56,oy+30),(ox+64,oy+30),(ox+60,oy+44)],'wood',3.2)
for k in range(3): fr.line(ox+57+k*2,oy+31,ox+60,oy+40,'wood',2.2)
E(i,60,26,5,5,'mag',5.2,fr); E(i,60,22,4,3,'white',5,fr)
for (x,y,c) in [(58,25,'blue'),(62,27,'yel'),(61,23,'red'),(57,28,'green')]: P(i,x,y,c,4)
ch.ell(ox+57,oy+38,2,2,'skin',0.6)
# 6 ВЛЮБЛЯТЬСЯ — мальчик, сердечко
i=5
for y in range(0,54): R(i,0,y,95,y,'daysky',3.6-y/54*1.6)
R(i,0,44,95,53,'green',1.4)
body(i,28,32,1,'yel'); LENA(i,28,22,1,'smile')
body(i,72,32,-1,'blue'); Hd(i,72,22,-1,'hair','short','smile',3.2)
ox,oy=O(i)
for (x,y) in [(-3,0),(-2,-1),(-1,-1),(0,0),(1,-1),(2,-1),(3,0),(-3,1),(3,1),(-2,2),(2,2),(-1,3),(1,3),(0,4),(-2,0),(-1,0),(1,0),(2,0),(-2,1),(-1,1),(0,1),(1,1),(2,1),(-1,2),(0,2),(1,2),(0,3)]:
    fr.put(ox+50+x,oy+10+y,'heart')
P(i,48,9,'heart2',0)
for (x,y) in [(33,25),(34,25)]: P(i,x,y,'cheek',0,ch)
# 7 МЕЧТАТЬ — облачко-мысль: щенок и крестик ветеринара
i=6
for y in range(0,54): R(i,0,y,95,y,'daysky',2.4+y/54*1.4)
body(i,22,36,1,'yel'); LENA(i,22,28,1,'up')
for (x,y,r) in [(36,20,1.6),(42,15,2.4)]: E(i,x,y,r,r,'white',5,fr)
E(i,68,18,22,14,'white',5,fr)
E(i,62,18,6,5,'wood',4.6,fr); E(i,56,15,2,4,'wood',3.0,fr); E(i,68,15,2,4,'wood',3.0,fr)
P(i,60,17,'eye',0); P(i,64,17,'eye',0); R(i,61,20,63,21,'eye',0,fr); P(i,62,22,'mouth',0)
R(i,78,12,80,22,'green',5,fr); R(i,74,16,84,18,'green',5,fr)
# 8 ОТДЫХАТЬ — кровать, одеяло, Z
i=7; R(i,0,0,95,53,'sky',3.6)
R(i,62,6,86,22,'wood',1.4); R(i,64,8,84,20,'sky',4.4); E(i,80,11,2,2,'moon',0)
E(i,40,30,18,6,'white',4.4); 
LENA(i,34,26,1,'sleep')
R(i,8,34,95,53,'blue',3.4,fr); R(i,8,34,95,34,'blue',4.6,fr)
for y in range(38,54,6): R(i,8,y,95,y,'blue',2.6,fr)
ox,oy=O(i)
for (x,y,n) in [(54,10,4),(61,4,3)]:
    for k in range(n+1): fr.put(ox+x+k,oy+y,'white',5); fr.put(ox+x+k,oy+y+n,'white',5); fr.put(ox+x+n-k,oy+y+k,'white',5)
# 9 ПОПРОСИТЬ ПОДДЕРЖКИ — мама обнимает
i=8; R(i,0,0,95,53,'wall',0.9)
for y in range(0,54,9): R(i,0,y,95,y,'wall',0.4)
body(i,62,30,-1,'blue',9,30); Hd(i,62,18,-1,'hair','bob','sleep',1.4)
body(i,40,34,1,'yel',6,24); LENA(i,40,25,1,'sleep')
ox,oy=O(i)
ch.line(ox+56,oy+34,ox+36,oy+38,'blue',0.6,4); ch.ell(ox+34,oy+38,2,2,'skin',0.6)
E(i,76,8,1.8,1.8,'red',3.5,fr)

def L(x,y):
    c=min(2,(x-2)//(PW+G)); r=min(2,(y-2)//(PH+G)); i=r*3+c
    lx,ly=(x-2)%(PW+G),(y-2)%(PH+G)
    key={0:(70,0),1:(48,0),2:(48,0),3:(48,10),4:(48,10),5:(48,0),6:(30,0),7:(40,26),8:(60,0)}[i]
    amb={7:0.5}.get(i,0.6)
    d=math.hypot(lx-key[0],ly-key[1]);return amb+0.35*max(0,1-d/90)
img=render([bg,ch,fr],L)
pp=img.load()
FRAME=(16,14,20)
for y in range(H):
    for x in range(W):
        lx,ly=(x-2)%(PW+G),(y-2)%(PH+G)
        if x<2 or y<2 or x>=W-2 or y>=H-2 or lx>=PW or ly>=PH: pp[x,y]=FRAME
img.save('collage_1x.png'); img.resize((W*5,H*5),Image.NEAREST).save('collage_5x.png')
print('ok',W,H)
