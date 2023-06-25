def program892():
    n,k = input().split(" ")
    n = int(n)
    k = int(k)
    
    while k != 0:
        if n%10 == 0:
            n = n // 10
        else:
            if n > 0:
                n = n - 1
            else:
                break
        k -= 1
    print(n)