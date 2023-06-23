    n = int(input())
    
    ps = map(lambda x: int(x) - 1, input().split())
    
    
    shortest_paths = [None] * n
    vertex_left = n
    
def dfs():
        global vertex_left
        visited = []
        queue = [(0, -1)]
        while queue:
            vtx, prev_steps = queue.pop(0)
            if vtx in visited:
                continue
            visited.append(vtx)
            shortest_paths[vtx] = prev_steps + 1
            vertex_left -= 1
            if vertex_left == 0:
                return
            nei = filter(lambda x: x != vtx and 0 <= x < n, [vtx - 1, vtx + 1, ps[vtx]])
            queue.extend((v, prev_steps + 1) for v in nei if v not in visited)
    
    dfs()
    print ' '.join(map(str, shortest_paths))