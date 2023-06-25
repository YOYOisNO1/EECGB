def program786():
    import os, sys
    
    if __name__ == "__main__":
      a, b = map(int, input().split())
      res = b * b * (b - 1) * a * (a + 1) / 4
      res += a * b * (b - 1) / 2
      print(res) % 1000000007