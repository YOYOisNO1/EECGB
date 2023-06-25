def program3288():
    import math
    n,k = map(int, input(). split())
    if n + n-1 < k or k == 1:
        print(0)
    else:
        if k > n:
            perv = k - n 
            rasn = n - perv + 1
            otvet = rasn / 2
            math.floor(otvet)
            print(int(otvet))
        elif k == n:
            if k % 2 == 0:
              otvet = k / 2
              print(int(otvet))
            else:
                 k -= 1
                 otvet = k / 2
              print(int(otvet))
        else:
            otvet = (k - 1) / 2 
            math.floor(otvet)
            print(int(otvet))