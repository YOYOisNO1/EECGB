def program797():
    #data = open("P1.txt")
    x,t,a,b,da,db = map(int,input().split())
    found = False
    for i in range(t):
        if max(0,a-da*i)==x:
            print("YES")
            found = True
            break
        
        for j in range(t):
            #print(i,j,max(0,a-da*i),) max(0,b-db*j)
            if max(0,a-da*i) + max(0,b-db*j) == x or max(0,b-db*j) == x:
                print("YES")
                found = True
                break
        if found:
            break
        
    if not found:
        if x!=0:
            print("NO")
        else:
            print("YES")
            