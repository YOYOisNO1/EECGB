def program147():
    from math import sqrt,ceil
    a,b = map(int,input().split())
    
    e = a - b 
    if(e == 0) :
        print("infinity")
    else :
        i = 1
        t = e
        ans = 0
        while(True) :
            if(e % i == 0):
            	t = e // i
            	if(t > b):
            		ans += 1
            if(e // i <= b) :
            	break
            i += 1
        print(ans)
            