def program3857():
    from __future__ import print_function
    n = input()
    l = filter(lambda x : len(x)!= 0,input().split('W'))
    print((len(l)))
    for i in l :
        print(len(i),end = ' ')