def program3256():
    a=[(2**k-1)*(2**(k-1)) for k in range(1,17)]
    n=input()
    for i in a[::-1]:
    	if n%i == 0:
    		print(i)
    		break