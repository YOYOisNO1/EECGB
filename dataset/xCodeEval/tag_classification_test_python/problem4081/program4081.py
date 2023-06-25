def program4081():
    n = int(input())
    k = n % 7
    maxi = 0
    mini = 0
    if k == 0:
        print((n) / 7)*2, (n / 7)*2
    if k == 1:
        print((n) / 7)*2, (n / 7)*2 + 1
    if k > 1 and k < 6 :
        print((n) / 7)*2, (n / 7)*2 + 2
    if k > 5:
        print((n) / 7)*2 + 1, (n / 7)*2 + 2
    