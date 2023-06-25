def program2857():
    n,k = map(int, input().split(" "))
    a = map(int, input().split(" "))
    ans = 0
    a.sort(reverse=True)
    for i in a:
        if k%i==0:
            ans=k/i
            break
    print(ans)