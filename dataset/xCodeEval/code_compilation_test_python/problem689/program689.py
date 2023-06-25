def program689():
    n = input()
    a = map(int, input().split())
    up , down = 'UP', 'DOWN'
    if a[-1] == 15:
      print down
    elif a[-1] == 0:
      print up
    elif n==1:
      print -1
    else
      print up if a[-1]>a[-2] else down