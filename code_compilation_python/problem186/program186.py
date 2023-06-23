def program186():
    s=input()
    s=s.split()
    y=int(s[0])
    x=int(s[1])
    x-=1
    if x>0:
        y-=x
        x=0
    if y<0:
        print('No')
    elif y%2==0:
        print('Yes')
    else:
        print('No')