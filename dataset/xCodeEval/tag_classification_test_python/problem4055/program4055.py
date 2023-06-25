def program4055():
    from decimal import *
    
    res = Decimal(input())
    print([res, int(res)][res == int(res)])