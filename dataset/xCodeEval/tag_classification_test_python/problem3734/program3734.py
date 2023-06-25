def program3734():
    k=input()
    if k>36:
        print(-1)
    else:
        if k%2==0:
            x=k/2
            arr=['8']*(x)
        else:
            x=k/2
            arr=['8']*(x)
            arr.append('4')
        print('').join(arr)