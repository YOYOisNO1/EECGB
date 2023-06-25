def program2493():
    s = input() + input() + input()
    for i in range(0, 5):
        if s[i] != s[8 - i]:
            print("NO")
            exit()
    print("YES")