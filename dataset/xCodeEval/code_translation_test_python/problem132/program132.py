def exp(a,p,m):
        if(p==0):
            return 1
        elif(p==1):
            return a
        elif(p%2==0):
            x = exp(a,p>>1,m)
            return x*x
        else:
            return (a*exp(a,p-1,m))%m
def prog(s):
        l = len(s)
        x = int(s,2)%((10**9)+7)
        e = exp(2,l-1,(10**9)+7)
        return (x*e)%((10**9)+7)
    s = input()
    print(prog(s))