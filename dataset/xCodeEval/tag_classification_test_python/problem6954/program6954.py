    import math
    
    
def solve():
        n = int(input().strip())
    
        vis = [False for i in range(n + 1)]
        pri_cnt = [i for i in range(n + 1)]
    
        pri = [0, 1]
        for i in range(2, n + 1):
            if not vis[i]:
                pri.append(i)
                for j in range(i, n + 1, i):
                    vis[j] = True
                    pri_cnt[j] -= pri_cnt[j] // i
    
        # print('pri', pri)
        # print('pri_cnt', pri_cnt)
    
        ans = 0
        mod: int = 10 ** 9 + 7
    
        divs = [[] for i in range(n + 1)]
    
        for i in range(2, n + 1):
            for j in range(i + i, n + 1, i):
                divs[j].append(i)
    
        for a in range(1, n - 1):
            bc = n - a
            # print(bc, gcd_bc_list)
            temp = 0
            total = bc - 1
            for gcd_bc in divs[bc]:
                cnt = pri_cnt[bc // gcd_bc] % mod
                temp += cnt
                ans += (cnt * math.lcm(a, gcd_bc)) % mod
                ans %= mod
            ans += a * (total - temp) % mod
            ans %= mod
            # print(a, 'temp', temp, 'ans', ans)
    
        return ans
    
    
    if __name__ == '__main__':
        # t = int(input().strip())
        # for _ in range(t):
        print(solve())