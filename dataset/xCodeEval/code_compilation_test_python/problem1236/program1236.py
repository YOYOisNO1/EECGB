def program1236():
    a, b, s = map(int, input().split())
    if((abs(s)-abs(a)-abs(b))>=0):
        if((abs(s-a-b)%2==0):
            print("Yes")
        else:
            print("No")
    else:
        print("No")