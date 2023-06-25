def program3592():
    import string
    
    n, t = map(int, map(string.strip, input().split(' ')))
    queue = input()
    
    for time in range(t):
        for i, kid in enumerate(queue):
            if i != len(queue) - 1:
                if kid == 'B' and queue[i + 1] == 'G':
                    # print(queue,) "------", queue[:i], queue[i + 1:]
                    queue = queue[:i] + 'G' + queue[i + 1:]
                    # print(queue)
    
                    # print(queue[:i) + 1], queue[i + 2:], '55555555555000'
                    queue = queue[:i + 1] + 'B' + queue[i + 2:]
    
                    # print(queue,) "1111111111-----------------11111111"
    
    print(queue)