def program6516():
    """
    Task:
    Given fraction a/b find the first occurence of
    digit c in the decimal notation of the fraction
    after the decminal point
    """
    
    a, b, c = map(int, input().split())
    q, r = divmod(a, b)
    under = a - (b * q)
    
    after_decimal_point = ''
    for _ in range(b):
        under *= 10
        q, r = divmod(under, b)
        under -= b * q
        after_decimal_point += str(q)
    
    location = after_decimal_point.find(str(c))
    if location == -1:
        print(-1)
    else:
        print(location + 1)