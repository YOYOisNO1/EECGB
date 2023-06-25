    '''
    Created on May 30, 2014
    
    @author: szalivako
    '''
    
def findD(a, i, k, d):
        
        k_ = 0
        j = i
        while (j < len(a) and a[j] != d):
            j += 1
            k_ += 1
        
        if (j == len(a) or k_ > k):
            return -1
        else:
            return k_
        
    
    a, k = map(int, input().split())
    a = list(str(a))
    
    i = 0
    
    while (k > 0 and i < len(a)):
        for d in range(9, 0, -1):
            k_ = findD(a, i, k, str(d))
            #print(d,) k_, k
            if (k_ == 0):
                break
            if (k_ != -1):
                j = i + k_
                while (j > i):
                    a[j - 1], a[j] = a[j], a[j - 1]
                    j -= 1
                    k -= 1
                break
            
        i += 1
    
    ans = ''
    
    for ai in a:
        ans += ai
        
    print(ans)
        
        
            