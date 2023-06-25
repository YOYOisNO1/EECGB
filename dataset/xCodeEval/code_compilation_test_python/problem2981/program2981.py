def program2981():
    a = ([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] + [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]) * 100
    
    b = map(int, input().split())
    
    for i in range(len(a)):
        if b == a[i:i + len(b)]:
            print("Yes")
            exit(0)
    
    print("No")