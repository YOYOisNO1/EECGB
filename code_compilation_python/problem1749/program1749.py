def program1749():
    verh='qwertyuiop'
    centr='asdfghjkl;'
    niz='zxcvbnm,./'
    n=input()
    a=input()
    nomervstroke=0##нужныйИндексВ строке
    if n=="R":##если нажал правее
        for i in range(len(a)):
            if a[i] in verh:
                nomervstroke=verh.find(a[i])-1
                print(verh[nomervstroke],end='')
            elif a[i] in centr:
                nomervstroke=centr.find(a[i])-1
                print(centr[nomervstroke],end='')
            else:
                nomervstroke=niz.find(a[i])-1
                print(niz[nomervstroke],end='')
    else:##если нажал левее
        for i in range(len(a)):
            if a[i] in verh:
                nomervstroke=verh.find(a[i])+1
                print(verh[nomervstroke],end='')
            elif a[i] in centr:
                nomervstroke=centr.find(a[i])+1
                print(centr[nomervstroke],end='')
            else:
                nomervstroke=niz.find(a[i])+1
                print(niz[nomervstroke],end='')