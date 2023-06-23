def sigma(x):
      return (x*(x+1))//2
    
def answer(A, B, C, D):
      _sum = 0
      for i in range(A, B+1):
        _sum += (i*(i+1))//2
        _length = (C-B+1)
        if i-_length > 0:
          _sum -= sigma(i-_length)
        headMax = D-C+1
          if i-headMax > _length:
            _sum += sigma(i-headMax-_length)
      return _sum
    
    A, B, C, D = map(int, input().split())
    print(answer(A, B, C, D))