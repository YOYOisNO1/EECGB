def program791():
    ch=input()
    l=[]
    l=ch.split()
    m=int(l[0])
    d=int(l[1])
    if m in [1,3,5,7,8,10,12]:
        if d in [1,2,3,4,5]:
            print(5)
        else:
            print(6)
    elif m in [4,6,9,11]:
        if d in [1,2,3,4,5,6]:
            print(5)
        else:
            print(6)
    elif m=2 :
        if d=1:
            print(4)
        else :
            print (5)