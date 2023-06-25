    import sys     
    import math as mt
    import bisect
    input=sys.stdin.readline
    #t=int(input())
    t=1
def ncr_util():
        inv[0]=inv[1]=1
        fact[0]=fact[1]=1
        for i in range(2,300001):
            inv[i]=(inv[i%p]*(p-p//i))%p
        for i in range(1,300001):
            inv[i]=(inv[i-1]*inv[i])%p
            fact[i]=(fact[i-1]*i)%p
def solve(d1,d2):
        ans1,ans2=0,0
        for i in ['R','S','P']:
            x=0
            for j in ['R','S','P']:
                if win[i]!=j:
                    x+=d2[j]
            ans1+=min(d1[i],x)
            for j in ['R','S','P']:
                if win[i]==j:
                    ans2+=min(d1[i],d2[j])
        return [n-ans1,ans2]        
            
        
        
        
        
    for _ in range(t):
        n=int(input())
        
        #n,m=(map(int,input().split()))
        #n1=n
        #a=int(input())
        #b=int(input())
        #a,b,c,r=map(int,input().split())
        #x2,y2=map(int,input().split())
        a1,a2,a3=map(int,input().split())
        b1,b2,b3=map(int,input().split())
        d1={}
        d1['R']=a1
        d1['S']=a2
        d1['P']=a3
        
        d2={}
        d2['R']=b1
        d2['S']=b2
        d2['P']=b3
        
            
        win={}
        win['R']='S'
        win['S']='P'
        win['P']='R'
        #n=int(input())
        #s=input()
        #s1=input()
        #p=input()
        #l=list(map(int,input().split()))
        #l2=list(map(int,input().split()))
        #l=str(n)
        #l.sort(reverse=True)
        #l2.sort(reverse=True)
        #l1.sort(reverse=True)
        print(*solve(d1,d2))
        
        
        