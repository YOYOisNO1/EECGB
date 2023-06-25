def program2195():
    '''input
    10
    '''
    n = input()
    ans = 0
    for i in range(1,n):
    	if (n-i)%i == 0:
    		ans += 1
    print(ans)