    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    k = int(input())
    a = list(input().rstrip())
    n = len(a)
    unused = [1] * k
    
    
def ng():
        print('IMPOSSIBLE')
        exit()
    
    
    try:
        for i in range(n):
            if a[i] == '?' and a[n - i - 1] != '?':
                a[i] = a[n - i - 1]
            if a[i] != '?':
                unused[ord(a[i]) - 97] = 0
    except IndexError:
        ng()
    
    for i in range(n):
        if a[i] != a[n - i - 1]:
            ng()
    
    for i in range(n // 2, n):
        if a[i] == '?':
            for cc in range(k - 1, -1, -1):
                if unused[cc]:
                    a[i] = a[n - i - 1] = chr(cc + 97)
                    unused[cc] = 0
                    break
            else:
                a[i] = a[n - i - 1] = 'a'
    
    if any(unused):
        ng()
    print(*a, sep='')