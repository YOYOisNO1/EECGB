def Main():
      n, l = map(int, input().split())
      A = list(map(int, input().split()))
      B = list(map(int, input().split()))
      L = []
      ans = False
      cnt = 0
      for i in range(l):
        # L.append((A[i] - B[i]))
        c = sorted(list(map(lambda x: (x + i)%l , B)))
        # print(c)
        if c == A:
          ans = True
          cnt += 1
      if ans:
        print("YES")
      else:
        print("NO")
      # print(L)
      # print(cnt)
      # print([ans])
      # print( ('NO', 'YES')[ans] )
    
      # if len(set(L)) == 1:
      #   print("YES")
      # else:
      #   print("NO")
    '''
    3 8
    2 4 6
    1 5 7
    '''
    
    if __name__ == '__main__':
      Main()