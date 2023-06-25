def program288():
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    
    px = 0
    py = 0
    ans = 0
    
    cnt = 0
    while cnt < n:
        if strings[0].split()[1] != "South":
            ans = "NO"
            break
    
        if strings[cnt].split()[1] == "South":
            py += int((strings[cnt].split())[0])
        if strings[cnt].split()[1] == "North":
            py -= int((strings[cnt].split())[0])
        if strings[cnt].split()[1] == "West":
            px += int((strings[cnt].split())[0])
        if strings[cnt].split()[1] == "East":
            px -= int((strings[cnt].split())[0])
    
        if cnt != n-1:
            if int(py) % 40000 == 0 and int(px) % 40000 == 0 and strings[cnt+1].split()[1] != "South":
                ans = "NO"
                break
            if int(py) % 40000 == 20000 and int(px) % 40000 == 0 and strings[cnt+1].split()[1] != "North":
                ans = "NO"
                break
    
    
        cnt += 1
    
    if int(py) % 40000 == 0 and ans != "NO":
        ans = "YES"
    else:
        ans = "NO"
    
    print(ans)