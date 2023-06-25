def program2525():
    s = str(input())
    
    d = s.split()
    lst = []
    
    for i in d:
        if i in lst:
            continue
        else:
            lst += [i]
    
    ans = 4 - len(lst)
    
    print(ans)