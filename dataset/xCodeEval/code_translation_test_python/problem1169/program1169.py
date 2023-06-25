def program1169():
    trump = input()
    a, b = map(str, input().split())
    arr = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    if a[1] == b[1]:
        if arr.index(a[0]) > arr.index(b[0]):
            print("YES")
        else:
            print("NO")
    else:
        if a[1] == trump:
            print("YES")
        else:
            print("NO")