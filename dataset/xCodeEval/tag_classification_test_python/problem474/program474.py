    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    s = input().rstrip()
    a = [input().rstrip() for _ in range(10)]
    ans = []
    for i in range(8):
        for j in range(10):
            if s[i * 10:(i + 1) * 10] == a[j]:
                ans.append(j)
                break
    
    print(*ans, sep='')