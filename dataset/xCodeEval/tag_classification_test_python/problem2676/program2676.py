def program2676():
    
    from sys import stdin
    d1,d2,d3=map(int,stdin.readline().strip().split())
    ans=0
    if(d1>=(d2+d3)):
        ans=2*(d2+d3)
    elif(d2>=(d1+d3)):
        ans=2*(d1+d3)
    elif(d3>=(d1+d2)):
        ans=2*(d1+d2)
    elif(d3<(d1+d2)):
        ans=d1+d3+d2
    print(ans)