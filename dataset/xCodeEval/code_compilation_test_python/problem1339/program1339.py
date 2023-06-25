    n = int(input())
    numbers = [n]
    
def Summ(N):
        S = 0
        while N > 0:
            S += N%10
            N //= 10
        return(S)
    
    for i in range(0,len(str(n))):
        n -= n%(10**i) + 1
        numbers.append(n)
    
    Max_Summ = -1
    Ans = 0
    
    for i in numbers:
        if Summ(i) > Max_Summ:
            Max_Summ = Summ(i)
            Ans = i
    
    print(Ans)