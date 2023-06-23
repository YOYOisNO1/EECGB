def program2279():
    n = input()
    s = [i for i in n]
    l = 0
     
    d = []
     
    for i in range(len(n)//2+1):
    	if s[i] == s[-i-1]:
    		
    	else:
    		l+=1
    		pass
     
    if l == 1 or (l==0 and len(s)%2 ==0 :
    	print("YES")
    else:
    	print("NO")