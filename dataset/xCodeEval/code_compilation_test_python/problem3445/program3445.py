def program3445():
    n = int(input())
    numbers = set()
    nn = ""
    for _ in range(n):
        a = int(input())
        numbers.add(a)
        nn += str(a)
    first = nn.count(str(numbers.pop()))
    second = nn.count(str(numbers.pop()))
    if len(numbers) != 2 or first != second:
        print("NO")
    else:
        print("YES")
        print(*numbers