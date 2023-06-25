def program5059():
    n,d=map(int,input().split())
    l=map(int,input().split())
    noj=0
    if(sum(l)+10*(len(l)-1)>d):
        noj=-1
    else:
        time=d-sum(l)
        noj=time/5
    print(noj)