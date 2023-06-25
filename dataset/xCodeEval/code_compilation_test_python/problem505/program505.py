def program505():
    n = input()
    for i in reversed(n) :
        k = int(i)
      if k < 5 :
        print('O-|' + 'OOOO'[:k] + '-' + 'OOOO'[:4-k])
      else : 
        k -= 5
        print('-O|' + 'OOOO'[:k] + '-' + 'OOOO'[:4-k])