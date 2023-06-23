def program3161():
    from math import acos, pi
    n, R, r = map(float, input().split())
    if r > R:
      print("NO")
    elif r > R / 2:
      print("YES") if n == 1 else "NO"
    else
      a2, c2 = (R - r) ** 2, (2 * r) ** 2
      angle = acos(1 - (c2/(2*a2)))
      print("YES") if n * angle <= 2 * pi else "NO"