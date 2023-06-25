    '''
    Author: Wa-Automaton
    Time: 202102162 14:44:00 UTC+8
    
    Website: codeforces.com
    Contest: Educational Codeforces Round 104 (Rated for Div. 2)
    Problem: F. Ones
    
    Result:
    Solution:
    
    More:
        Thanks RUSH_D_CAT. 
        Learn it from RUSH_D_CAT's solution 107487575.
    
    '''
    n = int(input())
    
    dp = {}
    
def calc(x):
        # print(x)
        # if x < 10 : return x # wa
        if 0 == x : return 0   # ok
        if x in dp.keys() : return dp[x]
        
        l = len(str(x))
        u = 10 ** l // 9
        if x < u : u = u // 10; l -= 1
        v = u * 10 + 1
        
        u1 = calc(x % u) + (x // u * l)
        # u2 = calc(v - x) + l + 1   # tle
        u2 = calc((v - x) % u) + (l + 1) + ((v - x) // u * l) # ok
        
        res = min(u1, u2)
        dp[x] = res
        # print(x, u, v, u1, u2, res)
        return res
        
    print(calc(n))