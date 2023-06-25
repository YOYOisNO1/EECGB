def program2231():
    num, denom, target = [int(x) for x in input().split()]
    a = num/denom
    if len(str(a)) < 100:
        a = '{:10.111f}'.format(a)
        a = a[a.find('.') :110]
    else a = str(a)
    print(a.find(str(target)))