def program1607():
    
    
    s = input()
    
    produceOutput = False
    
    for c in s:
      if c == 'H' or c == 'Q' or c == '9':
        produceOutput = True
    
    if produceOutput:
      print("YES")
    else:
      print("NO")  