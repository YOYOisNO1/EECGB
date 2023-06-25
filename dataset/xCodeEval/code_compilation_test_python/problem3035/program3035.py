    a = [['x', 'x'], ['x', 'x']]
    b = [['x', 'x'], ['x', 'x']]
    
def idx(i):
        if i > 1:
            return 0
    
        if i < 0:
            return 1
    
        return i
    
def swap(a, ia, ja, ib, jb):
        t = a[ia][ja]
        a[ia][ja] = a[ib][jb]
        a[ib][jb] = t
    
    import copy
    
def dfs(a, seen):
        seen.append(a)
        for i in range(2):
            for j in range(2):
                if a[i][j] != 'X':
                    continue
    
                acp = copy.deepcopy(a)
                swap(acp, i, j, idx(i+1), j)
                if acp not in seen:
                    dfs(acp, seen)
                swap(acp, i, j, idx(i+1), j)
    
                swap(acp, i, j, i, idx(j+1))
                if acp not in seen:
                    dfs(acp, seen)
                swap(acp, i, j, i, idx(j+1))
    
        return seen
    
def main():
        for j in range(2):
            # print j
            if j == 0:
                s1, s2 = input(), input()
                a[0][0] = s1[0]
                a[0][1] = s1[1]
                a[1][0] = s2[0]
                a[1][1] = s2[1]
    
            if j == 1:
                s1, s2 = input(), input()
                b[0][0] = s1[0]
                b[0][1] = s1[1]
                b[1][0] = s2[0]
                b[1][1] = s2[1]
    
        # print a, b
        arr = dfs(a, [])
    
        if b in arr:
            print("YES")
        else:
            print("NO")
    
    main()