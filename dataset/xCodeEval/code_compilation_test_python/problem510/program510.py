def program510():
    N = int(input())
    if N == 0:
        print("YES")
        print "1\n1\n3\n3"
    else:
        i = 0
        a = []
        mean = 0
        while i != N:
            o = int(input())
            a.append(o)
            mean += o
            i += 1
        x1, x4 = -1, -1
        for i, k in enumerate(a):
            for l in a[i:]:
                if k == 3 * l:
                    x1, x4 = l, k
                    break
                elif l == 3 * k:
                    x1, x4 = k, l
                    break
        st = sorted(a)
        if N == 4:
            # just check stuff
            mean /= 4.0
            median = (st[1] + st[2]) / 2.0
            if mean == median:
                print("YES")
            else:
                print("NO")
        elif N == 1:
            # do something
            print("YES")
            print str(a[0]) + "\n" + str(3 * a[0]) + "\n" + str(3 * a[0])
        elif N == 3:
            if x1 != -1 and x4 != -1:
                x3 = 4 * x1 - st[1]
                print("YES")
                print str(x3)
        else:
            x1, x2, x3 = st[0], st[1], st[2]
            if x2 + x3 != 4 * x1:
                print("NO")
            else:
                x4 = x1 * 3
                mean = (x1 + x2 + x3 + x4) / 4.0
                median = (x2 + x3) / 2.0
                print("YES")
                print str(x4)
    else:
    if x1 != -1 and x4 != -1:
        # 2 sum between x1 and x4
        asum = 4 * x1
        r = range(x1, x4 + 1)
        flag = True
        for fx in r:
            find = asum - fx
            if find in r:
                x2, x3 = -1, -1
                if find < fx:
                    x2, x3 = find, fx
                else:
                    x2, x3 = fx, find
                print("YES")
                print str(x2)
                print str(x3)
                flag = False
                break
        if flag:
            print("NO")
    else:
        x1, x2 = st[0], st[1]
        x4 = 3 * x1
        x3 = 4 * x1 - x2
        if x3 >= 1 and x4 >= 1:
            print("YES")
            print str(x3)
            print str(x4)
        else:
            print("NO")