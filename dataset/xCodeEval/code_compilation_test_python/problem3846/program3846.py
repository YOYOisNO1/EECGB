def program3846():
    s = input()
    pos = 0
    
    for i in s :
        if "0"<=i and i<="9" :
            ;
        else :
            break;
        pos+=1
    
    a=int(s[0:pos])
    c=s[pos:]
    
    d = {"f":1,"e":2,"d":3,"a":4,"b":5,"c":6}
    
    t=a
    a = (a+1)//2
    a = (a+1)//2
    
    print( 16*(a-1) + 7*(1-t%2) + d[c])