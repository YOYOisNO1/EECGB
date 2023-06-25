def program7842():
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    
    import math
    
    a = int(input())
    r = int(math.ceil(math.log(a, 10))) + 1
    z = (45 * r * pow(10, r - 1, a) + 1) % a
    x = a - z
    print(x) + 1, 10 ** r + x
    # print(fsum(10**5) + 100) - fsum(100) - fsum(10**5)
    # print(fsum(11010),) fsum(10000) + 1010 + fsum(1000) + 10 + fsum(10)