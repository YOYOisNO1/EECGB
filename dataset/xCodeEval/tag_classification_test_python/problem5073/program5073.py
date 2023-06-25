def program5073():
    comprimento = int(input())
    
    if comprimento % 2 != 0:
    	print(0)
    elif comprimento % 4 == 0:
    	print((comprimento/4)) -1
    else:
    	print(comprimento/4)