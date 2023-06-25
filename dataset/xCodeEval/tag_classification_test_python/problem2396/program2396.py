def program2396():
    n=list(input())
    count_4=n.count("4")
    count_7=n.count("7")
    if count_4 or count_7>0:
        if count_4>=count_7:
            print(4)
        else:
            print(7)
    else:
        print(-1)