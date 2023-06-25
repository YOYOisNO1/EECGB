def program6807():
    n = int(input())
    add = [False for i in range(n)]
    # l = [int(i) for i in range(n)]
    s = input()
    v = []
    for i in range(len(s)):
        v.append(s[i])
        if s[i] != '?':
            add[ord(s[i])-97] = True
    if len(s)%2 == 1:
        i = len(s)//2
        j = len(s)//2
    else:
        i = (len(s)//2)-1
        j = len(s)//2
    # print(i, j)
    while i >= 0:
        if v[i] == '?':
            if v[j] == '?':
                id = -1
                for k in range(n-1, -1, -1):
                    if add[k] == False:
                        id = k
                        break
                else:
                    id = 0
                # print(i, j, id)
                v[i] = chr(id+97)
                v[j] = chr(id+97)
                add[id] = True
    
            else:
                v[i] = v[j]
        else:
            if v[j] == '?':
                v[j] = v[i]
            else:
                if v[i] != v[j]:
                    print("IMPOSSIBLE")
                    exit()
        i-=1
        j+=1
    
    # print(add)
    for i in range(n):
        if add[i] == False:
            # print("oi")
            print("IMPOSSIBLE")
            exit()
    
    for i in range(len(v)):
        print(v[i], end='')
    print()