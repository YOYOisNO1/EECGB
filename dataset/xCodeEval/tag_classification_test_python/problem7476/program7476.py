def program7476():
    from math import factorial as fact;
    A=[1,3,15,133,2025,37851,1030367,36362925,1606008513,87656896891,5778121715415,452794797220965,41609568918940625]
    n = input();
    if n%2 == 0:
    	print((0))
    else:
        print(A[n/2] * fact(n) % (10**9 + 7))