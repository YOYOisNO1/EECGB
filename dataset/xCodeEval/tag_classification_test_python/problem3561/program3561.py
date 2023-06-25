def GirlsFirst(queue,queue_length):
        index = queue_length - 1
        while 1:
            if index - 1 >= 0:
                if queue[index] == 'G' and queue[index-1] == 'B':
                    queue[index] = 'B';queue[index-1] = 'G'
                    index -= 1
            else:
                break
            index -= 1
        return queue
    queue_length,time = map(int,input().split())
    queue = list(input());
    for i in range(time):
        queue = GirlsFirst(queue,queue_length)
    print("").join(map(str,queue))