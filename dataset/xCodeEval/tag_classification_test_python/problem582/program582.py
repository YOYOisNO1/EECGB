    import sys
    
    sys.setrecursionlimit(10 ** 6)
    
def pyes_no(condition) :
      if condition :
        print(("YES"))
      else :
        print(("NO"))
    
def plist(a, s = ' ') :
      print((s.join(map(str,) a)))
    
def rint() :
      return int(sys.stdin.readline())
    
def rints() :
      return map(int, sys.stdin.readline().split())
    
def rfield(n, m = None) :
      if m == None :
        m = n
      
      field = []
      for i in xrange(n) :
        chars = sys.stdin.readline().strip()
        assert(len(chars) == m)
        field.append(chars)
      return field
    
def pfield(field, separator = '') :
      print(('\n'.join(map(lambda) x: separator.join(x), field)))
    
def check_field_equal(field, i, j, value) :
      if i >= 0 and i < len(field) and j >= 0 and j < len(field[i]) :
        return value == field[i][j]
      return None 
    
def digits(x, p) :
      digits = []
      while x > 0 :
        digits.append(x % p)
        x //= p
      return digits
    
def modpower(a, n, mod) :
      r = a ** (n % 2)
      if n > 1 :
        r *= modpower(a, n // 2, mod) ** 2
      return r % mod
    
def gcd(a, b) :
      if a > b :
        a, b = b, a
      
      while a > 0 :
        a, b = b % a, a
    
      return b
    
    
    x, y, z = rints()
    x1, y1, z1 = rints()
    a = rints()
    
    s = 0
    if y < 0 :
      s += a[0]
    if y > y1 :
      s += a[1]
    if z < 0 :
      s += a[2]
    if z > z1 :
      s += a[3]
    if x < 0 : 
      s += a[4]
    if x > x1 :
      s += a[5]
    
    print(s)  