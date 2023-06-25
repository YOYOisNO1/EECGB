def program991():
    n=int(input())
    a=int(input())
    b=int(input())
    d=int(input())
    
    if (a==min(a,b,d) or b==min(a,b,d) or n==1):
    	print((n-1)*min(a,b,d))
    else:
    	print(min(a,b)+(n-2)*min(a,b,d)