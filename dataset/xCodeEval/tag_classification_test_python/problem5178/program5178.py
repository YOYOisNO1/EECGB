    #!/usr/bin/env python
    
    [n, l, r] = map(int, input().split())
    
    
def find_length(nr):
      if (nr <= 1):
        return 1
      else:
        return 1+2*find_length(nr/2)
    
def range_sum(nr, length, l, r):
      if (nr == 0):
        return 0
      elif (nr == 1):
        if (r >= l):
          return 1
        else:
          return 0
      else:
        result = 0
        length = length / 2
        if (l <= length) and (length <= r):
          result = result + (1 if (nr % 2 == 1) else 0)
        if (l < length):
          result = result + range_sum(nr/2, length, l, min(r, length))
        if (r > length/2):
          result = result + range_sum(nr/2, length, max(0,l-length-1), r-length-1)
        return result
    
    print(range_sum(n,) find_length(n), l-1, r-1)