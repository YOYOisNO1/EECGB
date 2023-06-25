def program4581():
    if __name__ == '__main__':
        _in = input()
        __in = _in.split(' ')
        n = int(__in[0])
        k = int(__in[1])
        guests = input()
        end_guest = dict()
        for i, g in enumerate(guests):
            end_guest[g] = i
    
        now_open = 0
        max_open = 0
        open = dict()
        for i, g in enumerate(guests):
            if not open.get(g):
                now_open += 1
                max_open = max(now_open, max_open)
            open[g] = True
            if end_guest[g] == i:
                now_open -= 1
        print('YES') if max_open > k else 'NO'