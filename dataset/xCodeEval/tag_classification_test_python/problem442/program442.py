def program442():
    a1,a2,a3,a4 =sorted(map(int,input().split()))
    if(a1+a2>a3 or a2+a3>a4):
        print("TRIANGLE")
    elif(a1+a2==a3 or a2+a3==a4):
        print("SEGMENT")
    else:
        print("IMPOSSIBLE")