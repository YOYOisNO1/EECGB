def program1754():
    c = input()
    h = input().split()
    p=0
    for i in h:
    	if(i[0]==c[0] or i[1] == c[1]):
    		p = 1
    		break
    		
    if p==1:
    	print('YES')
    else:
    	print('NO')