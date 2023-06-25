def program997():
    n=int(input())
    z=list(map(int, input().split()))
    a1=z[0]
    a2=z[1]
    a3=z[2]
    z=list(map(int, input().split()))
    b1=z[0]
    b2=z[1]
    b3=z[2]
    
    d=a1
    e=a2
    f=a3
    
    minn=n
    maxn=max(min(a1, b2), 0)+max(min(a2, b3), 0)+max(min(a3,b1), 0)
    
    minn-=min(a1, b3)
    a1-=min(a1, b3)
    b3-=min(a1, b3)
    
    minn-=min(a1, b1)
    a1-=min(a1, b1)
    b1-=min(a1, b1)
    
    minn-=min(a2, b1)
    a2-=min(a2, b1)
    b1-=min(a2, b1)
    
    minn-=min(a2, b2)
    a2-=min(a2, b2)
    b2-=min(a2, b2)
    
    minn-=min(a3, b3)
    a3-=min(a3, b3)
    b3-=min(a3, b3)
    
    minn-=min(a3, b2)
    a3-=min(a3, b2)
    b2-=min(a3, b2)
    
    minn2=n
    b1=z[0]
    b2=z[1]
    b3=z[2]
    
    a1=d
    a2=e
    a3=f
    
    minn2-=min(a2, b1)
    a2-=min(a2, b1)
    b1-=min(a2, b1)
    
    minn2-=min(a2, b2)
    a2-=min(a2, b2)
    b2-=min(a2, b2)
    
    minn2-=min(a1, b1)
    a1-=min(a1, b1)
    b1-=min(a1, b1)
    
    minn2-=min(a1, b3)
    a1-=min(a1, b3)
    b3-=min(a1, b3)
    
    minn2-=min(a3, b3)
    a3-=min(a3, b3)
    b3-=min(a3, b3)
    
    minn2-=min(a3, b2)
    a3-=min(a3, b2)
    b2-=min(a3, b2)
    
    minn3=n
    b1=z[0]
    b2=z[1]
    b3=z[2]
    
    minn3-=min(a3, b3)
    a3-=min(a3, b3)
    b3-=min(a3, b3)
    
    minn3-=min(a3, b2)
    a3-=min(a3, b2)
    b2-=min(a3, b2)
    
    minn3-=min(a1, b1)
    a1-=min(a1, b1)
    b1-=min(a1, b1)
    
    minn3-=min(a1, b3)
    a1-=min(a1, b3)
    b3-=min(a1, b3)
    
    minn3-=min(a2, b1)
    a2-=min(a2, b1)
    b1-=min(a2, b1)
    
    minn3-=min(a2, b2)
    a2-=min(a2, b2)
    b2-=min(a2, b2)
    
    a1=d
    a2=e
    a3=f
    
    print(min(minn3, minn2, minn), maxn)