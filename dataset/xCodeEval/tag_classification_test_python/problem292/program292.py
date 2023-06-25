def program292():
    t,s,x=map(int,input().split())
    q=(x-t)//s
    if(q>0 and ((x-t)%s==0 or (x-t)%s==1)):
    	print('YES')
    elif(x==t):
    	print('YES')
    else:
    	print('NO')