def program40():
    a1,a2,a3,a4=sorted(int(i) for i in input().split())
    if((a1+a4==a2+a3) or (a1+a2+a3==a4)):
        print("YES")
    else:
        print("NO")