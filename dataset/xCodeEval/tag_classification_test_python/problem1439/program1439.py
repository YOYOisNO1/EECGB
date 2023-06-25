def program1439():
    n, m = map(int, input().split())
    bl = False
    for i in range(n):
        l = list(input().split())
        if 'C' in l or 'M' in l or 'Y' in l:
            bl = True
           
      
    
    if bl is True:
        print("#Color")
    else:
        print("#Black&White")