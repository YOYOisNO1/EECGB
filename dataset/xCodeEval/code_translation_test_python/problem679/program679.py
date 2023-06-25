def program679():
    from itertools import groupby
    s = input().strip()
    cnt = 0
    for x,y in groupby(s):
      cnt += ((len(list(y)) & 1)^1)
    print(cnt)