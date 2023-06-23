    #Eight Point Sets
    
    class point:
    def __init__(self, x = 0, y = 0):
            self.x = x
            self.y = y
    
    
    x = []
    y = []
    a = []
    for i in range(8):
        u, v = map(int, input().split())
        a.append(point(u, v))
        if u not in x:
            x.append(u)
        if v not in y:
            y.append(v)
    
        if len(x) > 3 or len(y) > 3:
            print("ugly")
            exit()
    
    x.sort()
    y.sort()
    a.sort(key=lambda p: (p.x, p.y))
    # for i in range(len(a)):
    #     print("{} {}".format(a[i].x, a[i].y), end=" ")
    k = 0
    flag = True
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if a[k].x != x[i] or a[k].y != y[j]:
                flag = False
            k += 1
    
    
    if flag:
        print("respectable")
    else:
        print("ugly")