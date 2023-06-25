def program3189():
    string = str(input())
    l = len(string)
    ans = 0
    for i in range(l):
        for j in range(i + 1 , l):
            for k in range(1 , l):
                if i + k - 1 < l and j + k - 1 < l:
                    flag = True
                    for x in range(k):
                        if string[i + x] != string[j + x]:
                            flag = False
                            break
                    if flag == True and k > ans:
                        ans = k         
    print ans