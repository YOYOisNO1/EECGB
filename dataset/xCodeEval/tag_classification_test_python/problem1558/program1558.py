def reverse(str1):
    	str = ""
    	for i in str1:
    		str = i + str
    	return str
    
    n = input()
    string = str(input())
    for i in range(2,(n/2)+1):
    	if n%i==0:
    		temp = str(reverse(string[:i]))
    		string = temp + string[i:]
    print((reverse(string)))