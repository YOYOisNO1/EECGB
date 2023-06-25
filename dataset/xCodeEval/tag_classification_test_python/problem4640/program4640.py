def program4640():
    from operator import itemgetter as it
    n, k = map(int, input().split())
    S = input()
    start = [-1] * 26
    end = [-1] * 26
    for i in xrange(n):
        c = S[i]
        num = ord(c) - 65
        if start[num] == -1: start[num] = i
        end[num] = i
    
    s = set()
    q = []
    for i in xrange(26):
        q.append((i, start[i], 's'))
        q.append((i, end[i], 'e'))
    q.sort(key=it(1))
    
    for ele in q:
        no, p, t = ele
        if t == 's':
            s.add((no, 'e'))
        else:
            s.remove((no, 'e'))
        if len(s) > k:
            print('YES')
            break
    else:
        print('NO')