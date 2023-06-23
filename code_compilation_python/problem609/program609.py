def program609():
    n, m, a = map(int, input().split())
    print (n % a == 0 ? n: n % a + 1)*(m % a == 0 ? m: m % a + 1)