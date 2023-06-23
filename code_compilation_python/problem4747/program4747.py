    n = int(input())
    cpts = [int(i) for i in input().split()]
    tasks = [set() for i in xrange(3)]
    for i in xrange(n):tasks[cpts[i]-1].add(i)
    depends = [set([int(j)-1 for j in input().split()][1:]) for i in xrange(n)]
    finish = set()
    
def do_task(pos, finish, tasks, depends):
        hours = 0
        while True:
            ns = set()
            for t in tasks[pos]:
                depends[t].difference_update(finish)
                ns.update(depends[t])
            d = tasks[pos].difference(ns)
            if len(d) == 0:break
            finish.update(d)
            tasks[pos].difference_update(d)
            hours += len(d)
        return hours
    
    hours = float('inf')
    for pos in xrange(3):
        h = 0
        t = [s.copy() for s in tasks]
        d = [d.copy() for d in depends]
        f = set()
        while True:
            h += do_task(pos, f, t, d)
            if len(f) >= n:break
            h += 1
            pos = (pos + 1) % 3
        hours = min(hours, h)
    print hours
        