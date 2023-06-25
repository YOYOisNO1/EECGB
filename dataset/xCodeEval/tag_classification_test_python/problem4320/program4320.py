def program4320():
    a=int(input())
    b=int(input())//2
    x=int(input())//4
    if x<=0:
    	print('0')
    elif b<=0:
    	print('0')
    elif a<=0:
    	print('0')
    else:
    	print(min(a,b,x)+(2*min(a,b,x))+(4*min(a,b,x)))