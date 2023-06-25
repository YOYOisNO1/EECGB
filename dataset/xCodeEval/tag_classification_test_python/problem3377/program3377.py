def program3377():
    t = int(input())
    
    s = [0]*101
    s[1] = 1
    
    for i in range(2,len(s)):
        s[i] = s[i-1] + (i-1)*4
    
    print( s[t] )