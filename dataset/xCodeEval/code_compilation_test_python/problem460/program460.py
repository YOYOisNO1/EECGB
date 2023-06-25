def program460():
    s = input()
    print(len(set(s[i:] + s[:i] for i in range(len(s)))))i