def program418():
    n, m = map(int, input().split())
    l = map(int, input().split())
    
    a = [-1] * (n + 1)
    s = set()
    for i in range(1, n +1):
        s.update([i])
    flag = False
    for i in range(1, m):
        
        temp = l[i] - l[i - 1]
        if temp <= 0:
            temp = l[i] + n - l[i - 1]
            
        if a[l[i-1]] != -1 and a[l[i-1]] != temp:
            flag = True
            break
        
        if a[l[i-1]] != -1 and a[l[i-1]] == temp:
            continue
        if (temp not in s) and a[l[i-1]] == -1:
            flag = True
            break
        a[l[i-1]] = temp
        s.remove(a[l[i - 1]])
    if flag:
        print("-1")
    else:
        for i in range(1, n + 1):
            if a[i] == -1:
                a[i] = list(s)[0]
                s.remove(a[i])
        else:
            for i in range(1, n + 1):
                print(a[i],)
            