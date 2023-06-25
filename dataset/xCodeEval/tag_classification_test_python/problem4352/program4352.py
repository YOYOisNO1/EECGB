def program4352():
    
    
    x = input()
    x = list(x)
    li = []
    r = l = 0
    if len(x) % 2 == 0:
        a = len(x) // 2 - 1
        li.append(x[a])
    else:
        a = len(x) // 2
        li.append(x[a])
        
    
    for i in range(len(x) - 1):
        if i % 2 == 0:
            r += 1
            li.append(x[a + r])
        else:
            l += 1
            li.append(x[a - l])
            
    print(''.join(li))
            