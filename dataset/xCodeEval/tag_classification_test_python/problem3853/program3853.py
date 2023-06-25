    import sys, math
def get(a):
        if a!=-1:
            return(a)
        return(1000000000)
    n=int(input())
    z=list(map(int,input().split()))
    fir = [0 for i in range(n+1)] #отдых
    sec = [0 for i in range(n+1)] #контест
    th = [0 for i in range(n+1)] #трен
    sec[0]=-1
    th[0]=-1
    for i in range(n):
        if z[i]==0: #отдых
            fir[i+1]=min(fir[i]+1, get(sec[i])+1, get(th[i])+1)
            sec[i+1]=-1
            th[i+1]=-1
        elif z[i]==1: #контест
            fir[i+1]=min(fir[i]+1, get(sec[i])+1, get(th[i])+1)
            sec[i+1]=min(fir[i], get(th[i]))
            th[i+1]=-1
        elif z[i]==2:
            fir[i+1]=min(fir[i]+1, get(sec[i])+1, get(th[i])+1)
            sec[i+1]=-1
            th[i+1]=min(fir[i], get(sec[i]))
        else:
            fir[i+1]=min(fir[i]+1, get(sec[i])+1, get(th[i])+1)
            sec[i+1]=min(fir[i], get(th[i]))
            th[i+1]=min(fir[i], get(sec[i]))
    print(min(fir[-1],get(sec[-1]), get(th[-1])))