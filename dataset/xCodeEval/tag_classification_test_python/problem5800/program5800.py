def program5800():
    n = int(input())
    a = map(int, input().split())
    print('Bob') if 2*a.count(min(a)) > n else 'Alice'