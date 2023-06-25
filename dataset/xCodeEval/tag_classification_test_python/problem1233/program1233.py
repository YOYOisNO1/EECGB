def program1233():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans1 = max(a)
    print(ans1, max([y for y in a if ans1 % y or a.count(y) > 1]))