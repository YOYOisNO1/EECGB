def program3996():
    import queue
    n = int(input().strip())
    
    graph = [[0]*n for _ in range(n)]
    for i in range(n-1):
        j = i + 1
        while j < n:
            graph[i][j] = i ^ j
            graph[j][i] = j ^ i
            j += 1
    INF = 10**9
    pq = queue.PriorityQueue()
    pq.put(0)
    dist = [INF]*n
    dist[0] = 0
    visited = [False]*n
    while not pq.empty():
        top = pq.get()
        visited[top] = True
        for neighbor_index in range(len(graph[top])):
            if not visited[neighbor_index] and graph[top][neighbor_index] < dist[neighbor_index]:
                dist[neighbor_index] = graph[top][neighbor_index]
                pq.put(neighbor_index)
    res = 0
    for d in dist:
        res += d
    print(res)