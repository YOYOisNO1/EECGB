def program1608():
    s = input()
    t = input()
    
    s_clone = list(s)
    length = len(s)
    
    for i in range(length - 1, -1, -1):
      if ''.join(s_clone) > s and ''.join(s_clone) < t:
        print(''.join(s_clone))
        return
    
      dist = abs(ord(t[i]) - ord(s[i]))
      if dist > 0:
        if s[i] == 'z':
          s_clone[i] = 'a'
        else:
          s_clone[i] = chr(ord(s[i]) + 1)
    
    print('No such string')