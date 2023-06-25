    n, m = map(int,input().split())
    
    from math import factorial
    
def combinations_count(n, r):
        return factorial(n) // (factorial(n - r) * factorial(r))
    
    MOD = 10**9+7
    
def cut_pat(x):
        cut_pattern = 0
        for two in range(x//2+1):
            one = x - two*2
            if two == 0:
                tmp_cnt = 1
            else:
                tmp_cnt = combinations_count(one+two,two) % MOD
            cut_pattern += tmp_cnt
    #     print(cut_pattern)
    
        # 色がパターン
        return cut_pattern * 2
    
    cut_pattern = 0
    cut_pattern += cut_pat(n)
    cut_pattern += cut_pat(m)
    
    # 両辺とも全て1で切った場合同じものがかぶる
    cut_pattern -= 2
    
    cut_pattern %= MOD
    
    print(cut_pattern)