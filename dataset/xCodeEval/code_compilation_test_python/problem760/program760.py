def f(t, s, x):
      return x == t or x >= t + s and (x - t) % s <= 1
    
    t, s, x = map(int, input().split())
    print("YES") if f(t, s, x) else "NO"