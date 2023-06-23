def program1728():
    W,Y=[i for i in input().split(" ")]
    Z=max(W,Y)
    num=(7-Z)
    if num%6==0:
        print("1/1")
    elif num%3==0:
        print("%s/2",%(num/3))
    else num%2==0:
        print("%s/3",%(num/2))