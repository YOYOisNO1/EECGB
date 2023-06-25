def bit_diff(n, k):
      a = []
      b = []
      while n > 0:
        a.append(n % 2)
        n //= 2
      while k > 0:
        b.append(k % 2)
        k //= 2
      if len(a) < len(b):
        a, b = b, a
      if len(a) != len(b):
        b.append(0)
      ans = 0
      for i in range(len(a)):
        ans += a[i] != b[i]
      return ans
    n = input()
    val = input()[::-1]
    kl = int(val, 2)
    print (abs(bit_diff(kl, kl + 1))