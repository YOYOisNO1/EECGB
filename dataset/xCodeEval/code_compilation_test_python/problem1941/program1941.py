    import math
    
def main():
        n, m = list(map(int, input().split(' ')))
        max_base = [[0, 0] for _ in range(n+1)]
        for i in range(2, int(math.sqrt(n)) + 1):
            for j in range(2, 100):
                tmp = pow(i, j)
                if tmp > n:
                    break
                max_base[tmp][0] = i
                max_base[tmp][1] = j
        res = 1
        s = [0] * (m * (int(math.log2(n))) + 1)
        f = [0] * (int(math.log2(n) + 1))
        num = 0
        for i in range(1, int(math.log2(n) + 1)):
            for j in range(1, m + 1):
                if s[i * j] == 0:
                    num += 1
                    s[i * j] = 1
            f[i] = num
        for i in range(2, n + 1):
            if max_base[i][1] == 0:
                #print(i, int(math.log2(n) - math.log2(i)))
                #print(i, n, math.log(n, i))
                res += f[int(math.log(n, i))]
    
        print(res)
    
        return
    
    main()