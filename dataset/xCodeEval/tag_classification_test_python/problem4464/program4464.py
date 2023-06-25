    suits = ['C', 'D', 'H', 'S', 'W']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    
def parse(c):
        if c == 'J1':
            return 52
        if c == 'J2':
            return 53
        return 13 * suits.index(c[1]) + ranks.index(c[0])
    
def summarize(cards):
        s = [0] * 4
        r = [0] * 13
        j1, j2 = False, False
        for i in cards:
            if i < 52:
                s[i // 13] += 1
                r[i % 13] += 1
            elif i == 52:
                j1 = True
            else:
                j2 = True
        return s, r, j1, j2
    
    n, m = map(int, input().split())
    board = [
        [parse(c) for c in input().split()]
        for _ in range(n)
    ]
    
    pack = set(range(54))
    for r in board:
        pack -= set(r)
    ps, pr, pj1, pj2 = summarize(pack)
    
    jc = [[0] * (m - 2) for _ in range(n - 2)]
    ji = [[False] * (m - 2) for _ in range(n - 2)]
    valid = [[False] * (m - 2) for _ in range(n - 2)]
    subs = [[None] * (m - 2) for _ in range(n - 2)]
    
    for ni in range(n - 2):
        for mi in range(m - 2):
            ss, sr, sj1, sj2 = summarize(
                board[ni + nj][mi + mj] for nj in range(3) for mj in range(3))
            if not sj1 and not sj2:
                if max(ss) == 9 or max(sr) == 1:
                    valid[ni][mi] = True
            elif sj1 and sj2:
                jc[ni][mi] = 2
                if max(ss) == 7:
                    ssi = ss.index(7)
                    for pi in pack:
                        if pi // 13 != ssi: continue
                        for pj in pack:
                            if pj == pi: continue
                            if pj // 13 != ssi: continue
                            subs[ni][mi] = [pi, pj]
                            valid[ni][mi] = True
                if max(sr) == 1:
                    for pi in pack:
                        if sr[pi % 13] == 1: continue
                        for pj in pack:
                            if pj % 13 == pi % 13: continue
                            if sr[pj % 13] == 1: continue
                            subs[ni][mi] = [pi, pj]
                            valid[ni][mi] = True
            else:
                jc[ni][mi] = 1
                ji[ni][mi] = 0 if sj1 else 1
                pc = set()
                if max(ss) == 8:
                    ssi = ss.index(8)
                    for p in pack:
                        if p // 13 == ssi:
                            pc.add(p)
                if max(sr) == 1:
                    for p in pack:
                        if sr[p % 13] == 0:
                            pc.add(p)
                if len(pc) > 0:
                    valid[ni][mi] = True
                    subs[ni][mi] = pc
    
def solve():
        for ni0 in range(n - 2):
            for mi0 in range(m - 2):
                if not valid[ni0][mi0]: continue
                for ni1 in range(n - 2):
                    for mi1 in range(m - 2):
                        if not valid[ni1][mi1]: continue
                        if (((ni1 >= ni0 and ni1 <= ni0 + 2)
                             or (ni0 >= ni1 and ni0 <= ni1 + 2))
                            and ((mi1 >= mi0 and mi1 <= mi0 + 2)
                             or (mi0 >= mi1 and mi0 <= mi1 + 2))):
                            continue
                        ja = [None, None]
                        if jc[ni0][mi0] == 0 and jc[ni1][mi1] == 0:
                            return True, (0, 0), ja, ((ni0, mi0), (ni1, mi1))
                        elif jc[ni0][mi0] == 1 and jc[ni1][mi1] == 1:
                            s0 = list(subs[ni0][mi0])
                            s1 = list(subs[ni1][mi1])
                            if len(s1) == 1 and s1[0] in s0:
                                    s0.remove(s1[0])
                            if len(s0) == 0:
                                continue
                            ja[ji[ni0][mi0]] = s0[0]
                            if s0[0] in s1:
                                s1.remove(s0[0])
                            ja[ji[ni1][mi1]] = s1[0]
                            return True, (1, 1), ja, ((ni0, mi0), (ni1, mi1))
                        elif jc[ni0][mi0] == 2:
                            ja = subs[ni0][mi0]
                        elif jc[ni1][mi1] == 2:
                            ja = subs[ni1][mi1]
                        elif jc[ni0][mi0] == 1:
                            ja[ji[ni0][mi0]] = list(subs[ni0][mi0])[0]
                        else:
                            ja[ji[ni1][mi1]] = list(subs[ni1][mi1])[0]
                        return True, (jc[ni0][mi0], jc[ni1][mi1]), ja, ((ni0, mi0), (ni1, mi1))
        return False, 0, [None, None], None
    
    v, jc, j, c = solve()
    if 52 in pack:
        pack.remove(52)
    if 53 in pack:
        pack.remove(53)
    if j[0] is not None:
        pack.remove(j[0])
    if j[1] is not None:
        pack.remove(j[1])
    if not pj1 and j[0] is None:
        j[0] = pack.pop()
    if not pj2 and j[1] is None:
        j[1] = pack.pop()
    for i in range(2):
        if j[i] is not None:
            j[i] = ranks[j[i] % 13] + suits[j[i] // 13]
    
    if not v:
        print('No solution.')
    else:
        print('Solution exists.')
        if pj1 and pj2:
            print('There are no jokers.')
        elif not pj1 and not pj2:
            print('Replace J1 with {} and J2 with {}.'.format(j[0], j[1]))
    
        elif not pj1:
            print('Replace J1 with {}.'.format(j[0]))
        else:
            print('Replace J2 with {}.'.format(j[1]))
        print('Put the first square to ({}, {}).'.format(c[0][0]+1, c[0][1]+1))
        print('Put the second square to ({}, {}).'.format(c[1][0]+1, c[1][1]+1))