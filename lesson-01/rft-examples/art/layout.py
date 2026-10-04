"""Подбор раскладки сети Лены по событиям (без наложений слов и без линий поверх слов).
Вход: lena-dump.json (снимается со страницы скриптом dump.py), выход: JSON для const LAYOUT в index.html.
Запуск: python3 layout.py lena-dump.json > layout.json"""
import json,sys,math,random
import numpy as np
D=json.load(open(sys.argv[1]))
steps=D['steps'];W=D['W'];NODES=D['NODES'];ORDER=[o[0] for o in D['ORDER']]
EXIT_Y0,EXIT_DY,EXIT_X=165,55,1272
MODE=sys.argv[3] if len(sys.argv)>3 else 'all'
SEED=int(sys.argv[4]) if len(sys.argv)>4 else 7
random.seed(SEED);np.random.seed(SEED)
def jsh(s):
    h=0
    for c in s:h=(h*31+ord(c))&0xffffffff
    return h-(1<<32) if h>=1<<31 else h
KEYS=[str(k) for k in range(1,12)]+['core','free']
EDA={2:(430,610),3:(440,600),4:(470,590),5:(550,560),6:(610,530),7:(665,505),8:(700,485)}
EARLY={'1':{'polnota':(560,430),'smeshno':(760,340),'obsuzh':(800,440),'brosayut':(740,540)},
       '2':{'polnota':(540,420),'smeshno':(740,330),'obsuzh':(800,430),'brosayut':(720,530)}}
def last(key):
    idx=[i for i,s in enumerate(steps) if s['lay']==key];return [steps[i] for i in idx]
out={};prev={};FINAL={}
ORDER_KEYS=['10']+[k for k in KEYS if k!='10']
if MODE=='final':ORDER_KEYS=['10']
if MODE.startswith('free:'):
    out.update(json.load(open(MODE[5:])));FINAL={i:tuple(v) for i,v in out['10'].items()};ORDER_KEYS=['free']
if MODE.startswith('rest:'):
    out['10']=json.load(open(MODE[5:]))['10'];FINAL={i:tuple(v) for i,v in out['10'].items()};ORDER_KEYS=[k for k in KEYS if k!='10']
