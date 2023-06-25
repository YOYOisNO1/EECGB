def program2394():
    s=input()
    c4=c7=0
    for c in s:
        if c == '4':
            c4+=1
        elif c == '7':
            c7+=1
    if c4==0 and c7==0:
        print(-1)
    elif c4>=c7:
        print(4)
    else:
        print(7)