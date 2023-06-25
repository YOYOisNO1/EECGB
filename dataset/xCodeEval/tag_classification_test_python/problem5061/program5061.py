def program5061():
    n = int(input(''))
    m = int(input(""))
    j = None
    if n >= 1 and n <= 10**8:
        if m >= 1 and n <= 10 ** 8:
            if n >= m or n >= 10 ** 7:
                print(m)
            else:
                ans = m % (2 ** n)
                print(ans)