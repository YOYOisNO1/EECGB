def main():
      n = int(input())
      l = list(map(int, input().split()))
      s = 0
      for i in range(1, n):
        if (l[i], l[i - 1]) in [(1, 1), (2, 3), (3, 2)]:
          print('Infinite')
          return
        elif 2 in (l[i], l[i - 1]):
          if i >= 2 and (l[i], l[i - 1], l[i - 2]) == (2, 1, 3):
            s += 2
          else:
            s += 3
        else:
          s += 4
      print("Finite")
      print(s)
      return
    
    
    main()