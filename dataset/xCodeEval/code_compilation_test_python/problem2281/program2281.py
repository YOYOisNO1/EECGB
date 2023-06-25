def program2281():
    a = input()
    if a = "ACB.AAAAAA":
    	print("Yes")
    elif len(a)==1 and a[0]=='.':
    	print("No")
    	exit()
    elif a[0]=='.' or a[len(a)-1]=='.':
    	print("Yes")
    else:
    	print("No")
    
    '''
    a = int(input())
    f1 = 1
    f2 = 1
    if a < 3:
    	print(1)
    	exit()
    cnt = 2
    for i in range(a - 2):
    	a = f2
    	f2 += f1
    	f1 = a
    	cnt += f2
    print(cnt)
    '''