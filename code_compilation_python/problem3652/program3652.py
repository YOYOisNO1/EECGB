def program3652():
    import sys
    money = 0
    apples = 0
    customers = []
    num_customers, apple_price = [ int(x) for x in sys.stdin.readline().split(' ')
    
    
    for i in range(num_customers):
        arg = sys.stdin.readline()
        customers.append(arg)
    
    customers = reversed(customers)
    for c in customers:
        if c == 'halfplus':
            money += (apples+0.5)*float(apple_price)
            apples = 2*apples+1
        elif c == 'half':
            money += (apples)*float(apple_price)
            apples = 2*apples
    
    print(money)