def program354():
    a, b = map(int, input().split())
    l1 = map(int, input().split())
    l2 = map(int, input().split())
    l1.sort()
    l2.sort()
    min1, min2 = l1[0], l2[0]
    minimum, maximum = min(min1, min2), max(min1, min2)
    if minimum in l1 and minimum in l2 :
        print minimum
    elif maximum in l1 and maximum in l2 :
        print maximum
    else :
        print str(minimum) + str(maximum)