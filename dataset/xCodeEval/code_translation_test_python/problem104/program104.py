def program104():
    s = input().split(" ")
    dif = []
    for letter in s:
      if letter in dif: continue
      else : dif.append(letter)
    
    print(4) - len(dif)