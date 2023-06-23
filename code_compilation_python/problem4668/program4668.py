    from sys import stdin, exit
    from random import randint
    
    
def no_solution():
        print 'NO'
        exit(0)
    
    inp = stdin.read().strip().split('\n')
    
    n, K = map(int, inp[0].split(' '))
    
    a = [0] + [0 for i in xrange(n)]
    b = [0] + [0 for i in xrange(n)]
    c = [0] + [0 for i in xrange(n)]
    
    active = [i + 1 for i in range(n)]
    
    for i in xrange(1, n + 1):
        a[i], b[i], c[i] = map(int, inp[i].split(' '))
    
    
    answer = []
    
    while K > 0:
        n = len(active)
        if K == 0 or len(active) == 0:
            break
        if n <= K:
            for i in xrange(n):
                answer.append((active[i], -1))
                K -= 1
            active = []
            break
    
        good = False
        best = (-1, -1)
        bsz = 10 ** 6
        for it in xrange(30):
            idx1 = randint(0, n - 1)
            idx2 = randint(0, n - 1)
            if idx1 == idx2:
                continue
    
            i = active[idx1]
            j = active[idx2]
    
            if a[i] * b[j] == a[j] * b[i]:
                continue
    
            x_high = c[j] * b[i] - c[i] * b[j]
            y_high = a[j] * c[i] - a[i] * c[j]
    
            low = a[i] * b[j] - a[j] * b[i]
    
            #answer.append((i, j))
            #K -= 1
    
            hh = 0
            for k in active:
                if k == i or k == j:
                    continue
                
                low_prime = a[k] * b[j] - a[j] * b[k]
                if low_prime == 0:
                    n_act.append(k)
                    continue
    
                x_high_prime = c[j] * b[k] - c[k] * b[j]
                y_high_prime = a[j] * c[k] - a[k] * c[j]
    
                if x_high * low_prime != x_high_prime * low or \
                        y_high * low_prime != y_high_prime * low:
                            hh += 1
    
            #active = n_act
            good = True
            if hh < bsz:
                bsz = hh
                best = (i, j)
    
        if not good:
            no_solution()
    
        i, j = best
        if i == -1:
            continue
    
        if a[i] * b[j] == a[j] * b[i]:
            continue
    
        x_high = c[j] * b[i] - c[i] * b[j]
        y_high = a[j] * c[i] - a[i] * c[j]
    
        low = a[i] * b[j] - a[j] * b[i]
    
        answer.append((i, j))
        K -= 1
    
        n_act = []
        for k in active:
            if k == i or k == j:
                continue
            
            low_prime = a[k] * b[j] - a[j] * b[k]
            if low_prime == 0:
                n_act.append(k)
                continue
    
            x_high_prime = c[j] * b[k] - c[k] * b[j]
            y_high_prime = a[j] * c[k] - a[k] * c[j]
    
            if x_high * low_prime != x_high_prime * low or \
                    y_high * low_prime != y_high_prime * low:
                        n_act.append(k)
        active = n_act
    
            
    if len(active) == 0 and K >= 0:
        print 'YES'
        print len(answer)
        for i in xrange(len(answer)):
            print '%d %d' % answer[i]
            assert(answer[i][0] != answer[i][1])
    else:
        no_solution()