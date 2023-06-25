def program1360():
    a = int(input())
    b = int(input())
    c = int(input())
    if a == 1 and c == 1:
    		print(b+2)
    elif a == 1:
    	print((b+1)*c)
    elif c == 1:
    	print((b+1)*a)
    elif b == 1:
    	print((min(a,c)+1)*max(a,c))
    else:
    	print(a*b*c)