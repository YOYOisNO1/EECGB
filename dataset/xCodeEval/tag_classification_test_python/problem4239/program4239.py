def program4239():
    for i in range(8):
        s = list(input())
        for i in range(7):
            if s[i] == s[i+1]:
                print('NO')
                exit()
    
    
    print('YES')