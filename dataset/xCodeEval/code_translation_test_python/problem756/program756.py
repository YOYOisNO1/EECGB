def program756():
    #
    #   268A. Games
    #
    
    teams = int(input().strip())
    host = []
    guest = []
    for i in range(teams):
        h, g = map(int, input().strip().split())
        host.append(h)
        guest.append(g)
    
    count_matches = 0
    
    for g in guest:
        count_matches += host.count(g)
    
    print(count_matches)