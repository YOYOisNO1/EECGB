def program1144():
    r, c, n, k = list(map(int, input().split()))
    A = [2] * n
    for i in range(n):
        A[i] = list(map(int, input().split()))
    answer = 0
    for i1 in range(1, r + 1):
        for j1 in range(1, c + 1):
            for i2 in range(i1, r + 1):
                for j2 in range(j1, c + 1):
                    t = 0
                    for i in range(n):
                        if i1 <= A[i][0] <= i2 and j1 <= A[i][1] <= j2:
                            t += 1
                    answer += (t >= k)
    print(answer)