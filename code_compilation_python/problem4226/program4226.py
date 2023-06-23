def program4226():
    fin = open('input.txt', 'r')
    p = '.!?:-,;()'
    for i in fin.readlines():
        s = i.strip().split()
        cnt = 0
        for word in s:
            Set = set()
            for c in word:
                if c in p: continue
                Set.add(c)
            if 0 < len(Set) <= 3:
                cnt += 1
        print(i, cnt)
        if cnt < len(s) / 2:
            print(i)