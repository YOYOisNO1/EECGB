def program1972():
    string = input().split(' ')
    n = int(string[0])
    pos = int(string[1])
    a = int(string[2])
    b = int(string[3])
    
    if b==n and a==1:
    	print(0)
    elif b==n and a!=1:
    	if pos>=a:
    		print(pos-a+1)
    	else:
    		print(a-pos+1)
    elif a==1 and b!=n:
    	if pos<=b:
    		print(b-pos+1)
    	else:
    		print(pos-b+1)
    else:
    	if pos<=a:
    		print(b-pos+2)
    	elif pos>=2
    		print(pos+2-a)
    	else:
    		res_left=pos-2*a+2+b
    		res_right=2*b-pos+2-a
    		print(min(res_left, res_right))