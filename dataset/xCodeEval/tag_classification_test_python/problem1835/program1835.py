    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    n = int(input())
    print(2 * n - n // 2)