def program585():
    l = map(int,input().split(' '))
    l.sort()
    result  =  sum(l)/3
    if l[1]+l[0]<result:
        result = l[1]+l[0]
    print(result)