def binary_search(lb, ub, criterion):
        ok = lb
        ng = ub
        while ng - ok > 1:
            mid = (ng + ok) // 2
            if criterion(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    
    n, k = list(map(int, input().split()))
    odd_acc_count = 0
    odd_count = 1
    depth = 0
    while odd_acc_count < k:
        odd_acc_count += odd_count
        odd_count *= 2
        depth += 1
    
    residual = k - (odd_acc_count - odd_count // 2) - 1
    odd_max_idx = binary_search(0, n + 2, lambda x:
                                (2 * x + 1) * (1 << (depth - 1)) + residual <= n)
    ans_odd = 2 * odd_max_idx + 1
    
    even_acc_count = 0
    even_count = 2
    depth = 0
    while even_acc_count < k:
        even_acc_count += even_count
        even_count *= 2
        depth += 1
    residual = k - (even_acc_count - even_count // 2) - 1
    even_max_idx = binary_search(0, n + 2, lambda x:
                                 2 * x * (1 << (depth - 1)) + residual <= n
                                 )
    
    ans_even = 2 * even_max_idx
    print(max(ans_odd, ans_even))