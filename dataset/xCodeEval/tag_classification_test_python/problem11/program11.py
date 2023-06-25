def program11():
    NM = input()
    N = int(NM.split(" ")[0])
    M = int(NM.split(" ")[1])
    if M == 1:
        print(N-1)
    else:
        print((N) * (M -1))