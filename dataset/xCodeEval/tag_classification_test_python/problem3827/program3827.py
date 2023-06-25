    #!/usr/bin/env python
    
    n = int(input())
    dice = []
    for i in xrange(n):
      faces = set(["%d" % f for f in map(int, input().split())])
      dice.append(faces)
    
def can_make(value, dice):
      if (value == ""):
        return True
      elif (len(dice) == 0):
        return False
      else:
        result = False
        d = 0
        while (d < len(dice)) and (not result):
          if value[0] in dice[d]:
            result = can_make(value[1:], [die for (i,die) in enumerate(dice) if (i != d)])
          d+=1
        return result
    
    result = 0
    while can_make("%d" % (result+1), dice):
      result+= 1
    
    print(result)