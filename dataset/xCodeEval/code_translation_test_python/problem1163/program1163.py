def program1163():
    n = int(input())
    s = set()
    arr = list(map(int, input().strip().split()))
    for x in arr:
        if x != 0:
            s.add(x)
    print(len(s))