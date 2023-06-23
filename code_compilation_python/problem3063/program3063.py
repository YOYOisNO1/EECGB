def program3063():
    t = int(input())
    i=0
    l =[]
    u = []
    ans= False
    for _ in range(t):
        n = list(map(int, input().split()))
        l.append(n[1])
        u.append(n[0])
        if n[1]%2 != n[0]%2:
            ans = True
    if sum(l)%2==0 and sum(u)%2==0:
        print("0")
    elif sum(l)%21=sum(u)%2:
        print("-1")
    else:
        if ans:
            print("1")
        else:
            print("-1")