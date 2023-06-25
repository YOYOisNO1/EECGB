def program2011():
    n=int(input())
    m=[int(k) for k in input().split(" ")]
    r=[int(k) for k in input().split(" ")]
    isok=[0]*n
    mx=720720
    for d in range(mx):
        for i in range(n):
        if (1+d)%m[i]==r[i]:
            isok[d]=1.0
            break
    print sum(isok)/n