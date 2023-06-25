def program4483():
    a = int(input())
    b = int(input())
    c = []
    for i in range(a):
        d = int(input())
        c.append(d)
    
    print(max(max(c),(-(-(sum(c)+b)//len(c)))), max(c)+b)