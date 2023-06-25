def program1514():
    n=int(input())
    s=input()
    l=[0]*26
    co=0
    for i in s:
    	idx=ord(i)-ord('a')
    	l[idx]+=1
    	if l[idx]>1:
    		print("Yes")
    		quit()
    	elif l[idx]==1:
    		co+=1
    if co==1:
    	print("Yes")
    else:
    	print("No")