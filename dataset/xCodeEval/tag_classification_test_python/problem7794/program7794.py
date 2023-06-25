def next(dx, dy):
        return ([(dx,dy+1), (dx, dy-1)] if dy == 0 else [(dx+1,dy), (dx-1, dy)] if dx * dy == 0 else [(dx,0), (0, dy)])
    visited = set()
    states = set()
    n = int(input())
    T = map(int, input().split())
    states.add((0,0,0,1))
    for t in T:
        new_states = set()
        for x,y,dx,dy in states:
            cnt = 0
            for k in range(1, t + 1):
                visited.add((x + k * dx, y + k * dy))
                cnt += 1
            next_dirs = next(dx, dy)
            for ndx, ndy in next_dirs:
                new_states.add((x + t*dx, y + t*dy, ndx, ndy))
        states = new_states
    print(len(visited))