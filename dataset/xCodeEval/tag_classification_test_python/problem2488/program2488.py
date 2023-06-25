def program2488():
    s = input()+input()+input()
    # s = sirul care trebuie sal verificam daca e simetric
    # are 9 elemente ( 0 pana la 8 )
    # aplicam conditiile de simetrie
    
    if s[:3]==s[8:5:-1] and s[0::3]==s[8::-3] :
        print('YES')
        exit()
    print('NO')