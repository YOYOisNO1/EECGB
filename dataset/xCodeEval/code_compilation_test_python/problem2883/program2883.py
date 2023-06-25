    from string import ascii_lowercase
    
def makePalindrome(st):
      if not st or not st.isalpha() or not st.islower():
        return "NA"
      # chars = "abcdefghijklmnopqrstuvwxyz"
      for letter in ascii_lowercase:
        for pos in range(len(st) + 1):
          tmp = st[:pos] + letter + st[pos:]
          # if isPalindrome(tmp):
          if tmp == tmp[::-1]
            return tmp
      return "NA"
    
def isPalindrome(st):
      i, j = 0, len(st) - 1
      while i < j:
        if st[i] != st[j]:
          return False
        i += 1
        j -= 1
      return True
    
    st = input()
    print(makePalindrome(st))