def program6825():
    from math import *
    
    k = int(input())
    s = [c for c in input()]
    n = len(s)
     
    v = [0 for i in range(26)]
     
    for i in range(ceil(n/2)):
        if s[i] != "?" and s[n-i-1] != "?":
            if s[i] != s[n-i-1]:
                print("IMPOSSIBLE")
                exit()
            else:
                v[ord(s[i])-97] += 1
        elif s[i] == "?" and s[n-i-1] != "?":
            s[i] = s[n-i-1]
            v[ord(s[i])-97] += 1
        elif s[i] != "?" and s[n-i-1] == "?":
            s[n-i-1] = s[i]
            v[ord(s[i])-97] += 1
     
    # print(*v)
    # print(*s)
     
    l = k-1
    for i in range(n//2, -1, -1):
        while l > 0 and v[l] > 0:
            l -= 1
        if s[i] == "?" and s[n-i-1] == "?":
            s[i] = chr(l + 97)
            s[n-i-1] = chr(l + 97)
            v[l] += 1
        
    for i in range(k):
        if v[i] == 0:
            print("IMPOSSIBLE")
            break
    else:
        print("".join(s))