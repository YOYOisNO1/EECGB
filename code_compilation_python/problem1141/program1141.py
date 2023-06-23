def program1141():
    
    if __name__ == '__main__':
      a = int(input())
      b = int(input())
      c = int(input())
    
      ans = 0 
      first = 0
      if a != 1 and b != 1:
        first = a*b
      else:
        first = a+b
      if c != 1:
        ans = first*c
      else:
        ans = first+c
      print(ans