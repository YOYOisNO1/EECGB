def digit(n):
    	digits = dict()
    	digits[1]=('one',)
    	digits[2]=('two','twen')
    	digits[3]=('three','thir')
    	digits[4]=('four','for')
    	digits[5]=('five','fif')
    	digits[6]=('six','six')
    	digits[7]=('seven','seven')
    	digits[8]=('eight','eigh')
    	digits[9]=('nine','nine')
    	digits[10]=('ten',)
    	digits[11]=('eleven',)
    	digits[12]=('twelve',)
    
    	if n <= 12:
    		return str(digits[n][0])
    	else:
    		n1 = n/10
    		n2 = n%10
    		if n1 < 2:
    			return str(digits[n2][1]) + 'teen'
    		elif n2 < 1:
    			return str(digits[n1][1]) + 'ty'
    		else:
    			return str(digits[n1][1]) + 'ty-' + str(digits[n2][0]) 
    
    n = int(input())
    print digit(n)