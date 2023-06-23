def program671():
    n = int(input())
    a=list(map(int,input().split())
    ans = 1
    k = 1
    for i in a:
        if i:
            ans*=k
            k=1
        else:
            k+=1
    print(ans)