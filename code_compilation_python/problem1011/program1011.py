def program1011():
    n = int(input())
    if n/10 < 1:
        print(1)
    else:
        n = str(n)
        f = len(n) - 1
        b = int(str(len(n)) + "0"*f)
        print(n - b)