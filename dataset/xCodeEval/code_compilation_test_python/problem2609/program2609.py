def program2609():
    # import sys
    # sys.stdin = open("test.in","r")
    # sys.stdout = open("test.out","w")
    w,h=map(int,input().split())
    u1,d1=map(int,input().split())
    u2,d2=map(int,input().split())
    for i in range(h,-1,-1):
    	if i==d1:
    		w=w-u1+i
    	elif i==d2:
    		w=w-u2+i
    	else:
    		w=w+i
    print(max(0,w)				