def program1316():
    k = int(input())
    l = int(input())
    m = 0
    while(l-1):
        if l%k==0 :
            l = l/k
            m += 1
        else:
            break
    if l == 1 : 
        print("YES")
        print(m-1)
    else : print("NO")