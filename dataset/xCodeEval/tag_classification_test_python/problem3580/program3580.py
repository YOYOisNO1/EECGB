def program3580():
    x,y=[int(x) for x in input().split()]
    a=input()
    for i in range(1,y+1):
        if 'BG' in a:
            a=a.replace('BG','GB')
            
    print(a)