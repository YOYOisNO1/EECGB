def program344():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1 and a[0] != 15 and a[0] != 0:
        print("-1")
    elif (a[-1] == 0) or (n > 1 and a[-1] > a[-2] and a[-1] != 15):
        print("UP")
    else:
        print("DOWN")