def main():
            a,b,c,d,e,f = map(int, input().split())
            can = 'Ron'
            cannot = 'Hermione'
            a,b,c,d,e,f = e,f,a,b,c,d
    		if b == 0 or d == 0 or f == 0:
                    print cannot
                    return 
            if a == 0 or c == 0 or e == 0:
                    print  can
                    return
            first = 10000
            second = 0
            third = 0
            for it in range(0, 1000): 
                    x = first / a
                    first %= a
                    second += b * x
                    y = second / c
                    second %= c
                    third += y * d
                    z = third / e
                    third %= e
                    first += z * f
            
            #print first
            if first > 10000*10000:
                    print can
            else:
                    print cannot
    
    main()
    
    '''
def main():
    	a,b,c,d,e,f = map(int, input().split())
    	can = 'Ron'
    	cannot = 'Hermione'
    	a,b,c,d,e,f = e,f,a,b,c,d
    	first = 10000
    	second = 0
    	third = 0
    	for it in range(0, 10000): 
    		x = first / a if a else 2**60
    		if a:
    			first %= a 
    		second += b * x
    		y = second / c if c else 2**60
    		if c:
    			second %= c
    		third += y * d
    		z = third / e if e else 2**60
    		if e:
    				third %= e
    		first += z * f
    	
    	#print first
    	if first > 10000*2:
    		print can
    	else:
    		print cannot
    
    main()
    '''