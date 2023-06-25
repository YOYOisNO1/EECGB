def search(n,low,high):
        mid = (low + high) / 2
    
        while low < high:
            mid = (low + high) / 2
            x = 3 * mid * (mid+1)
            #print(low,high,x)
            if x > n:
                high = mid
            elif x == n:
                return mid
            elif low + 1 >= high:
                if 3 * low * (low+1) >= n:
                    return low
                return high
            else:
                low = mid + 1
        return low
    
    n = input()
    
    if n == 0:
        print(0,0)
    else:
        # 0,6,12,18...
        # 123456
        # sum(6n) = 3n(n+1)
        x = search(n,1,int(1e10))
    
        index = 3*x*(x+1) - n
        #print(x,index)
        
        if index == 0:
            print(x) * 2  , 0
    
        else:
            t = (index-1) % x
            q = (index-1) / x
    
            if q == 0:
                print(x) * 2 - 1 - t , -(t+1) * 2
                
            basis = x * 2 - 1 - (x-1) , -x * 2
            
            if q == 1:
                print(basis[0]) - 2 - t * 2,basis[1]
    
            basis = basis[0] - 2 - (x-1) * 2,basis[1]
            
            if q == 2:
                print(basis[0]) - (t+1) , basis[1] + (t+1) * 2
                
            basis = basis[0] - x ,basis[1] + x * 2
            
            if q == 3:
                print(basis[0]) + (t+1) , basis[1] + (t+1) * 2
    
            basis = basis[0] + x ,basis[1] + x * 2
            
            if q == 4:
                print(basis[0]) + (t+1) * 2 , basis[1] 
    
            basis = basis[0] + x * 2 ,basis[1]
            
            if q == 5:
                print(basis[0]) + (t+1) , basis[1] - (t+1) * 2
    
            