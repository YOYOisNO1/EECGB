def program5266():
    x,k=map(int,input().split())
    rem=1000000007
    if(x==0):
        print(0)
    else:
        print(((pow(2,k+1,rem)*(x%rem))%rem-(pow(2,k,rem)-1%rem)%rem)%rem)