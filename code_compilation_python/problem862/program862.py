def program862():
    n=int(input())
    a=input()
    s=[]
    for i in range(n):
    	s.append(int(a[i]))
    xx=sum(s)
    for i in range(1001):
    	cur=0
    	it=0
    	for j in range(n):
    		cur+=s[j]
    		if cur==num:
    			it+=1
    			cur=0
    	if cur==0 && it>1:
    		f=1
    		break
    if f==1:
    	print("YES")
    else:
    	print("NO")