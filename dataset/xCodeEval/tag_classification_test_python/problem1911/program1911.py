def program1911():
    a, b = map(int, input().split(':'))
    print(30*(a-12*(a>11)+b/60), 6*b)