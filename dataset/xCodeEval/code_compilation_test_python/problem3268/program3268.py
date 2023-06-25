def program3268():
    n, s = [int(x) for x in input().strip().split(" ")]
    s = 1, e = n + 1
    while(s < e):
        mid = (s+ e)/2
        if mid - sum(map(int, str(c))) < s:
            a = c + 1
        else:
            b = c
    print(n-a+1)