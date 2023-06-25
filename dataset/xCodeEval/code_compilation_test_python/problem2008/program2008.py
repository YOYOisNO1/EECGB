def program2008():
    
     import time
    s=input().split()
    L=[]
    for i in range(1,len(s)):
        L.append(int(s[i]))
    L.sort()
    for x in L:
        time.sleep(1.98/len(L))
        print(str(x), end=" ")