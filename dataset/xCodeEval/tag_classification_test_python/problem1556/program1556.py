def program1556():
    n=int(input())
    a=input()
    l=[i for i in range(1,n+1) if n%i==0]
    for i in l:
    	a = a[i-1::-1] +a[i:]
    print(a)