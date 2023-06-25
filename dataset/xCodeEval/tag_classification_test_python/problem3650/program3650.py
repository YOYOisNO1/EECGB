    import re
    
def getcleanint():
        cleanstr =re.split(' ',input())
        cleanint=[]
        for i in range(0,len(cleanstr)):
           cleanint.append(int(cleanstr[i]))
        return cleanint
    
    lst=getcleanint()
    n=lst[0]
    t=lst[1]
    queue=list(input())
    
    
    for x in range(0,t):
        i=0
        while 1==1:
            if(i>=n-1):
                break
            if(queue[i]=="B" and queue[i+1]=="G"):
                queue[i],queue[i+1]=queue[i+1],queue[i]
                i+=2
            else:
                i+=1
    
    final=""
    for i in range(0,n):
        final+=queue[i]
    print(final)