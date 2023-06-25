def program3550():
    #!/usr/bin/env python3
    n = int(input())
    if n == 0:
        print(0, 0)
    else:
        acc = 0
        i = 1
        while acc + 6*i < n:
            acc += 6*i
            i += 1
        j = 0
        while acc + i*(j+1) < n:
            j += 1
        k = n - acc - i*j - 1
        dy = [ 0, 2,  2,  0, -2, -2 ]
        dx = [ 2, 1, -1, -2, -1,  1 ]
        y = dy[(j+1)%6] + dy[j]*(i-1) + dy[(j+2)%6]*k
        x = dx[(j+1)%6] + dx[j]*(i-1) + dx[(j+2)%6]*k
        print(x, y)