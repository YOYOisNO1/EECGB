def program3622():
    # http://codeforces.com/problemset/problem/431/B
    
    '''
    notice that first with second student, and second with the third will
    communicate one time, and third with fourth student, and fourth with fifth —
    will communicate two times. Another pairs of students will never communicate to
    each other during they stay in queue.
    '''
    
    from itertools import permuations
    q,t = 0, [list(map, int(input().split())) for i in range(5)]
    
    for a,b,c,d,e in permutaions([0,1,2,3,4]):
        s = t[a][b] +t[b][a] +t[b][c] +t[c][b] + 2*(t[c][d] + t[d][c] +t[d][e] + t[e][d])
        if s>q:
            q = s
    print(q)