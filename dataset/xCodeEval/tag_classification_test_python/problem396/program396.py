    __author__ = 'Darren'
    
    
def solve():
    
    def find_ways(t, n, h):
            if t == breaks and n == total:
                return 1
            if t > breaks or n == total:
                return 0
            if (t, n, h) not in dp:
                result = 0
                if t % 2 == 0:
                    for i in range(h+1, 5):
                        result += find_ways(t, n+1, i)
                    for i in range(1, h):
                        result += find_ways(t+1, n+1, i)
                else:
                    for i in range(h+1, 5):
                        result += find_ways(t+1, n+1, i)
                    for i in range(1, h):
                        result += find_ways(t, n+1, i)
                dp[(t, n, h)] = result
            return dp[(t, n, h)]
    
        total, humps = map(int, input().split())
        breaks = 2 * humps - 1
        dp = {}
        ans = 0
        for i in range(2, 5):
            ans += (i - 1) * find_ways(0, 2, i)
        print(ans)
    
    
    if __name__ == '__main__':
        solve()