def k_tree(n, k, d):
    def _k_tree(n, k):
            if k <= 0 or n <= 0:
                return 0
            cache = [1] * n
            for i in range(1, n):
                sum_num = 0
                for j in range(max(0, i - k), i):
                    sum_num += cache[j]
                if i < k:
                    sum_num += 1
                cache[i] = sum_num
            return cache[-1]
        return _k_tree(n, k) - _k_tree(n, d - 1)
    
    
    n, k, d = map(int, input().strip().split())
    print(k_tree(n, k, d) % 1000000007)