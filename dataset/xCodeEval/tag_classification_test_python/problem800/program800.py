def program800():
    a,b = map(int,input().split(":"))
    min = int(input())
    
    temp1 = int((min + b)/60)
    temp2 = (min + b) % 60
    
    a = (a + temp1) % 24
    b = temp2
    
    string = str(a) + ':' + str(b)
    if(len(str(a)) == 1):
    	a = '0' + str(a)
    if(len(str(b)) == 1):
    	b = '0' + str(b)
    string = str(a) + ':' + str(b)
    print(string)