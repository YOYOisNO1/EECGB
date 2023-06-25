def program1449():
    # Author : code_marshal
    # cmp is not available in python 3.x
    
    a,b,c,d=map(int,input().split())
    ch=cmp(max(a*3//10,a-a*c//250),max(b*3//10,b-b*d//250))
    if not ch:print("Tie")
    elif ch==1:print("Misha")
    else:print("Vasya")