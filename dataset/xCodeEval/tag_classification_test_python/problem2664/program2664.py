    s = list(input())
def check(s):
      for i in range(len(s)-2):
        
        if set(s[i:i+3])=={'A','B', 'C'}:
          return('Yes')
      return('No')
    print(check(s))