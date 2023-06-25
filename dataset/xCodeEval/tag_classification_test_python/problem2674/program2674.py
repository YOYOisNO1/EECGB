def program2674():
    l = list(map(int, input().split()))
    print(min((sum(l) - max(l))*2, sum(l)))