def program465():
    n=input()
    arr=map(int,input().split())
    pos=0
    neg=0
    for i in arr:
        if(i>0):
            pos+=1
        elif(i<0):
            neg+=1
    req=n/2
    if(n%2==1):
        req+=1
    # print(req,pos,neg)
    if(pos>=req):
        print(1)
    elif(neg>=req):
        print(-1)
    else:
        print(0)