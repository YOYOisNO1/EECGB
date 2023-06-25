def program100():
    required = list(map(int, input().split()))
    available = list(map(int, input().split()))
    if available[0] < required[0]:
        print("NO")
    elif (available[0] + available[1] - required[0]) < required[1]:
        print("NO")
    elif sum(available) - (required[0] + required[1]) < required[2]:
        print("NO")
    else:
        available[0] -= required[0]
        available[0] -= required[1]
        if available[0] < 0:
            available[1] -= abs(available[0])
            available[0] = 0
        if sum(available) - required[2] >= 0:
            print("YES")
        else:
            print("NO")