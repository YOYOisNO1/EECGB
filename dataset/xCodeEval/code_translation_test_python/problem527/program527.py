def program527():
    n = input()
    s = sum(map(int,input().split()))
    j = 0
    for i in range(0,5):
    	if ( s + i + 1 ) % ( n + 1 ) != 1:
    		j += 1
    print(j)