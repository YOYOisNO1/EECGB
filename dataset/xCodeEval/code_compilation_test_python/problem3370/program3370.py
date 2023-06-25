def program3370():
    n, b = map(int, input().split())
    end = []
    res = []
    last_end = -1
    queue_size = 0
    for i in range(n):
        t, d = map(int, input().split())
        while end and t >= end[0]:
            end.pop(0)
            queue_size -= 1
        if last_end <= t:
            last_end = t+d
            res.append(last_end)
            end.append(last_end)
            queue_size += 1
        elif queue_size <= b:
            last_end = last_end+d
            res.append(last_end)
            end.append(last_end)
            queue_size += 1
        else:
            res.append(-1)
            end.append(-1)
    print ' '.join(map(str, res))