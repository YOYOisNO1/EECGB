def program3872():
    lights = input().strip()
    
    l = []
    for c in lights:
      if c == "!":
        l += [{"R":1, "B":1, "Y":1, "G":1}] 
      else:
        l += [{c:0}]
    
    invalid = True
    while invalid:
      invalid = False
      for i in range(len(l)):
        if len(l[i]) > 1:
          for j in range(-3, 4):
            if i+j>=0 and i+j<len(l) and i+j!=i:
              other = l[i+j]
              if len(other) == 1:
                for key in other.keys():
                  if key in l[i]:
                    del l[i][key]
          if len(l[i])>1:
            invalid = True
    
    counts = {"R":0, "B":0, "Y":0, "G":0}
    for el in l:
      for k in el:
        if el[k] == 1:
          counts[k] += 1
    
    print("{} {} {} {}".format(counts["R"],counts["B"],counts["Y"],counts["G"],))
    