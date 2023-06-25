def program1954():
    n = int(input())
    s = [input().strip() for _ in range(n)]
    w = ["minotaur", "theseus", "ariadne", "daedalus"]
    a = [False, False, False, False]
    for i in range(n):
      for j in range(n):
        for di in (-1, 0, 1):
          for dj in (-1, 0, 1):
            for l in range(4):
              ol True
              for k in range(len(w[l])):
                ol &= 0 <= i + k * di < n and 0 <= j + k * dj < n and s[i + k * di][j + k * dj] == w[l][k]
              a[l] |= ol
    if a[0] and not all(ai for ai in a[1:]):
      print("NO")
    else:
      print("YES")