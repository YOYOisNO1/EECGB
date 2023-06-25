    dr = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    
    n = int(input())
    t = [int(i) for i in input().split()]
    
def dfs(d, pos, path):
        if d == n+1:
            return set()
        cell = set()
        c = t[d-1]
        for _ in range(c):
            pos = (pos[0] + dr[path][0], pos[1] + dr[path][1])
            cell.add(pos)
        cell = cell.union(dfs(d+1, pos, (path+1) % 8))
        cell = cell.union(dfs(d+1, pos, (path-1) % 8))
        return cell
    
    total_cells = dfs(1, (0, 0), 0)
    print(len(total_cells))