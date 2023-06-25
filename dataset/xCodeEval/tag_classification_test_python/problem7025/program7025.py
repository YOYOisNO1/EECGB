    n = int(input())
    
def PotenciaDosMasCercana(n):
        if n == 0:
            return 0,0
        p = 1
        i = 0
        while p <= n:
            p = p << 1
            i +=1
        return p >> 1, i - 1
    
    
def C_Conexas(b):
        dp = [int]*2
        dp[0] = 0
        for i in range(1,b+1):        
            dp[1] = 2 * dp[0] + 2 ** (i-1)
            dp[0] = dp[1]
        return dp[0]
    
    
def main(n):
        a,b = PotenciaDosMasCercana(n)
        Ans = 0
        if(n == a):
            Ans = C_Conexas(b)
        else:
            c,d = PotenciaDosMasCercana(n-a)
            Ans = C_Conexas(b) + main(n-a) + a
        return Ans
    
    print(main(n))