def program3424():
    r = input()
    l = r.split(' ')
    r1 = input()
    r2 = input()
    if r1[0] == '>' and r1[int(l[0])-1] == '<':
    	if r2[0] == '^' and r2[int(l[1])-1] == 'v':
    		print('YES')
    		exit(0)
    elif r1[0] == '<' and r1[int(l[0])-1] == '>':
    	if r2[0] == 'v' and r2[int(l[1])-1] == '^':
    		print('YES')
    		exit(0)
    print('NO')