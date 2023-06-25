def func():
        f = input()
        m = input()
        s = input()
        test = {'F':f, 'M':m, 'S':s}
        r = 'rock'
        p = 'paper'
        sc = 'scissors'
        rn = 0
        pn = 0
        sn = 0
    
        if (f == m and f == s and m == s) or (f != m and f != s and m != s):
            return print('?')
    
        for i in test.values():
            if i == r:
                rn += 1
            elif i == p:
                pn += 1
            else:
                sn += 1
    
        if rn == 2 and sn == 1 or sn == 2 and pn == 1 or pn == 2 and rn == 1:
            return print('?')
        else:
            if test['M'] == test['F']:
                print('S')
            elif test['F'] == test['S']:
                print('M')
            else:
                print('F')
    
    func()