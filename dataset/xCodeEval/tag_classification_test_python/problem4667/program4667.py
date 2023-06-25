def program4667():
    n,k = map(int,input().split())
    s = input()
    guests = {}
    we_gooch = True
    for letter in s:
      if letter not in guests:
        guests[letter] = 1
      else:
        guests[letter] += 1
    unique_doors = set()
    for letter in s:
      unique_doors.add(letter)
      if len(unique_doors) > k:
        we_gooch = False
      guests[letter]-=1
      if guests[letter] == 0:
        unique_doors.remove(letter)
    if we_gooch:
      print('NO')
    else:
      print('YES')