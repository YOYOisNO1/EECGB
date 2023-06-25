def F (x) :
        if (x < 10) :
            return x
        
        rv = 9
        tmp = x
        len = 0
        while (tmp > 0) :
            len += 1
            tmp /= 10
    
        d = int (x / pow(10, len-1))
    
        tmp = 1
        for i in range(len - 2) :
            rv += 9 * tmp
            tmp *= 10
    
        for i in range (1, 10) :
            if (i < d) :
                rv += 1 * tmp
        
        if (x / (pow(10, len-1)) <= x % 10) :
            rv += 1
    
        rv += (x % (pow(10, len - 1))) / 10
    
        return rv
    }
    
    l, r = map (int, input().split())
    
    print(F(r) - F(l-1))
    
    #     author: Ashwin Ginoria
    #     email: ashwinginoria@gmail.com
    #  123456789012345678
    # 100000000000000000
    # 1000000000000000000
    