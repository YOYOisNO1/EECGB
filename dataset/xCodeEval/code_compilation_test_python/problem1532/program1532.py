    d={}
def c(n):
        t=d.get(n,(0,0))
        if t!=(0,0): return t
        if n<8: return n,n
        t=int(n**(1/3)+1.e-9)
        v1=c(n-t*t*t)
        v1=v1[0]+1,v1[1]+t*t*t
        v2=c(t*t*t-1)
        if v2>v1: v1=v2
        d[n]=v1
        return v1
        
    print(' '.join(map(str,c(int(input())))))