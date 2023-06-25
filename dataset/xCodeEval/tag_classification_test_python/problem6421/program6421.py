    #設定
    import sys
    input = sys.stdin.buffer.readline
    
    #ライブラリインポート
    from collections import defaultdict
    
    INF = float("inf")
    con = 1000000007
    
def getlist():
    	return list(map(int, input().split()))
    
    # 組み合わせ Combination
    # C = fac[N] * finv[i] * finv[N - i]
    
    #処理内容
def main():
    	N, M = getlist()
    	DP1 = [0] * 100001
    	DP2 = [0] * 100001
    	DP1[0] = 1
    	DP1[1] = 1
    	DP2[0] = 0
    	DP2[1] = 1
    	#DP
    	for i in range(2, 100001):
    		DP1[i] = (DP1[i - 1] + DP2[i - 1]) % con
    		DP2[i] = DP1[i - 1] % con
    	ans = (DP1[N - 1] + DP1[M - 1] + DP2[N - 1] + DP2[M - 1]) * 2 - 2
    	print(ans % con)
    	
    if __name__ == '__main__':
    	main()