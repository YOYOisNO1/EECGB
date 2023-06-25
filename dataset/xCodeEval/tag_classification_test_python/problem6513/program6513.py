def program6513():
    import sys
    
    a, b, c = map(int, sys.stdin.readline().split())
    
    a = a % b
    
    to_divide = set()
    
    result = []
    
    while True:
        a *= 10
        while a < b:
            a *= 10
            result.append(0)
            if c == 0:
                print(len(result))
                sys.exit(0)
    
        if a in to_divide:
            print(-1)
            sys.exit(0)
    
        div = a / b
        result.append(div)
        to_divide.add(a)
        if c == div:
            print(len(result))
            sys.exit(0)
    
        a = a % b
        if a == 0:
            break
    
    if c == 0:
        print(len(result)) + 1
    else:
        print(-1)
    