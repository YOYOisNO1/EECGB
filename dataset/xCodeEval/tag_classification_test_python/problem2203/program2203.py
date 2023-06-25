def program2203():
    a, b, s = [int(i) for i in input().split(" ")]
    if (abs(a)+abs(b)+s)%2 == 1 or abs(a)+abs(b) > s:
        print("No")
    else:
        print("Yes")