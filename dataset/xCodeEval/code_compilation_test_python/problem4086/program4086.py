    import sys
    
    n=int(sys.stdin.readline().strip('\n'))
    line=sys.stdin.readline().strip('\n').split(' ')
    values=map(lambda x:int(x),line)
    
def evaluateBothSides(start,stop):
        print start,stop
        if stop-start==1:
            return min(values[start-1],values[stop])
        elif stop-start==0:
            return 0
        else:    
            maxNum=0
            maxPos=0
            for i in xrange(start,stop):
                if values[i]>maxNum:
                    maxPos=i
                    maxNum=values[i]
            return evaluateBothSides(start,maxPos)+evaluateBothSides(maxPos+1,stop)+min(values[start-1],values[stop])
    
def evaluateMax(stop):
        2+2
    
def evaluate(start,stop):
        2+2
        
    
def addToQueue(inp,queue):
        out=0
        if inp<queue[-1]:
            queue.append(inp)
        else:
            queue.pop()
            out+=inp
            while inp>queue[-1]:
                out+=queue.pop()
            queue.append(inp)
        return out
    
def queueEvaluate():
        maxLeft=0
        maxRight=0
        maxPos=0
        maxNum=0
        for i in xrange(0,n):
                if values[i]>maxNum:
                    maxPos=i
                    maxNum=values[i]
        out=0
        queue=[maxNum]
        for i in xrange(maxPos+1,n):
            out+=addToQueue(values[i],queue)
            #print queue
        if len(queue)==1:
            pass
        else:
            maxRight=queue[1]
            for i in xrange(2,len(queue)):
                out+=queue[i]
        queue=[maxNum]
        for i in xrange(maxPos-1,-1,-1):
            out+=addToQueue(values[i],queue)
            #print queue
        if len(queue)==1:
            pass
        else:
            maxLeft=queue[1]
            for i in xrange(2,len(queue)):
                out+=queue[i]
        out+=min(maxLeft,maxRight)
        return out
    
    print queueEvaluate()
            
                    