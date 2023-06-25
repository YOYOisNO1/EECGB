def program3738():
    x=int(input())
    if x>36:
        print(-1)
    elif x%2==0:
        print('8'*(x//2))
    else:
        print('8'*(x//2)+'6')