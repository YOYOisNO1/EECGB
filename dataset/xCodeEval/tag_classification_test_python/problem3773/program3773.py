def program3773():
    r1 = list(map(int,input().split()))
    r2 = list(map(int,input().split()))
    r3 = list(map(int,input().split()))
    r4 = list(map(int,input().split()))
    
    if sum(r1[:3]) > 0 and r1[3] ==1 :
        print('YES')
    elif sum(r2[:3]) > 0 and r2[3] ==1:
        print('YES')
    elif sum(r3[:3]) > 0 and r3[3] ==1:
        print('YES')
    elif sum(r4[:3]) > 0 and r4[3] ==1:
        print('YES')
    else:
        if (r1[0] == 1 and r4[3] == 1) or (r1[1] == 1 and r3[3] == 1) or (r1[2] == 1 and r2[3] == 1):
            print('YES')
        elif (r2[0] == 1 and r1[3] == 1) or (r2[1] == 1 and r4[3] == 1) or (r2[2] == 1 and r3[3] == 1):
            print('YES')
        elif (r3[0] == 1 and r2[3] == 1) or (r3[1] == 1 and r1[3] == 1) or (r3[2] == 1 and r4[3] == 1):
            print('YES')
        elif (r4[0] == 1 and r3[3] == 1) or (r4[1] == 1 and r2[3] == 1) or (r4[2] == 1 and r1[3] == 1):
            print('YES')
        else:
            print('NO')