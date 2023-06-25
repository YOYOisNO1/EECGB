    import sys
    import operator
    import math
    
    #Check does input a prime number
def prime(n):
        for i in range(2,int(math.sqrt(n)+1)):
            if(n%i==0):
                return False
        return True
    
    #Read input and convert both numbers into integers
    inp = [int(p) for p in sys.stdin.readline().split()]
    
    frequency = {}
    """
    #out = [f for f in range(inp[0],inp[-1]+1)]
    
    for i in range(inp[0],inp[-1]+1):
        if not prime(i):
            for j in range(2,inp[-1]/2+1):
                if i%j == 0:
                    if j in frequency:
                        frequency[j] += 1
                    else:
                        frequency[j] = 0
                    
    
    print(max(frequency.iteritems(),) key=operator.itemgetter(1))[0]
    """
    if inp[0]==inp[-1]:
        print(inp[0])
    else:
        print(2)