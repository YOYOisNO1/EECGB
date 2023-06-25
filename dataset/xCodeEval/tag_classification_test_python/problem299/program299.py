def program299():
    n = input()
    years = [int(s) for s in input().split()]
    print(sum(years) // int(n))