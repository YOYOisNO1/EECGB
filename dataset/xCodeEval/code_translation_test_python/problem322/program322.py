def program322():
    n = input()
    c = 0
    for i in range(1, len(n)):
    	c += i * 9 * 10**(i - 1)
    if len(n) == 1:
    	c = n
    else:
    	c += (int(n) - 10**(len(n) - 1) + 1) * len(n)
    print(c)