def program3739():
    fly1 = list(map(int, input().split()))
    fly2 = list(map(int, input().split()))
    if (fly1[0] == fly2[0] and fly1[1] == fly2[1]) or (fly1[0] == fly2[0] and fly1[2] == fly2[2]) or (
            fly1[2] == fly2[2] and fly1[1] == fly2[1]):
        print("YES")
    else:
        print("NO")