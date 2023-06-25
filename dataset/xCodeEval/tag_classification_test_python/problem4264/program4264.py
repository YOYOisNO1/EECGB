def program4264():
    a, b, c, d, e, f = map(int, input().split(' '))
    want = -1
    listSticks = [a, b, c, d, e, f]
    for value in listSticks:
        if listSticks.count(value)>= 4:
            want = value
    if want>0:
        listSticks.remove(want)
        listSticks.remove(want)
        listSticks.remove(want)
        listSticks.remove(want)
        if (listSticks[1] == listSticks[0]):
            print("Elephant")
        else:
            print("Bear")
    else:
        print("Alien")