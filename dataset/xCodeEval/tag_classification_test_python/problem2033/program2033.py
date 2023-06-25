def solve(rest, k, least):
        if least != 1 << 30 and rest < least:
            return 0
        if rest == 0 and least == 1 << 30:
            return 1
        if least == 1 << 30 and memo[rest] != 0:
            return memo[rest]
        if least != 1 << 30 and memo2[rest] != 0:
            return memo2[rest]
        ret = 0
        for i in xrange(min(rest, k), 0, -1):
            if i >= least:
                tmp = solve(rest - i, k, 1 << 30)
            else:
                tmp = solve(rest - i, k, least)
            ret += tmp
        if least == 1 << 30:
            memo[rest] = ret
        else:
            memo2[rest] = ret
        return ret
    
    if __name__ == '__main__':
        n, k, d = map(int, input().split())
        memo = [0] * (n + 1)
        memo2 = [0] * (n + 1)
        mod = 10 ** 9 + 7
        print(solve(n,) k, d) % mod