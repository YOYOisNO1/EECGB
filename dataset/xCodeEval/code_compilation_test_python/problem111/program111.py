def program111():
    a = input().strip()
    
    max_deep = 0
    
    l = -1
    
    for i in range(len(a)):
        if a[i] in ['A', 'E', 'I', 'O', 'U']:
            if i - l > max_deep:
                max_deep = i - l
            l = i
    
    if l == -1:
        max_deep = len(a) + 1
    
    print max_deep