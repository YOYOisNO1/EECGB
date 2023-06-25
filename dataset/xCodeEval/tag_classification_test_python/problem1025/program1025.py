def program1025():
    n = int(input())
    a1,a2,a3 = [int(i) for i in input().split()]
    b1,b2,b3 = [int(i) for i in input().split()]
    maxi = min(a1,b2) + min(a2,b3) + min(a3,b1)
    mini = max(0, b1-a1-a2, b2-a2-a3, b3-a3-a1)
    print(mini,maxi)