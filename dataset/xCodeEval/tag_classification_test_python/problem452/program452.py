def program452():
    
    case=input()
    coins=case.split()
    coins=[int(x) for x in coins]
    pot=sum(coins)
    if pot%5==0 and pot>0:
        print(pot/5)
    else:
        print(-1)