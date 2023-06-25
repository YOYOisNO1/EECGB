def program633():
    
    a = input()
    x = sorted(map(int, input().split()))
    
    for i in reversed(range(2, a)):
        if x[i] + x[i - 1] > x[i - 2] and x[i] + x[i - 2] > x[i - 1] and x[i - 2] + x[i - 1] > x[i]:
            print("YES")
            break
    else:
        print("NO")