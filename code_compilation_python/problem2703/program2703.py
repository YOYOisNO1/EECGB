def program2703():
    import sys
    
    a, b = sys.stdin.readline().strip().split()
    a, b = int(a), int(b)
    
    mas = []
    
    while b>=a:
        mas += [b]
        if b % 2 == 0:
            b=b/2
        elif b%10==1
            b=(b-1)/10
        elif a != b:
            print("NO")
            exit(0)
    mas.reverse()
    
    if a==mas[0]:
        print("YES")
        print len(mas)
        print " ".join(map(str, mas))
    else:
        print("NO")
    
    