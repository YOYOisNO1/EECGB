def program730():
    t = int(input())
    ret = 0
    pows= 1
    digit = 0
    while t > 0:
        digit = t%10
        if digit > 4:
            ret = ret + (9-digit)*pows
        else:
            ret = ret + digit*pows
        pows *= 10
        t /= 10
    
    if digit == 9:
        ret = ret + digit*pows/10
    print(ret)