def program2281():
    playersstring=input()
    players=[]
    for i in range(len(playersstring)):
        players.append(int(playersstring[i]))
    num=1  
    listofnums=[]
    for i in range(len(players)-1):
      if players[i]==players[i+1]:
        num=num+1
        
      else:
        listofnums.append(num)
        
        num=1
    listofnums.append(num)
    if max(listofnums)>=7:
      print("YES")
    else:
      print("NO")  