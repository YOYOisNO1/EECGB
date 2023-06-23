    n = int(input())
    
    nums = list(map(int, input().split(' ')))
    
    if n == 1:
        print(0)
        exit()
    
    memory = {}
    
def dp(i, j, k):
        """
            第i个位置 为 偶数(j=0)或奇数(j=1) 且 剩余k个偶数 时 前i个位置的最优解
        """
        if i < k-1:
            # 剩余位置少于剩余偶数，返回100
            return 100
    
        if i < 0:
            # 出口
            if (j == 1 and k != 0) or (j == 0 and k != -1):
                # 当j为奇数时候k应为0 偶数时k应为-1
                # 否则k有剩余偶数未填 返回100
                return 100
            else:
                return 0
    
        if nums[i] != 0 and nums[i]%2 != j:
            # 第i位不为0 奇偶不符合 返回100
            return 100
    
        if (i, j, k) in memory:
            return memory[(i, j, k)]
        
        if j == 0:
            res = min(dp(i-1, 0, k-1), dp(i-1, 1, k)+1)
        else:
            res = min(dp(i-1, 0, k-1)+1, dp(i-1, 1, k))
    
        memory.setdefault((i, j, k), res)
        
        return res
    
    
    res = min(dp(n-1, 0, (n>>1)-1), dp(n-1, 1, n>>1))
    
    print(res)