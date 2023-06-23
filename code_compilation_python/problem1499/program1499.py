def program1499():
    n = list(map(int,input().split()))
    
    ar = []
    j = 1
    
    while n!=0:
     q = n[0]%n[1]
     n[0] //= n[1]
     n[0] = -1*n[0]
     #j += 1
     ar.append(q)
    
    print(len(ar))
    for i in range(len(ar)):
     print(ar[i])
    
    