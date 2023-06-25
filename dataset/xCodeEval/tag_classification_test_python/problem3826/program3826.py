    n = int(input())
    cubics = [[0 for _ in range(10)] for __ in range(n)]
    for i in range(n):
        for v in [int(k) for k in input().split(' ') if k]:
            cubics[i][v] = 1
    allowed = [1 for _ in range(n)]
def build(v, i=0):
        if i >= len(v):
            return 1
        for j in range(n):
            if allowed[j] and cubics[j][v[i]]:
                allowed[j] = 0
                if build(v, i + 1):
                    allowed[j] = 1
                    return 1
                allowed[j] = 1
        return 0
    for i in range(1, 10 ** n):
        if not build([int(k) for k in str(i)]):
            print(i - 1)
            exit()
    print(10 ** n - 1)