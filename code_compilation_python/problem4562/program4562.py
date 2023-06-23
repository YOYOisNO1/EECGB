    x0, y0 = map(int, input().split())
    n = int(input())
    arr = [[x0, y0]]
    for i in range(0, n):
        x, y = map(int, input().split())
        arr.append([x, y])
    dist = [[0 for j in range(0, n+1)] for i in range(0, n+1)]
    for i in range(0, n+1):
        for j in range(0, n+1):
            dist[i][j] = (arr[i][0] - arr[j][0])**2 + (arr[i][1] - arr[j][1])**2
    # print(arr)
    # print(dist)
    
def dfs(status, memo):
        # if status in memo:
        #     return memo[status][0]
        if memo[status] != None:
            return memo[status][0]
        if status <= 0:
            return 1e8
        res = 1e8
        prev = []
        for i in range(1, n+1):
            if ((status >> i) & 1) == 0:
                continue
            next = status - (1 << i)
            temp = dfs(next, memo) + dist[0][i]*2
            if temp < res:
                res = temp
                prev = [i, 0]
            for j in range(1, n+1):
                if j == i:
                    continue
                if ((status >> j) & 1) == 0:
                    continue
                next = status - (1 << i) - (1 << j)
                temp = dfs(next, memo) + dist[0][j] + dist[j][i] + dist[i][0]
                if temp < res:
                    res = temp
                    prev = [i, j, 0]
        memo[status] = [res, prev]
        print(status, res)
        return res
    
    
    # memo = {1: [0, []]}
    memo = [None for i in range(0, 1 << 25)]
    memo[1] = [0, []]
    start = 1
    end = 1
    for i in range(1, n + 1):
        end += (1 << i)
    res = dfs(end, memo)
    path = [0]
    cur = end
    while cur > 1:
        prev = memo[cur][1]
        # if len(prev) == 2:
        path.extend(prev)
        for i in range(len(prev) - 1):
            cur -= (1 << prev[i])
    
    print(res)
    print(' '.join(map(str, path)))
    
    
    