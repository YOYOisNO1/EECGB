def program3762():
    n = int(input())
    ar = list(map(int, input().split()))
    if len(ar) == 1:
        if ar[0] == 15:
            print('DOWN')
        elif ar[0] == 0:
            print('UP')
        else:
            print(-1)
    else:
        if ar[-1] - ar[-2] > 0:
            if ar[-1] != 15:
                print('UP')
            else:
                print('DOWN')
        else:
            if ar[-1] != 0:
                print('DOWN')
            else:
                print('UP')