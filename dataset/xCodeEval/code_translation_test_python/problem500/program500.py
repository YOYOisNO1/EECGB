def program500():
    a, b, c=map(int, input().split())
    print(a*b+b*c+a*c-a-b-c+1)