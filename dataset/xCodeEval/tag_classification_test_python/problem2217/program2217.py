    import sys
    input = sys.stdin.readline
    
    n,x=map(int,input().split())
    
    LEN=len(str(x))
    
    if LEN==n:
        print(0)
        exit()
    elif LEN>n:
        print(-1)
        exit()
    
    from functools import lru_cache
    @lru_cache(maxsize=None)
def calc(x,n):
        #print(x)
    
        if len(str(x))==n:
            return 0
    
        A=[]
    
        for s in str(x):
            A.append(int(s))
    
        A=set(A)
    
        ANS=1<<60
    
        for a in A:
            if a<=1:
                continue
            else:
                ANS=min(ANS,1+calc(x*a,n))
        return ANS
    
    ANS=calc(x,n)
    
    if ANS==1<<60:
        print(-1)
    else:
        print(ANS)
        