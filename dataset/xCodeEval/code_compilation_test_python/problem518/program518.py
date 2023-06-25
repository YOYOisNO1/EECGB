def program518():
    par = map(int, input().split(' '))
    
    total = sum(par)
    if total % 5 == 0:
        sol = total / 5
        if sol == 0 :
            return -1 
        else:
            return sol
    return -1