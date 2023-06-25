def program3329():
    """"
    inputString = input().split()
    n = int(inputString[0])
    m = int(inputString[1])
    a = int(inputString[2])
    
    n,m,a = input().split()
    
    if m % a == 0:
        m //= a
    else:
        m //= a
        m += 1
    
    if n % a == 0:
        n //= a
    else:
        n //= a
        n += 1
    
    #print(m * n)
    
    n = int(input())
    
    if n & 1 or n == 2:
        print("NO")
    else:
        print("YES")
    """""
    """""
    str = input()
    
    cnt = 0
    
    for i in range(len(str)):
    
    
        if cnt > i:
            break
    
    
        if ord(str[i]) <= 90:
            cnt+=1
        else:
            cnt-=1
    
    if cnt > 0:
        str = str.upper()
    else:
        str = str.lower()
    
    print(str)
    """""
    
    l, r = input().split()
    
    l = int(l)
    r = int(r) + 1
    
    nr = 0
    
    for i in range(l, r):
    
        v = [0] * 10
    
        for char in str(i):
            v[int(char)] += 1
    
        #print(v)
    
        ok = True
        for elem in v:
            if elem > 1:
                ok = False
                break
    
        if ok == True:
            nr = i
            break
    
    if nr:
        print(nr)
    else:
        print(-1)
    