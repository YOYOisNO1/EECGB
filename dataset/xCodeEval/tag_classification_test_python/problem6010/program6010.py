def program6010():
    n = int(input())
    
    extremes = 3 * pow(4 , n - 2)
    mid = (3 ** 2) * pow(4, n - 3)
    ans = 2 * extremes + (n - 3) * mid
    print(ans)