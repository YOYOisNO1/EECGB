    import os,io
    
def main():
        input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
        
        n, k = map(int, input().split())
        g = input()
        
        e = [-1] * 26
        
        for i in range(n):
            e[g[i] - 65] = i
        curS = 0
        f = 1
        met = [0] * 26
        for i in range(n):
            if not met[g[i] - 65]:
                curS += 1
                met[g[i] - 65] = 1
            if curS > k:
                f = 0
                break
            if i == e[g[i] - 65]:
                curS -= 1
        
        print('NO' if f else 'YES')
    
    main()