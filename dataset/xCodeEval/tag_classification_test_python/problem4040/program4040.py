def program4040():
    inp = input()
    counter = 0
    allInfo = inp.split()
    dist = []
    for i in range(4):
        allInfo[i] = int(allInfo[i])
    dist = allInfo[:3]
    neededDist = allInfo[3]
    dist.sort()
    if (dist[1] - dist[0])<neededDist:
        counter = counter+(neededDist-(dist[1] - dist[0]))
    if (dist[2] - dist[1])<neededDist:
        counter = counter+(neededDist-(dist[2] - dist[1]))
    print(counter)