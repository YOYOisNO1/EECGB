def program47():
    l = lambda k:(- sum(map(int, input().split(' ')))/k)
    print('YNEOS'[l(50) + l(10) + input() < 0 ::2])