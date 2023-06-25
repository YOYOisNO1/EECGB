def program5859():
    a,b,c = map(int,input().split())
    total = (a*c)//b
    t = 0
    
    for i in range(total+1):
    	if total*b>=(total-i)*a:
    		t = i
    		break
    
    print(t)