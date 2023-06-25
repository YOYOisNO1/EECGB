def bit_count(n):
      ans = 0
      while n > 0:
        ans += n % 2
        n //= 2
      return ans
    n = input()
    val = input()
    kl = int(val, 2)
    print (abs(bit_count(kl) - bit_count(kl + 1))