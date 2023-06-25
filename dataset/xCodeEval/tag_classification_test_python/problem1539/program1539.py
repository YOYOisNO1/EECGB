def program1539():
    s = list(input())
    t = list(input())
    k = 0
    
    for i in range(len(t)):
        if t[i] == s[k]:
            k+=1
    
    print(k+1)