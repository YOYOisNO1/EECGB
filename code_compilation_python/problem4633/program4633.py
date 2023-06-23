    pl,pr,vl,vr,k = map(int,input().split())
    p,x = [0,1e9],0
def g(x):
        if x<1e9:
            p.append(x)
            g(10*x+4),g(10*x+7)
    g(4),g(7),p.sort()
def f(a,b,c,d): return max(0,min(b,d)-max(a,c)+1)
    for i in range(1,len(p)-k):
        q,r,s,t=p[i-1]+1,p[i],p[i+k-1],p[i+k]-1
        x+=f(q,r,vl,vr)*f(s,t,pl,pr)+f(q,r,pl,pr)*f(s,t,vl,vr)
        if k==1 and r>=max(vl,pl) and r<=min(vr,pr): x-=1
    print(1.*x/((pr-pl+1)*(vr-vl+1)))