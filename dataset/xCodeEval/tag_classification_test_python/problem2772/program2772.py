def program2772():
    a = [(str(j+1)+"".join([str(x) for x in range(11 - i, 10)])) for i in range(1,10) for j in range(10-i)]
    for i in range(int(input())):
    	print(a[int(input())-1])