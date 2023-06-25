def program514():
     n = int(input())
    A = sorted([int(input()) for _ in range(n)])
    if   n == 4:
        print("YES") if sum(A)/4.0 == (A[1]+A[2])/2.0 == (A[3]*1.0-A[0]) else "NO"
    elif n == 3:
        for d in range(sum(A)/4,10**6+1):
            na = sorted(A[:]+[d])
            if sum(na)/4.0 == (na[1]+na[2])/2.0 == (na[3]*1.0-na[0]):
                print "YES\n%s"%i
                break
            if sum(na)/4.0 < na[3]*1.0-na[0] or d == 10**6:
                print("NO")
                break
    elif n == 2:
        for i in range((sum(A)+2)/4,10**6+1):
            a,b,c = sorted(A+[i])
            d = 5*a+b+c
            if d%3 != 0: continue
            a,b,c,d = sorted([a,b,c,d/3])
            if (b+c)/2.0 == d*1.0-a:
                print "YES\n%s\n%s"%(c,d)
                break
            elif (b+c)/2.0 < d*1.0-a or d > 10**6 or c == 10**6:
                print("NO")
                break
    elif n == 1:
        print "YES\n%s\n%s\n%s"%(A[0],3*A[0],3*A[0])
    else:
        print "YES\n%s\n%s\n%s\n%s"%(1,1,3,3)