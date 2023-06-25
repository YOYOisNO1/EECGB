def program577():
    a, b, c, d, x, y = map(int, input().split())
    print(sum(v) % a % b % c % d == v for v in range(x, y + 1))