def program2233():
    l= map(int, input().split())
    a=l[0]
    b=l[1]
    c=l[2]
    
    f=0
    
    for i in range(b) :
        a *= 10
        if c == a // b :
            f=1
    	    print i + 1
    	    break
        a =a% b
    
    if f==0:
        print -1