def program699():
    players = {1, 2, 3}
    not_playing = 3
    cases = int(input())
    trial = cases
    for x in range (cases):
      winner = int(input())
      if winner == not_playing: 
        print(("NO"))
        break
      for y in players:
        if y != winner and y!= not_playing: 
          not_playing = y
          break
      trial -= 1
    if trial == 0: print("YES") 