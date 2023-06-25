def program3319():
    abc=list(map(int,input().rstrip().split()))
    abc.sort()
    if abc[0]+abc[1]>abc[2]:
        print('0')
        exit()
    elif abc[0]+abc[1]==abc[2]:
        print('1')
    elif abc[0]+abc[1]<abc[2]:
        print(abc[2]-abc[0]-abc[1]+1)
    