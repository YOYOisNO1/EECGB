def program2253():
    nParticipantes = int(input())
    n = input().split(' ')
    notas = []
    for e in n:
        notas.append(e)
    c = 0
    lts = []
    for i in notas:
        if int(i) > 0:
            if i not in lts:
                c += 1
                lts.append(i)
    print(c)