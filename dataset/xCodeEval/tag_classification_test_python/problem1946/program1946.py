def program1946():
    a, b, c = map(int, input().split())
    l = list(map(int, input().split()))
    li = list(map(int, input().split()))
    for i in range(1, a+1):
        if i in l:
            print(1, end=' ')
        elif i in li:
            print(2, end= ' ')