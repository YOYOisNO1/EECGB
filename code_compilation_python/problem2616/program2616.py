    import math
    
def solve(n, A):
        visited = [False] * n
        r = 1
        for x in range(n):
            if visited[x]:
                continue
            else:
                visited[x] = True
            
            y = A[x]
            k = 1
            while not visited[y]:
                visited[y] = True
                y = A[y]
                k += 1
    
            if y != x:
                return -1
            r = k * r // math.gcd(k, r)
    
        return r if r%2 else r//2
    
    n = int(input())
    A = [int(x)- 1 for x in input().split()]
    
    print(solve(n, A))