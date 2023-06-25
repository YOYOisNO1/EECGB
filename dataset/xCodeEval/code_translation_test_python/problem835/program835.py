def program835():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    brr1 = []
    for i in range(0, 2 * n, 2):
        brr1.append([min(arr1[i], arr1[i + 1]), max(arr1[i], arr1[i + 1])])
    
    brr2 = []
    for i in range(0, 2 * m, 2):
        brr2.append([min(arr2[i], arr2[i + 1]), max(arr2[i], arr2[i + 1])])
    
    anss = set()
    crr1 = [[False, False] for _ in range(n)]
    crr2 = [[False, False] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            if brr1[i][0] == brr2[j][0] and brr1[i][1] != brr2[j][1]:
                crr1[i][0] = True
                crr2[j][0] = True
                anss.add(brr1[i][0])
            if brr1[i][0] == brr2[j][1] and brr1[i][1] != brr2[j][0]:
                crr1[i][0] = True
                crr2[j][1] = True
                anss.add(brr1[i][0])
            if brr1[i][1] == brr2[j][0] and brr1[i][0] != brr2[j][1]:
                crr1[i][1] = True
                crr2[j][0] = True            
                anss.add(brr1[i][1])
            if brr1[i][1] == brr2[j][1] and brr1[i][0] != brr2[j][0]:
                crr1[i][1] = True
                crr2[j][1] = True                        
                anss.add(brr1[i][1])
             
    ans = -2   
    for i in crr1:
        if i == [True, True]:
            ans = -1
            break
        
    for i in crr2:
        if i == [True, True]:
            ans = -1
            break
    
    if ans == -1:
        print(-1)
    else:
        if len(anss) == 1:
            print(*anss)
        else:
            print(0)