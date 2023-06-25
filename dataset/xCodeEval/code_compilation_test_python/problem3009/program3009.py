def program3009():
        a = abs(int(input()))
        b = 0
        while a > 0 or a & 1:
            b += 1
            a -= b
        print(b)