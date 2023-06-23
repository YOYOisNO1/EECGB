def program3272():
    n = int(input())
    person = 3
    for i in range(n):
      win = int(input())
      if win == person:
    	print('NO')
    	exit()
      else:
    	person = 6 - person - win
    print('YES')