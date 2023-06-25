    from sys import stdin, stdout
    from itertools import imap
    import Queue
    
    lenQueue, times = imap(int, stdin.readline().split())
    children = stdin.readline()
    
    '''
    ppalQueue = Queue.Queue()
    boysQueue = Queue.Queue()
    
    
def printQueue(queue):
        allItems = ""
        while not queue.empty():
            allItems += queue.get()
        return allItems
    
    
    for eachTime in range(times):
        for boy in children:
            if boy is 'B' and boysQueue.empty():
                boysQueue.put(boy)
            elif boy is 'B' and not(boysQueue.empty()):
                ppalQueue.put(boy)
            elif boy is 'G' and not(boysQueue.empty()):
                ppalQueue.put(boy)
                ppalQueue.put('B')
                boysQueue.queue.clear()
            elif boy is 'G' and boysQueue.empty():
                ppalQueue.put(boy)
        if not(boysQueue.empty()):
            ppalQueue.put(boysQueue.get())
        children = printQueue(ppalQueue)
    stdout.write(children)
    '''
    for eachTime in range(times):
        children = children.replace('BG', 'GB')
    stdout.write(children)