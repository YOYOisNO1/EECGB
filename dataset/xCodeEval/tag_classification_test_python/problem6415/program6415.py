    n,m,i,j,a,b = [int(x) for x in input().split()]
    
    i -= 1
    j -= 1
    
    best = float('inf')
    
def find(x,y,a,b,n,m):
        n = n//a
        m = m//b
        x = x//a
        y = y//b
    
        total = min(x,y)
    
        x -= total
        y -= total
        
        if (y+x)%2 == 0:
            if y == 0 and m > 1:
                return y+x+total
            elif x == 0 and n > 1:
                return y+x+total
            elif y == 0 and x == 0:
                return y+x+total
            else:
                return float('inf')
        else:
            return float('inf')
    
    if i%a == 0:
        x = i
        if j%b == 0:
            y = j
            best = min(best,find(x,y,a,b,n,m))
            #print(1,best)
        if (m-j-1)%b == 0:
            y = m-j-1
            best = min(best,find(x,y,a,b,n,m))
            #print(2,best)
    if (n-i-1)%a == 0:
        x = n-i-1
        if j%b == 0:
            y = j
            best = min(best,find(x,y,a,b,n,m))
            #print(3,best)
        if (m-j-1)%b == 0:
            y = m-j-1
            best = min(best,find(x,y,a,b,n,m))
            #print(4,best)
    if best == float('inf'):
        print('Poor Inna and pony!')
    else:
        print(best)
        
        