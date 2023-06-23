    import sys
    sys.stdin = open('in.txt')
    from calendar import monthrange
    
    n = int(input())
    a = list(map(int, input().split(' ')))
    
def count_of_days(year, month):
      return monthrange(year, month)[1]
    
def solve(a):
      a29 = a.count(29)
      if a29 > 1:
        return 'NO'
    
      if a29 == 0:
        seq = []
        for year in range(2100, 2100+3):
          for month in range(1, 1+12):
            seq.append(count_of_days(year, month))
        return 'YES' if str.join(' ', map(str, a)) in str.join(' ', map(str, seq)) else 'NO'
    
      idx = a.index(29)
      year = 2000
      month = 2
      for i in range(idx-1, -1, -1):
        month -= 1
        if month == 0:
          month = 12
          year -= 1
        if count_of_days(year, month) != a[i]:
          return 'NO'
      year = 2000
      month = 2
      for i in range(idx+1, len(a)):
        month += 1
        if month == 13:
          month = 1
          year += 1
        if count_of_days(year, month) != a[i]:
          return 'NO'
      return 'YES'
    print(solve(a))
    
    
def generate(year, month, n):
      a = [0]*n
      for i in range(n):
        a[i] = count_of_days(year, month)
        month += 1
        if month == 13:
          month = 1
          year += 1
      return a
    