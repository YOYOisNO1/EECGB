def program1347():
    n = int(input())
    ar1 = map(int,input().split())
    ar2 = map(int,input().split())
    n1 = ar1[0]
    n2 = ar2[0]
    ar1 = ar1[1:]
    ar2 = ar2[1:]
    cnt = 0
    while ar1!=[] and ar2 !=[] and cnt<108:
        if ar1[0]>ar2[0]:
            ar1.append(ar2[0])
            ar1.append(ar1[0])
            ar2 = ar2[1:]
            ar1 = ar1[1:]
        else:
            ar2.append(ar1[0])
            ar2.append(ar2[0])
            ar1 = ar1[1:]
            ar2 = ar2[1:]
        cnt += 1
        
    if ar1==[]:
        print(cnt,2)
    elif ar2==[]:
        print(cnt,1)
    else:
        print(-1)