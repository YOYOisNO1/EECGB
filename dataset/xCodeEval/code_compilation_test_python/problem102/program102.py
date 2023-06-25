    import sys
    
    numbers = map(int, sys.stdin.readline().split())
    
    start = numbers[0]
    end = numbers[1]
    
    
    
    lucky = [4, 7]
    
    for i in range(1, 10):
        for j in range(len(lucky)):
            lucky.append(int(str(lucky[j]) + "4"))
            lucky.append(int(str(lucky[j]) + "7"))
    
def nextfun(i):
        count = 0
        while i > lucky[count]:
            count +=1
            
        return lucky[count]
        
        
    answer = 0
    
    while(start <= end):
        answer += nextfun(start)
        start += 1
        
        
    print answer