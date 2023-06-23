def move(x, v, t):
          return [max(0.0, x[i] + v[i] * t) for i in range(3)]
    
def makeTurn():
          global x, v, m, a, b, eps
          turnTime = 10 ** 10
          time = (0.0 - x[0]) / v[0]
          if time > 0: turnTime = min(turnTime, time)
          time = (a - x[0]) / v[0]
          if time > 0: turnTime = min(turnTime, time)
          time = (b- x[2]) / v[2]
          if time > 0: turnTime = min(turnTime, time)
          time = (0.0 - x[2]) / v[2]
          if time > 0: turnTime = min(turnTime, time)
          time = (0.0 - x[1]) / v[1]
          if time > 0: turnTime = min(turnTime, time)
          next = move(x, v, turnTime)
          if abs(next[0]) <= eps or abs(next[0] - a) <= eps:
                v[0] = -v[0]
          if abs(next[2]) <= eps or abs(next[2] - b) <= eps:
                v[2] = -v[2]
          #print '%lf %lf' % (v[0], next[0])
          x = next
          return abs(x[1]) > eps
    
    a, b, m = map(int, input().split())
    eps = 1e-6
    v = map(int, input().split())
    x = (a * 1.0 / 2, m * 1.0, 0.0)
    while makeTurn():
          pass
    print x[0], x[2]