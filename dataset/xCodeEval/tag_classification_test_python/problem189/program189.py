def findMatching(teams):
        homes = []
        guests = []
        checked = []
        count = 0
        for team in teams:
            homes.append(str(team[0]))
            guests.append(str(team[1]))
    
        for home in homes:
            for guest in guests:
                if home == guest:
                    count +=1
        return count
    
    
    nums = int(input())
    teams = []
    for i in range(nums):
        listOfInputs = input().split()
        teams.append(listOfInputs)
    print(findMatching(teams))