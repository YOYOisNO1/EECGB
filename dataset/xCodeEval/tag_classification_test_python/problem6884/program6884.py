def program6884():
    n, k= map(int, input().split())
    binom=1
    curNum=n
    curDeNum=1
    rem=0
    c=0
    while k>=0 and c<=n:
        c+=1
        k-=1
        rem=(rem+binom)%1000000007
        binom=(binom*curNum*pow(curDeNum, -1, 1000000007))%1000000007
        curNum-=1
        curDeNum+=1
    print(rem)