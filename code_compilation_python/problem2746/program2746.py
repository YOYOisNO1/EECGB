    br = open('b.in')
    a = map(int, br.readline().split(":"))
    b = map(int, br.readline().split(":"))
    d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    r = 0
def can(y):
      if y % 100 == 0 and y % 400 != 0:
        return 0
      return y % 4 == 0
def calc(a, b):
      r = 0
      for i in range(a[0], b[0] + 1):
        for j in range([0, a[1]][i == a[0]] + 1, [12, b[1] - 1][i == b[0]] + 1):
          r += d[j] + (j == 2 and can(i))
      if a[0] == b[0] and a[1] == b[1]:
        return b[2] - a[2]
      return r + b[2] + (d[a[1]] + (a[1] == 2 and can(a[1]))) - a[2]
    print max(calc(a, b), calc(b, a))