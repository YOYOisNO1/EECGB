def program759():
    ab,bc,ca=[int(x) for x in input().split()]
    import math
    a=math.sqrt((ab*ca)/bc)
    b=math.sqrt((ab*bc)/ca)
    c=math.sqrt((bc*ca)/ab)
    print(int(4*(a+b+c)))