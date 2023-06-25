def divisao(n):
        if n == 0:
            return 0
        valor = 1
        count = 1
        while 10*valor+1 <= n:
            valor *= 10
            valor += 1
            count += 1
            
        if n<= 5 * valor:
            return divisao(n - valor)+count
     
        if n>6*valor:
            return divisao(10 * valor + 1 - n) + count + 1
     
        ans1 = divisao(n - valor) + count
        ans2 = divisao(10 * valor + 1 - n) + count + 1
        return(min(ans1, ans2))
     
    n = int(input())
    print(divisao(n))