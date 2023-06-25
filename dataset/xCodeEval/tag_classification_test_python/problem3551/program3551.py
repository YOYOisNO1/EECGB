def getLines(num):
      inputLines = []
      for i in range(0,num):
        line = input()
        if line:
          inputLines.append(line)
        else:
            break
      return inputLines
     
def notZeroPow(num,p):
      return True if num >= 1 and num <= pow(10,p)  else False
     
     
    lines = getLines(2)
    t = int(lines[0].split()[1])
    s = []
    
    for c in lines[1]:
      s.append(c)
    
    con = False
    for n in range(t):
    
      for i , c in enumerate(s):
        if con:
          con = False
          continue
        if i+1 < len(s):
          if c == "B" and s[i+1] == "G":
            s[i] = "G"
            s[i+1] = "B"
            con = True
    
    final = ""
    for c in s:
      final += c
    
    print(final)