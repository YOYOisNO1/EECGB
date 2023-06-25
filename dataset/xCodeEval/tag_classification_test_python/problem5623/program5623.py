def program5623():
    import math;
    n,m = list(map(int, str(input()).split()))
    if(min(m,n) == 1):
        print(n*m)
    elif(min(n,m) == 2):
        some = max(m,n)
        total = some - (some%4)
        some %= 4
        if(some == 1) or (some == 2):
            total+=some*2
        elif(some == 3):
            total += 4
        print(total)
    else:
        print(int(math.ceil(n*m/2.0)))