    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    s = input().rstrip()
    ans = s[0]
    suf = s[-1]
    s = s[1:-1]
    at_flag = 0
    
    while s:
        if s[:3] == 'dot':
            ans += '.'
            s = s[3:]
        elif not at_flag and s[:2] == 'at':
            ans += '@'
            at_flag = 1
            s = s[2:]
        else:
            ans += s[0]
            s = s[1:]
    
    print(ans + suf)