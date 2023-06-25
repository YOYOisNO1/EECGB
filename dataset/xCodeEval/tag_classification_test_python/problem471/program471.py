def program471():
    n=int(input())
    w=list(map(int,input().split()))
    d={}
    for i in w:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    if(n==1):
        print('NO')
    elif(w.count(100)==0):
        if(w.count(200)%2==0):
            print('YES')
        else:
            print('NO')
    elif(w.count(200)==0):
        if(w.count(100)%2==0):
            print('YES')
        else:
            print('NO')
    elif(sum(w)%200==0):
        print('YES')
    else:
        print('NO')