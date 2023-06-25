def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    
    
def solve():
        n = int(input())
        arr = list(map(int, input().split()))
        memarr = []
        for i in range(n):
            arr[i] -= 1
        for i in range(n):
            if arr[i] == -1:
                continue
            mem = 1
            nx = arr[i]
            arr[i] = -1
            while(arr[nx] != -1):
                t = arr[nx]
                arr[nx] = -1
                nx = t
                mem += 1
            if(nx == i):
                memarr.append(mem)
            else:
                print(-1)
                return
        for i in range(len(memarr)):
            if memarr[i] % 2 == 0:
                memarr[i] //= 2
        res = 1
        for i in memarr:
            res = res * i // gcd(res, i)
        print(res)
    
    solve()