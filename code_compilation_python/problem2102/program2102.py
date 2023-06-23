def program2102():
    A = list(map(int,input().split()))
    i = 0
    ab = []
    while i != 16:
        ab.append((A[i],A[i+1]))
        i += 2
    ab = sorted(ab,key=lambda tup: tup[0])
    if (ab[3][0] != ab[5][0]) and (ab[3][0] == ab[4][0]) :
        if ((ab[3][0] != ab[3][1]) and (ab[4][0] != ab[4][1]))  and (ab[0][0] == ab[1][0] == ab[2][0]) and (ab[5][0] == ab[6][0] == ab[7][0]) and (ab[0][1] != ab[1][1] != ab[2][1]!= ab[0][1]) and (ab[5][1] != ab[6][1] != ab[7][1]!= ab[5][1]):
            print('respectable')
        else:
            print("ugly")
    else:
        print("ugly")
    #complecity  O(nlogn)