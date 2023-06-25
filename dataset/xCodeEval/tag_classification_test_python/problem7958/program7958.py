def program7958():
    n = int(input())
    friends = [[] for i in xrange(n)]
    foes = [[] for i in xrange(n)]
    
    k = int(input())
    for i in xrange(k):
        a,b = map(int, input().split())
        friends[a-1].append(b-1)
        friends[b-1].append(a-1)
    
    f = int(input())
    for i in xrange(f):
        a,b = map(int, input().split())
        foes[a-1].append(b-1)
        foes[b-1].append(a-1)
    
    used = [False] * n
    out = 0
    
    while not all(used):
        i = used.index(False)
        used[i] = True
        fr_set = set()
        qq = [i]
        cur_res = 0
        while len(qq):
            elem = qq.pop(0)
            fr_set.add(elem)
            for friend in friends[elem]:
                if used[friend] == False:
                    qq.append(friend)
                    used[friend] = True
            for foe in foes[elem]:
                if foe in fr_set:
                    cur_res = -1
                    break
        if cur_res == -1:
            continue
        cur_res = len(fr_set)
        if out < cur_res:
            out = cur_res
    print(out)