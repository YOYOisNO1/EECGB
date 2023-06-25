def program497():
    import sys
    S_1=input()
    S_2=input()
    for I in range(len(S_1)):
        if not S_1[I]==S_2[len(S_2)-1-I]:
            print'NO'
            sys.exit()
    print'YES'