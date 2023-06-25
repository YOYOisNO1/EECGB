    
def string_count (string='name', idx=0, num=100, end=100):
        flag = True
        for i in range (idx, end+1):
            if i+num >= len(string):
                flag = False; break
            if string[i] == string[i+num]:
                flag = True
            else:
                flag = False
                break
        return flag
    
    x = int(input())
    s = str(input())
    max = 0
    
    #for i in range (0, x-1):
    z = 1
    u = 0
    while 1:
      #u = 0
      v = s.find(s[0],z)
      if v < 0: break
      tmp = v - u
      r = string_count(s, 1, tmp, v-1)
      if tmp > max and r==True:
          max = tmp
      z = v+1
    
    if max > 0: max -= 1
    
    print((x) - max)