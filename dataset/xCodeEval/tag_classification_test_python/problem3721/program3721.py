def program3721():
    freqOfA, minSpentA = [int(x) for x in input().split()]
    freqOfB, minSpentB = [int(x) for x in input().split()]
    departTime = input().split(":")
    departTime, Currdepart, encounters, KMA = 60 * int(departTime[0]) + int(departTime[1]), 5 * 60, 0, 0 #departure time of the first bus
    
    while True:
        if Currdepart >= departTime + minSpentA or Currdepart > 23*60+59: break
        if Currdepart + minSpentB > departTime:
            encounters += 1
        Currdepart += freqOfB
    print(encounters)