for key in ORDER_KEYS:
    ss=last(key)
    if not ss:continue
    s=ss[-1]
    ids=[i for i in s['nodes']]
    scale={i:1.0 for i in ids}
    for t in ss:
        for i in t['front']:scale[i]=max(scale.get(i,1),1.12)
        if 'eda' in ids:scale['eda']=max(scale['eda'],t['edaK']*(1.12 if 'eda' in t['front'] else 1))
    # выходы
    ex={};vis=0
    for x in ORDER:
        v=s['exits'].get(x,'x-off')
        if v!='x-off':ex[x]=EXIT_Y0+vis*EXIT_DY;vis+=1
    edges=[k.split('>') for k in s['edges']]
    # подсказки
    hint={}
    for i in ids:
        h=FINAL.get(i) or (NODES[i][1],NODES[i][2])
        if key in EARLY and i in EARLY[key]:h=EARLY[key][i]
        hint[i]=h
    if key=='11':prev={i:tuple(v) for i,v in out['10'].items()}
    if key=='free':prev={i:tuple(v) for i,v in out['core'].items()}
    if key not in('10','11','core','free'):
        kk=int(key);prv=[str(j) for j in range(kk-1,0,-1) if str(j) in out]
        prev={i:tuple(v) for i,v in out[prv[0]].items()} if prv else {}
    k=int(key) if key.isdigit() else 99
    if 'eda' in ids:hint['eda']=EDA.get(k,(700,485))
    if key=='core':
        c=prev['eda']
        for i in ids:
            if i!='eda' and not i.startswith('st_'):hint[i]=(c[0]+(prev[i][0]-c[0])*.86,c[1]+(prev[i][1]-c[1])*.86)
    fixed=set()
    if key!='10':fixed|={i for i in ('ya','somnoy') if i in ids}
    if key=='11':fixed|=set(ids)
    if key=='free':fixed|={i for i in ids if not i.startswith('st_')}
    for i in ids:
        if i.startswith('st_'):pass
    move=[i for i in ids if i not in fixed]
    P={i:list(prev.get(i) or hint[i]) for i in ids}
    for i in ids:
        if i in fixed:P[i]=list(prev[i] if key in('free','11') else (FINAL.get(i) or prev[i]))
    W_H=0.0 if key=='10' else (0.003 if key=='core' else 0.012)
    W_C=0.0 if key in('10','core') else 0.004
    if key=='free':
        tgt={'st_wed':'ya','st_promo':'ocenki','st_boss':'oshibka','st_date':'vstrecha','st_eve':'odin'}
        for i in ids:
            if i.startswith('st_'):P[i]=[P[tgt[i]][0]+random.choice([-1,1])*60,P[tgt[i]][1]+random.choice([-1,1])*60];hint[i]=tuple(P[tgt[i]])
    wh={i:(W[i][0]*scale[i],W[i][1]*scale[i]) for i in ids}
    xw={x:W['x:'+x] for x in ex}
    names=ids+['x:'+x for x in ex]
    def boxes(P):
        B=[]
        for i in ids:
            w,h=wh[i];B.append((P[i][0]-w/2,P[i][1]-h/2,P[i][0]+w/2,P[i][1]+h/2))
        for x in ex:
            w,h=xw[x];B.append((1265,ex[x]-h/2,1265+w,ex[x]+h/2))
        return np.array(B)
    def pt(P,a):
        return P[a] if a in P else (EXIT_X+6,ex[a])
    T=np.linspace(0.04,0.96,26)
    def curves(P):
        S=[];own=[]
        for a,b in edges:
            A=pt(P,a);B=pt(P,b);dx=B[0]-A[0];dy=B[1]-A[1];L=math.hypot(dx,dy) or 1
            bend=(1 if jsh(a+'>'+b)%2 else -1)*min(26,L*.07)
            cx=(A[0]+B[0])/2-dy/L*bend;cy=(A[1]+B[1])/2+dx/L*bend
            xs=(1-T)**2*A[0]+2*(1-T)*T*cx+T*T*B[0];ys=(1-T)**2*A[1]+2*(1-T)*T*cy+T*T*B[1]
            S.append(np.stack([xs,ys],1));own.append((a,b))
        return S,own
    idx={nm:j for j,nm in enumerate(names)}
    SHARE=np.array([[bool({a,b}&{c,d}) for c,d in edges] for a,b in edges]) if edges else np.zeros((0,0),bool)
    def cost(P,detail=False):
        Bx=boxes(P);c=0.;rep=[]
        # наложения слов
        pad=np.array([-22,-14,22,14])
        Bi=Bx+pad*.5
        n=len(Bx)
        ox=np.minimum(Bi[:,None,2],Bi[None,:,2])-np.maximum(Bi[:,None,0],Bi[None,:,0])
        oy=np.minimum(Bi[:,None,3],Bi[None,:,3])-np.maximum(Bi[:,None,1],Bi[None,:,1])
        ov=np.clip(ox,0,None)*np.clip(oy,0,None);np.fill_diagonal(ov,0)
        o=ov.sum()/2;c+=o*30
        if detail and o>0:
            for a in range(n):
                for b in range(a+1,n):
                    if ov[a,b]>0:rep.append(('OVER',names[a],names[b]))
        # линии поверх слов
        S,own=curves(P)
        Bp=Bx+np.array([-8,-6,8,6])
        for (a,b),pts in zip(own,S):
            inside=(pts[:,None,0]>Bp[None,:,0])&(pts[:,None,0]<Bp[None,:,2])&(pts[:,None,1]>Bp[None,:,1])&(pts[:,None,1]<Bp[None,:,3])
            cnt=inside.sum(0)
            for nm in (a,b):
                j=idx.get(nm) if nm in idx else idx.get('x:'+nm)
                if j is not None:cnt[j]=0
            h=cnt.sum();c+=h*1500
            if detail and h:rep+=[('EDGE',a+'>'+b,names[j]) for j in np.nonzero(cnt)[0]]
        # пересечения линий (по 8 отрезкам на связь)
        if S:
            Q=[p[::3] for p in S]
            segs=np.concatenate([np.stack([p[:-1],p[1:]],1) for p in Q])
            eid=np.concatenate([np.full(len(p)-1,k) for k,p in enumerate(Q)])
            p1=segs[:,0];d=segs[:,1]-p1
            def cr(u,v):return u[...,0]*v[...,1]-u[...,1]*v[...,0]
            r=p1[None,:]-p1[:,None]
            den=cr(d[:,None],d[None,:])
            with np.errstate(divide='ignore',invalid='ignore'):
                t=cr(r,d[None,:])/den;u=cr(r,d[:,None])/den
            X=(t>0.01)&(t<0.99)&(u>0.01)&(u<0.99)&~SHARE[eid[:,None],eid[None,:]]
            nx=int(np.triu(X).sum());c+=nx*15
            if detail:rep.append(('CROSS',nx))
        # границы
        lo_x=228 if True else 0
        for j,i in enumerate(ids):
            x0,y0,x1,y1=Bx[j]
            if i.startswith('st_'):c+=(max(0,20-x0)+max(0,x1-1215)+max(0,150-y0)+max(0,y1-784))*200;continue
            c+=(max(0,lo_x-x0)+max(0,x1-1215)+max(0,150-y0)+max(0,y1-784))*200
        # подсказки, непрерывность, длина связей
        for i in ids:
            h=hint[i];c+=W_H*((P[i][0]-h[0])**2+(P[i][1]-h[1])**2)
            if i=='eda':c+=0.2*((P[i][0]-h[0])**2+(P[i][1]-h[1])**2)
            if i in prev:c+=W_C*((P[i][0]-prev[i][0])**2+(P[i][1]-prev[i][1])**2)
        for a,b in edges:
            A=pt(P,a);B=pt(P,b);c+=W_L*math.hypot(A[0]-B[0],A[1]-B[1])
        return (c,rep) if detail else c
    W_L=0.3 if key=='10' else 0.05
    cur=cost(P);best=(cur,{i:list(v) for i,v in P.items()})
    N=(int(sys.argv[2]) if len(sys.argv)>2 else 5000)*(3 if key=='10' else 1)
    for it in range(N if move else 0):
        temp=60*(1-it/N)+0.5;sig=55*(1-it/N)+3
        i=random.choice(move)
        if False:pass
        else:
            old=P[i][:];P[i][0]+=random.gauss(0,sig);P[i][1]+=random.gauss(0,sig*.8)
        c2=cost(P)
        if c2<cur or random.random()<math.exp((cur-c2)/temp):
            cur=c2
            if cur<best[0]:best=(cur,{j:list(v) for j,v in P.items()})
        else:P[i]=old
    P=best[1];c,rep=cost(P,True)
    print(key,round(c),[r for r in rep if r[0]!='CROSS'],[r for r in rep if r[0]=='CROSS'],file=sys.stderr)
    out[key]={i:[round(v[0]),round(v[1])] for i,v in P.items()}
    if key=='10':FINAL={i:tuple(v) for i,v in P.items()}
    prev={i:tuple(v) for i,v in P.items()}
print(json.dumps({k:out[k] for k in KEYS if k in out},ensure_ascii=False))
