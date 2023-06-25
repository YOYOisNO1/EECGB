def program1441():
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(input().split())
    s = '#Black&White'
    for i in range(n):
        for j in range(m):
            if ord(a[i][j]) == ord('C') or ord(a[i][j]) == ord('M') or ord(a[i][j]) == ord('Y'):
                s = '#Color'
    print(s)