def program1548():
    a1,a2,a3,a4=map(int,input().split())
    if(a1+a3==a2+a4):
        print("YES")
    elif(a1+a4 == a2+a3):
        print("YES")
    elif(a1+a2==a3+a4 or a1=a2+a3+a4 or a2=a1+a3+a4 or a3 = a1+a2+a4 or a4=a1+a3+a2):
        print("YES")
    else:
        print("N0")