def program2741():
    s = str(input())
    t = str(input())
    
    t = "".join(reversed(t))
    
    if (s==t):
        print(("YES"))
    else:
        print(("NO"))