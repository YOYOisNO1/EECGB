def program501():
    #codeforces_1003B_live
    a,b,x = [int(e) for e in input().split(" ")]
    ans = ""
    choose = ["0","1"]
    if x == 1:
    	print(a*"0"+b*"1")
    	exit()
    if x == 2:
    	if (b>1):
    		print((b-1)*"1"+a*"0"+"1")
    	else:
    		print((a-1)*"0"+b*"1"+"0")
    	exit()
    if x == 3:
    	print((b-2)*"1"+"101"+(a-1)*"0")
    	exit()
    while x > 1:
    	ans += choose[x%2]
    	if (x%2 == 0): a-=1;
    	if (x%2 == 1): b-=1;
    	x -= 1
    '''
    print(ans)
    print(a)
    print(b)
    '''
    if ans[-1] == "0":
    	if a == 0:
    		ans = "1" + ans + (b-1)*"1"
    	else:
    		ans = ans + "1"*(b) + "0"*(a)
    else:
    	ans = ans + "0"*a + "1"*b
    print(ans)