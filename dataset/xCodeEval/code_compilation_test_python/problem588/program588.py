def program588():
    n = int(input())
    a = map(int,input().split())
    s = sum(a)
    a.sort()
    for i in range(n//2):
    print(a[i],s*2//n-a[i])