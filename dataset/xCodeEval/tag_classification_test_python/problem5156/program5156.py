    
def calculate_size(n):
      if n == 1 or n == 0:
        return 1
      return calculate_size(n/2) * 2 + 1
    
    
    # n = {0, 1}, l = 1, r = 1
def construct_array(n, l, r): 
      if r < l: 
        return []
      if n == 1 or n == 0:
        return [n]
      
      half_size = calculate_size(n/2)
      
      if r <= half_size:
        return construct_array(n/2, l, r)
      
      if l > half_size + 1:
        return construct_array(n/2, l - half_size - 1, r - half_size - 1)
      
      return construct_array(n/2, l, half_size) + [n%2] + construct_array(n/2, 1, r - half_size -1)
    
    
      
def count_ones(array):
      count = 0
      for i in array:
        count = count + i
      return count
    
    import sys
    
    for line in sys.stdin:
      x = line.split(' ')
      print(count_ones(construct_array(int(x[0]),) int(x[1]), int(x[2])))