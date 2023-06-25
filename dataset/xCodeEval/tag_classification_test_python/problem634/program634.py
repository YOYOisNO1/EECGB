def program634():
    Number = input()
    Points = map(int, input().split())
    Points.sort()
    Length = len(Points) - 2
    for i in range(Length):
        if Points[i]+Points[i+1] > Points[i+2]:
            value= 1
            break
        else:
            value = 0
    if value == 1:
        print("YES")
    else:
        print("NO")