def program4812():
    n=int(input())
    s=input()
    x,y,t=0,0,0
    for i in range(n):
    	if s[i]=="L":
    		x-=1
    	elif s[i]=="R":
    		x+=1
    	elif s[i]=="U":
    		y+=1
    	elif s[i]=="D":
    		y-=1
    print(n-abs(x)-abs(y))