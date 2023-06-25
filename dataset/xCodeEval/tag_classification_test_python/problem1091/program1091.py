def program1091():
    n=int(input())
    a1,a2,a3=map(int,input().split())
    b1,b2,b3=map(int,input().split())
    
    maxx=0
    
    maxx=maxx+min(a1,b2)
    maxx=maxx+min(a2,b3)
    maxx=maxx+min(a3,b1)
    
    minn=0
    
    if a1>(b1+b3):
        minn=max(minn,(a1-(b1+b3)))
        
    if a2>(b1+b2):
        minn=max(minn,(a2-(b1+b2)))
        
    if a3>(b2+b3):
        minn=max(minn,(a3-(b2+b3)))
        
    print(minn,maxx)    