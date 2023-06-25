def program5065():
    n = int(input())
    m = int(input())
    
    if n > m or 2**n > m:
        print(m)
    else:
        print(m%(2**n))