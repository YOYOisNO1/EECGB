def program1716():
    
    n = input()
    
    x = [int(x) for x in input().split()]
    x.reverse()
    l = []
    
    for i in x:
        if i not in l:
            l.append(i)
    
    print(len(l))
    l.reverse()
    
    for i in l:
        print(str(i) , end = ' ')