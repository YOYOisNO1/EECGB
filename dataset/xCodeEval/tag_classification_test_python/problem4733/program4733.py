def program4733():
    x = int(input())
    y = input()
    z = y.split()
    w = [int(d) for d in z]
    w.sort()
    m = []
    flag = False
    i = 0
    
    for num in w:
        if w.count(num + 1) != 0 and w.count(num + 2) != 0:
            flag = True
            
        else:
            continue
    if flag == True:
        print("YES")
    else:
        print("NO")
        