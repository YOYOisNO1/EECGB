def program3574():
      n = int(input())
      c = map(int,input().split())
      x,y = map(int,input().split())
      sumc = 0
      
      for i in range(n):
        sumc += c[i]
        if x <= sumc and sumc<=y and x<=sum(c)-sumc and sum(c)-sumc <= y:  
          print(i+2)
          return
      print(0)