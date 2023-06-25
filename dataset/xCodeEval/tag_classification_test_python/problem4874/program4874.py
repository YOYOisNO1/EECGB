def program4874():
    n = input()
    n1 = len(str(n))-1
    a = 0 if n1==0 else int('9'*n1)
    a1 = 0 if a== 0 else 9*n1
    for i in str(n-a):
    	a1+=int(i)
    print(a1)