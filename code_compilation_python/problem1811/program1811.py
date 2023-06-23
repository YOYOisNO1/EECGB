def solution (a, b, n):
    
        # traverse for all possible values
        i = 0
        _atual = i * a
        while _atual <= n:
            _atual = i * a
    
            # check if it is satisfying
            # the equation
            _res = n - (_atual)
            if _res % b == 0:
                if i < 0 or int(_res/b) < 0:
                    print("NO")
                    exit()
                print("YES")
                print i, int(_res / b)
                return 0
            i = i + 1
        print("NO")
    
    
    
    n = int(input())
    a = int(input())
    b = int(input())
    
    if a==1 or b==1:
        if a<b:
            print("YES")
            print n, 0
        else:
            print("YES")
            print 0, n
        exit()
    
    solution(a,b,n)
    