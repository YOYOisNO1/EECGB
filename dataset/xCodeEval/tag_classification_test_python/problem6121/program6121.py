def program6121():
    r1, c1, r2, c2 = [int(i) for i in input().split()]
    if (r1 == r2 or c1 == c2):
    	print(1, end=' ')
    else:
    	print(2, end=' ')
    if ((r1 + c1)%2 != (r2 + c2)%2):
    	print(0, end=' ')
    elif (abs(r2 - r1) == abs(c2 - c1)):
    	print(1, end=' ')
    else:
    	print(2, end=' ')
    print(max(abs(r2 - r1), abs(c2 - c1) ) )