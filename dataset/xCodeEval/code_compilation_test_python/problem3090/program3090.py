def program3090():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_h = alphabet.upper()
    alpha = tuple(alphabet)
    alpha_h = tuple(alphabet_h)
    n = int(input())
    s = str(input())
    g = 0
    i = 1
    
    while i <= n-1:
      if s[i-1] in alpha:
        while s[i] in alpha_h:
         # print(s[i], i)
          g = g + 1
          i = i + 1
       #   print(i)
          if i>=n-1 or s[i] in alpha:
            break      
      i = i + 1
    i = n - 1
    if s[n-1] in alpha_h and g > 0:
      while s[i] in alpha_h and i>=0:
        g = g - 1
        i = i - 1
    if n = 1 and s[0] in alpha:
      g = 1
                        
    print(g)