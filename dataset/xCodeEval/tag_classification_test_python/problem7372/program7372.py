def main():
        n, m = map(int, input().split())
        links = [[False] * n for i in range(n)]
        for i in range(n):
            links[i][i] = True
        for _ in range(m):
            u, v = map(int, input().split())
            u -= 1
            v -= 1
            links[u][v] = links[v][u] = True
        res = [0] * n
        ref1 = ref3 = None
        for i, link in enumerate(links):
            if all(link):
                res[i] = 2
        if not all(res):
            i = res.index(0)
            res[i] = 1
            ref1 = links[i]
            for i, f in enumerate(ref1):
                if f and not (res[i]):
                    res[i] = 1
            if not all(res):
                i = res.index(0)
                res[i] = 3
                ref3 = links[i]
                for i, f in enumerate(ref3):
                    if f:
                        mark = res[i]
                        if mark == 1:
                            print("No")
                            return
                        if not mark:
                            res[i] = 3
        ref = [None, ref1, None, ref3]
        for i, mark in enumerate(res):
            if not mark:
                print("No")
                return
            if mark & 1:
                if ref[mark] != links[i]:
                    print("No")
                    return
        print("Yes")
        print(''.join(" abc"[mark] for mark in res))
    
    
    if __name__ == '__main__':
        main()