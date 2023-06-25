def program1195():
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    r=0
    b=0
    for i in range (n):
        if(l1[i]==0 and l2[i]==1):
            b+=1
        elif(l1[i]==1 and l2[i]==0):
            r+=1
    if(r==0):
        print(-1)
    elif(r>b):
        print(1)
    else:
        if((b+1)%r==0):
            print((b+1)//r)
        else:
            print(((b+1)//r)+1)