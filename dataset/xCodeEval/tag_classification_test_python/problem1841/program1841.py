def program1841():
    n, m = map(int, input().split())
    a = 0
    div = m/n
    
    while div % 2 == 0:
          a += 1
          div /= 2
    while div % 3 == 0:
          a += 1
          div /= 3
    if div == 1:
          print(a)
    else:
          print("-1")