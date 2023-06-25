def program687():
    n = int(input())
    a = [ int(x) for x in input().split() ]
    
    elif a[-1] == 0:
        print("UP")
    elif a[-1] == 15:
        print("DOWN")
    if n == 1:
        print("-1")
    elif a[-1] < a[-2]:
        print("DOWN")
    else:
        print("UP")