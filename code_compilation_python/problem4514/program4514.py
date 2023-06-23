    import sys
    from array import array  # noqa: F401
    
    
def input():
        return sys.stdin.buffer.readline().decode('utf-8')
    
    
    lines = [
        [0, 1, 2],
        [3, 4, 5, 6],
        [7, 8, 9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18],
        [0, 3, 7],
        [1, 4, 8, 12],
        [2, 5, 9, 13, 16],
        [6, 10, 14, 17],
        [11, 15, 18],
        [2, 6, 11],
        [1, 5, 10, 15],
        [0, 4, 9, 14, 18],
        [3, 8, 13, 17],
        [7, 12, 16]
    ]
    
    dp = [0] + [-1] * (1 << 19)
    
    
def dfs(state: int):
        if dp[state] != -1:
            return dp[state]
    
        for line in lines:
            for i in range(len(line)):
                line_bit = 0
                for j in range(i, len(line)):
                    line_bit |= 1 << line[j]
                    if state & line_bit == line_bit and dfs(state & ~line_bit) == 0:
                        dp[state] = 1
                        return 1
        dp[state] = 0
        return 0
    
    
    start_bit = 0
    for s in (0, 3, 7, 12, 16):
        for i, c in enumerate(input().split(), start=s):
            if c == 'O':
                start_bit |= 1 << i
    
    print('Karlsson' if dfs(start_bit) else 'Lillebror')