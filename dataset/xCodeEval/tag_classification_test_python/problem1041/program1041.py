def program1041():
    n=int(input())
    a1,a2,a3=[int(num) for num in input().split()]
    b1,b2,b3=[int(num) for num in input().split()]
    c1=min(a1,b2)
    c2=min(a2,b3)
    c3=min(a3,b1)
    c4=max(0,a1-(b3+b1))
    c5=max(0,a2-(b1+b2))
    c6=max(0,a3-(b2+b3))
    print(max(c4,c5,c6),c1+c2+c3)