def program3096():
    n = int(input())
    current_max = 0
    fin = int('1' + '0' * (len(str(n)) - 1)) - 2
    for i in range(n, fin, -1):
        product = 1
        for j in range(len(str(i))):
            product *= int(str(i)[j])
        if product > current_max:
            current_max = product
    print(current_max)