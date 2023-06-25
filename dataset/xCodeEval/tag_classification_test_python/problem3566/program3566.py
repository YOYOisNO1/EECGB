def program3566():
    array = list(map(int, input().split(' ')))
    queue = input()
    
    n = array[0]
    t = array[1]
    item = 0
    queue = [i for i in queue]
    
    while item != t:
        i = 0
        while i <= n-2:
            if queue[i] == 'B' and queue[i+1] == 'G':
                queue[i],queue[i+1] = queue[i+1],queue[i]
                i += 2
            else:
                i += 1
        item += 1
    
    print(''.join(queue))