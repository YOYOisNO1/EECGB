def program3495():
    ricxvi,k=map(int, input().split())
    sum=ricxvi
    n=ricxvi
    while n>=k :
        sum=sum+n/k
        n=n/k+n%k
    print(sum)