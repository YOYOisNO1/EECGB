def program3324():
    n = int(input())
    s = input()
    i = 0
    countS = 0
    countSF = 0
    while i < n-1:
        if s[i] == 'S' and s[i+1] == 'F':
            countS += 1
        if s[i] == 'F' and s[i+1] == 'S':
            countSF += 1
        i += 1
    if countS > countSF:
        print("YES")
    else:
        print("NO")