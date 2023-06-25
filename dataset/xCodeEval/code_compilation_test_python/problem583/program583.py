def get_result(line,remainder,quotient,m):
        result1 = remainder * ((line[0]*(line[0]-1))/2)
        result2 = (m-remainder) * ((quotient*(quotient-1))/2)
        return result1 + result2
    
    
    n,m = map(int,input().split())
    
    max_friends = (n-m+1)*(n-m)/2
    
    line = m*[n/m]
    remainder = n%m
    quotient = n/m
    
    for i in range(remainder):
        line[i] += 1
    
    min_friends = get_result(line,remainder,quotient,m)
    
    print min_friends  max_friends