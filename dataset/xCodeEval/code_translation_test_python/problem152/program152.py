def program152():
    n = int(input())
    s = input().split(' ')
    M = 0
    for word in s:
        c = 0
        for char in word:
            if char.isupper():
                c += 1
        M = max(c, M)
    print(M)