import json,math
import numpy as np
D=json.load(open('lena-dump.json'));L=json.load(open('layout-final.json'))
W=D['W'];ORDER=[o[0] for o in D['ORDER']];steps=D['steps']
def jsh(s):
    h=0
    for c in s:h=(h*31+ord(c))&0xffffffff
    return h-(1<<32) if h>=1<<31 else h
T=np.linspace(.04,.96,40)
OUT={};left=[]
for lk,P in L.items():
    ss=[s for s in steps if s['lay']==lk]
    s=ss[-1];ex={};vis=0
    for x in ORDER:
        if s['exits'].get(x,'x-off')!='x-off':ex[x]=165+vis*55;vis+=1
    sc=max(t['edaK'] for t in ss)
    boxes=[]
    for i in s['nodes']:
        k=sc if i=='eda' else 1
        if i in ss[-1]['front']:k*=1.12
        boxes.append((i,P[i][0]-W[i][0]*k/2-9,P[i][1]-W[i][1]*k/2-7,P[i][0]+W[i][0]*k/2+9,P[i][1]+W[i][1]*k/2+7))
    for xx,yy in ex.items():boxes.append((xx,1262,yy-W['x:'+xx][1]/2-4,1265+W['x:'+xx][0],yy+W['x:'+xx][1]/2+4))
    def pt(a):return P[a] if a in s['nodes'] else (1278,ex[a])
    for key in s['edges']:
        a,b=key.split('>');A=pt(a);B=pt(b);dx=B[0]-A[0];dy=B[1]-A[1];l=math.hypot(dx,dy)
        def hits(bd):
            cx=(A[0]+B[0])/2-dy/l*bd;cy=(A[1]+B[1])/2+dx/l*bd
            X=(1-T)**2*A[0]+2*(1-T)*T*cx+T*T*B[0];Y=(1-T)**2*A[1]+2*(1-T)*T*cy+T*T*B[1]
            return sum(int(((X>x0)&(X<x1)&(Y>y0)&(Y<y1)).sum()) for i,x0,y0,x1,y1 in boxes if i not in(a,b))
        d0=(1 if jsh(key)%2 else -1)*min(26,l*.07)
        h0=hits(d0)
        if h0==0:continue
        best=min(((hits(bd),abs(bd-d0),bd) for bd in range(-160,161,8)))
        OUT.setdefault(lk,{})[key]=best[2]
        if best[0]:left.append((lk,key,best[0]))
print(json.dumps(OUT));print('left',left)
