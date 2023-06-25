def program1205():
    for _ in [0]*int(input()):
        l=input()+input()
        x=l.count('1')
        if x==4: print(2)
        elif x>0: print(1)
        else: print(0)