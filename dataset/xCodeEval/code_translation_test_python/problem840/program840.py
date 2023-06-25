def program840():
    bf = []
    for k in range(20):
    	bf = [int('1'*(k+1)+'0'*k,2)] + bf
    n = input()
    while bf[0] > n:
    	bf = bf[1:]
    while (n % bf[0]) != 0:
    	bf = bf[1:]
    print(bf[0])