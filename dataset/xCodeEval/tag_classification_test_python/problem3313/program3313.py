def program3313():
    n, m, r= map(int, input().split())
    s_ = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    #n ,m , r = 5, 6, 8
    #s_ = [7, 7, 10, 5, 5]
    #b= [5, 6, 2, 8, 1, 8]
    
    s = []
    for x in s_:
        if x not in s:
            s.append(x)
    n = len(s)
    
    if min(s)>=max(b):
        print(r)
    else:
        quantity =[]
        balance = []
        for i in range (n):
            quantity.append(r//s[i])
            balance.append(r%s[i])
        best_quantity =max(quantity)
        best_balance = -1
        #print(balance)
        op = quantity.count(best_quantity)
        #print(op)
        for q in range (op):
            #print(balance[quantity.index(best_quantity)])
            if best_balance < balance[quantity.index(best_quantity)]:
                best_balance = balance[quantity.index(best_quantity)]
                #del quantity[quantity.index(best_quantity)]
                quantity[quantity.index(best_quantity)] = 0
                #quantity.insert(quantity.index(best_quantity), 0)
                #print(quantity)      
            #print((best_balance))
        print(best_quantity*max(b)+best_balance)