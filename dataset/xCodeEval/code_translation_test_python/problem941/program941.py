def program941():
    hundred, ten = [int(x) for x in input().split()]
    total = 100*hundred + 10*ten
    
    #reduce by number of rounds where Ciel can take 2 100-yen and 2 10-yen, and Hanako can take 22 10-yen
    skipped = min(hundred//2,ten//24)
    hundred = hundred - 2*skipped
    ten = ten - 24*skipped
    
    while True:
        win = 0
        if hundred >= 2 and ten >= 2:
            hundred = hundred - 2
            ten = ten - 2
        elif hundred >= 1 and ten >= 12:
            hundred = hundred - 1
            ten = ten - 12
        elif ten >= 22:
            ten = ten - 22
        else:
            break
        win = 1
        if ten >= 22:
            ten = ten - 22
        elif hundred >= 1 and ten >= 12:
            hundred = hundred - 1
            ten = ten - 12
        elif hundred >= 2 and ten >= 2:
            hundred = hundred - 2
            ten = ten - 2
        else:
            break
    if win == 0:
        print(("Hanako"))
    else:
        print(("Ciel"))
        