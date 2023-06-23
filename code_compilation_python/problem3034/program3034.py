    import sys
    from time import time
    
    line=sys.stdin.readline().strip('\n')
    k=int(sys.stdin.readline().strip('\n'))
    
def isRepeat(inp):
        if len(inp)%2==1:
             return False
        else:
            for i in xrange(0,len(inp)/2):
                if inp[i]!=inp[i+len(inp)/2]:
                    return False
        return True
    
        
def findTandemRepeat(inp):
        remove=0
        while(remove<len(inp)):
            for i in xrange(0,remove+1):
                temp=inp[i:len(inp)-remove+i]
                if isRepeat(temp):
                    return len(inp)-remove
            remove+=1
        return 0       
    
    if k<=len(line):  
        best=0
        for i in range(0,len(line)-k+1):
            #print (line + line [i:i+k])
            best=max(best,findTandemRepeat(line + line[i:i+k]))
    
        print best
    
    else:
        print str(2*((k+len(line))/2))