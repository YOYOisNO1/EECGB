def program1209():
    n = int(input())
    dv = 3
    while n % dv == 0:
    	dv *= 3
    print(n/dv) + 1