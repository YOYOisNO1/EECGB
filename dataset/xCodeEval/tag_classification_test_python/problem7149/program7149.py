    import collections
    from sys import *
    input = stdin.readline
    
    # !!! Check if input have a t !!!
    
    T = 0
    # T = 1
    
def solve():
    	mod = 998244353
    	n, k = ria()
    
    	choose = [[0 for _ in range(n+1)] for _ in range(n+1)]
    	# choose[0][0] = 1
    	for i in range(n+1):
    		choose[i][0] = 1
    		for j in range(1, i+1):
    			choose[i][j] = (choose[i-1][j] + choose[i-1][j-1]) % mod
    
    	dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
    	pw = [0 for _ in range(n * n + 1)]
    	dp[1][0] = 1
    	for j in range(1, k+1):
    		pw[0] = 1
    		for pi in range(1, n*n+1):
    			pw[pi] = pw[pi-1] * (k - j + 1) % mod
    		for i in range(1, n+1):
    			for z in range(1, i+1):
    				edge_num = (i - z) * (z - 1) + (i - z) * (i - z - 1) // 2
    				dp[i][j] += dp[z][j-1] * choose[i-1][z-1] % mod * pw[edge_num] % mod
    				dp[i][j] %= mod
    	print(dp[n][k])
    	return
    
    
def ria():
    	return list(map(int, input().strip().split()))
def rsa():
    	return input().strip().split()
def ri():
    	return int(input().strip())
def rs():
    	return input().strip()
    
def tcase():
    	for _ in range(ri()):
    		solve()
    
def main():
    	tcase() if T else solve()
    
    if __name__ == "__main__":
        main()