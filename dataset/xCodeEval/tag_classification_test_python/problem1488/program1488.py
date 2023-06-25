def program1488():
    #!/usr/bin/env python3 
    
    import itertools
    
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']
    
    n = [notes.index(n) for n in input().strip().split()]
    
    for (X,Y,Z) in itertools.permutations(n):
      d1 = Y-X
      if (d1 < 0):
        d1+=12
      d2 = Z-Y
      if (d2 < 0):
        d2+=12
      if (d1 == 4) and (d2 == 3):
        print("major")
        exit()
      if (d1 == 3) and (d2 == 4):
        print("minor")
        exit()
    
    print("strange")