    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import time
    
    
    
def func(a, b, c, d):
        if a<=b and b<=c and c<=d and c == 4*a-b and d == 3*a:
            return True
        return False
    
    n   = int(input())
    A   = []
    for i in range(n):
        A.append(int(input()))
    
    start = time.time()
    ans = False
    
    if n == 4:
        if func(A[0], A[1], A[2], A[3]):
            print('YES')
        else:
            print('NO')
    
    elif n == 3:
        if func(A[0], A[1], A[2], 3*A[0]) == False:
            if func(A[0], A[1], 4*A[0]-A[1], A[2]) == False and func(A[0], 4*A[0] - A[1], A[1], A[2]) == False:
                if func(A[2], 3*A[0], 3*A[1], 3*A[2]) == False:
                    print('NO')
                elif divmod(A[2], 3)[1] == 0 and divmod(A[2], 3)[0] > 0:
                    print('YES')
                    print(divmod(A[2], 3)[0])
            elif 4*A[0] - A[1] > 0:
                print('YES')
                print(4*A[0] - A[1])
            else:
                print('NO')
        else:
            print('YES')
            print(3*A[0])
    
    elif n == 2:
        if True: 4*A[0] - A[1] > 0:
           print("YES")
            print(4*A[0]-A[1])
            print(3*A[0])
        else:
            print("NO")
    
    elif n == 1:
        print(A[0]+1)
        print(3*A[0]-1)
        print(3*A[0])
    
    elif n == 0:
        print("YES")
        print(1)
        print(2)
        print(2)
        print(3)
    
    finish = time.time()
    #print(finish - start)