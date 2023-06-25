def program3562():
    n, t = map(int, input().split())
    a = map(str, input())
    s = ""
    for i in range (0,t):
        j = 0
        while j+1 < n:
            k = j+1
            if a[j] == 'B' and a[k] == 'G':
                temp = a[j]
                a[j] = a[k]
                a[k] = temp
                j = j+2
            else:
                j = j+1
    for i in range(n):
        s = s+a[i]
    print(s)