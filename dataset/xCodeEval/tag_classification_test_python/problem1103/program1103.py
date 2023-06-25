    n=int(input())
    alice=tuple(map(int,input().split() ))
    bob=tuple(map(int,input().split() ))
def minimize(order):
        ag,ac,ap=alice
        bg,bc,bp=bob
        for j in order:
            if j==0:d=min(ag,bp);ag-=d;bp-=d
            elif j==1:d=min(ap,bc);ap-=d;bc-=d
            elif j==2:d=min(ac,bg);ac-=d;bg-=d
            elif j==3:d=min(ap,bp);ap-=d;bp-=d
            elif j==4:d=min(ag,bg);ag-=d;bg-=d
            else:d=min(ac,bc);ac-=d;bc-=d
        return ag+ac+ap
def maximize(f):
        ans=0
        ag,ac,ap=bob
        bg,bc,bp=alice
        
        d=min(ag,bp)
        ag-=d;bp-=d
        ans+=d
        
        d=min(ap,bc)
        ap-=d;bc-=d
        ans+=d
        
        d=min(ac,bg)
        ac-=d;bg-=d
        ans+=d
        return ans
    ans=n
    from itertools import permutations as pe
    for i in pe(list(range(6)),r=None):
        #rは長さ、Noneでiteraterの長さ
        ans=min(ans,minimize(i))
        
    print(ans,maximize(1))