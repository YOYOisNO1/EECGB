    #!/usr/bin/python
    import math
    
    line = input()
    n,m,a,b = [int(x) for x in line.split()]
    
    a -= 1
    b -= 1
    
def find(n,m,a,b):
        nrows = n/m
        if n%m:
            nrows += 1
    
        arow = a/m
        brow = b/m
    
        if arow == brow:
            return 1
    
        if (b+1)%m == 0: #last in end
            if a%m == 0:    #first in start
                return 1
            else:
                return 2
    
        if a%m == 0:
            if (b+1)%m == 0 or b == n-1:
                return 1
            else:
                return 2
    
        if b == n-1:
            if a%m == 0:
                return 1
            else:
                return 2
    
        if a%m == (b+1)%m:
            return 2
    
        if brow - arow >= 2:
            return 3
        else:
            return 2
    
        return 2
    
    print(find(n,m,a,b))