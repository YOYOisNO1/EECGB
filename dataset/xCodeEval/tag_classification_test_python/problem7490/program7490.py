def f(mx, tot):
      while tot < 0 or tot > mx:
        if tot > mx:
          tot = 2 * mx - tot
        else:
          tot *= -1
      return tot
    a, b, m = map(int, input().split())
    vx, vy, vz = map(int, input().split())
    tm = m / -vy
    print(f(a, a / 2 + vx * tm), f(b, vz * tm))