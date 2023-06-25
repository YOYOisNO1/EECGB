def program2670():
    n=input()
    a=list(n[:2]);b=n[3:]
    if int(a[1]) not in [6,7,8,9]:
        if int(b)<int(''.join(a[::-1])):
            print(''.join(a)+':'+''.join(a[::-1]))
        elif int(''.join(a))==23:print("00:00")
        else:
            if a[1]=='5':
                a=str(int(a[0])+1)+'0'
                print(''.join(a)+':'+''.join(a[::-1]))
            else:
                a[1]=str(int(a[1])+1)
                print(''.join(a)+':'+''.join(a[::-1]))
    elif int(a[1]) in [6,7,8,9]:
        a=str(int(a[0])+1)+'0'
        print(''.join(a)+':'+''.join(a[::-1]))