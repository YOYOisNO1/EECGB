def program6574():
    from math import pi, sin
    n, R, r = map(int, input().split())
    print("YES"
          if (r < R or r == R and n == 1)
          and (n == 1 or n == 6 and 3*r == R or r/(R-r) <= sin(pi/n))
          else "NO")