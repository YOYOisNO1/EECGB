def program3690():
    a, b, r = map(int, input().split(' '))
    if 2*r <= a and 2*r <= b:
        print("First")
    else:
        print("Second")