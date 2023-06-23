def program3151():
    A = list(map(int, input().split()))
    cntOne = A.count(1)
    cntTwo = A.count(2)
    cntThree = A.count(3)
    cntFour = A.count(4)
    
    if cntOne >= 1 or cntTwo >= 2 or cntThree >= 3 or (cntTwo = 1 and cntFour = 2):
        print("YES")
    else:
        print("NO")