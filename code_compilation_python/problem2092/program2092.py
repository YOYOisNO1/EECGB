def program2092():
    n = (int)input()
    mylist = input().split(' ')
    # mylist = [1, 2, 3, 4]
    mylist.sort()
    tmp = mylist[0]
    lenn = len(mylist)
    mylist[0] = mylist[lenn-1]
    mylist[lenn-1] = tmp
    print mylist