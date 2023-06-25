def program2131():
    n = input()
    a = []
    for i in range(4): a += input()
    print("YES","NO")[max(a.count(i) for i in '0123456789')>2*k]