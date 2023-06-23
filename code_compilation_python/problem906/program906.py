def program906():
    a1,a2,k1,k2,n=(int(input()) for i in range(5))
    if k1>k2:
    	a1,k1,a2,k2=a2,k2,a1,k1
    print(max(0,n-(a1*(k1-1)+a2*(k2-1)),end=" ")
    if n<=a1*k1:
    	print(n//k1)
    else:
    	print(a1+(n-(a1*k1))//k2)