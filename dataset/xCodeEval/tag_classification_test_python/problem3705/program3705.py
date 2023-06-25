def program3705():
    n,m=map(int,input().split())
    lPoint = map(int,input().split())
    lPoint = sorted(enumerate(lPoint),key=lambda x:x[1])
    lAns = [-1] * n
    x=0
    for i,t in lPoint:
        lAns[i]=x
        x^=1
    #print(lAns)
    print(" ").join(map(str,lAns))