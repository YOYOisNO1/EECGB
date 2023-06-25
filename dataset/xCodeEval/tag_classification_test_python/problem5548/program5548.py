def program5548():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    count = 0
    if n >= a and n < b:
        count = n / a
    if n < a and n >= b:
        count = (n - b) / (b - c) + 1
    if n >= a and n >= b:
        if a <= b - c:
            count = n / a
        else:
            count = (n - b) / (b - c) + 1
        n -= count * (b - c)
        if n >= a:
            count += n / a
    print(count)