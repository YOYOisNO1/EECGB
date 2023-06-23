def program728():
    n = int(input())
    t = list(map(int, input().split()))
    print(t)
    pa,pb = t.index(1), t.index(n)]
    if (pa+1 == 1 and pb+1 == n) or (pb+1 == 1 and pa+1 == n):
        print(n-1)
    else:
        if pa < pb:
            print(n-pa-1 if n-1-pb > pa else pb - 1)
        else:
            print(n-pb-1 if n-1-pa > pb else pa - 1)