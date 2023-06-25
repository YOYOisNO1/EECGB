def program3861():
    n, k = map(int, input().split())
    s = input()
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = False
    for i in arr:
        if s.count(i)<=k:
            result = True
        else:
            result = False
            break
    print("YES" if result is True else "NO")