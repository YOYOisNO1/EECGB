def program5025():
    from __future__ import division
    from sys import stdin
    
    a, b = [int(x) for x in stdin.readline().split()]
    mem = [[[1, 0] if j == 0 and i else [0, 0] for j in range(b + 2)] for i in range(a + 2)]
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            mem[i][j][0] = (i / (i + j)) + (j / (i + j)) * mem[i][j - 1][1]
            mem[i][j][1] = (j / (i + j)) * (
                    mem[i][j - 2][0] * ((j - 1) / (i + j - 1)) + mem[i - 1][j - 1][0] * (i / (i + j - 1)))
    
    print(mem[a][b][0])