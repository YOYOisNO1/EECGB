def program4215():
    t = int(input())
    
    nums = []
    for i in xrange(t):
        cur_c = 0
        cur_s = input().split()
        cur_n = map(long, cur_s)
        for n in xrange(cur_n[0], cur_n[1]+1):
            s = str(n)
            digits = set(s)
            flag = True
            for d in digits:
                if d == '0':
                    continue
                if n % int(d) != 0:
                    flag = False
                    break
            if flag:
                cur_c += 1
    #        
    #        if '2' in digits:
    #            if not (s[-1] in ('0', '2', '4', '8')):
    #                continue
    #        if '3' in digits:
    #            if not sum(map(int, s)) % 3 == 0:
    #                continue
    #        if '4' in digits:
    #            if not int(s[-2:]) % 4 == 0:
    #                continue
    #        if '5' in digits:
    #            if not (s[-1] == '5' or s[-1] == '0'):
    #                continue
    #        if '6' in digits:
    #            if '2' not in digits:
    #                if not (s[-1] in ('0', '2', '4', '8')):
    #                    continue
    #            if '3' not in digits:
    #                if not sum(map(int, s)) % 3 == 0:
    #                    continue
    #        if '7' in digits:
    #            if not abs(int(s[-2]) - int(s[-1])*2) % 7 == 0:
    #                continue
    #        if '8' in digits:
    #            if not int(s[-3:]) % 8 == 0:
    #                continue
    #        if '9' in digits:
    #            if not sum(map(int, s)) % 9 == 0:
    #                continue
    #        cur_c += 1
        print cur_c    
        