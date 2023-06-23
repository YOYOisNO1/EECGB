    import sys
    
def main():
      n, k = map(int, input().split())
      b = list(map(int, input().split()))
      bs = [[], [], []]
      s = input()
      for i in range(n):
        ind = -1
        if s[i] == 'O':
          ind = 0
        elif s[i] == 'R':
          ind = 1
        else:
          ind = 2
        bs[ind].append(b[i])
      bs[0].sort()
      bs[1].sort()
      bs[2].sort()
      if len(bs[0]) == 0 or len(bs[1]) + len(bs[2]) == 0 or len(bs[0]) + max(len(bs[1]), len(bs[2])) < k:
        print(-1)
        sys.exit(0)
    
      sufs = [0]
      for i in range(len(bs[0]) - 1, -1, -1):
        sufs.append(sufs[-1] + bs[0][i])
    
      ans = -1
      for i in (1, 2):
        x, y = bs[0], bs[i]
        if len(x) + len(y) < k:
          continue
        cursum = 0
        for cny in range(1, len(y) + 1):
          if cny > 0:
            cursum += y[-cny]
          cnx = k - cny
          if cnx > 0 and cnx <= len(x):
            ans = max(ans, cursum + sufs[cnx])
    
      print(ans)
    
    if __name__ == '__main__':
      main()