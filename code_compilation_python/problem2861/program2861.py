def program2861():
    input()
    d = map(int, input().split())
    l = [[0,'chest'], [0,'biceps'], [0,'back']]
    for i, dd in enumerate(d):
      l[i%3][0] += dd
    print sorted(l, reverse=True)[0][1