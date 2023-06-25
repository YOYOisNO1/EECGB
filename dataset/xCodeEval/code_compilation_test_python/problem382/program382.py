def program382():
    n = int(input())
    fat,b = map(int, input().split(' '))
    bad,d = map(int, input().split(' '))
    dead,f = map(int, input().split(' '))
    
    while fat + bad + dead < n and fat < b:
        fat +=1
        
    while fat + bad + dead < n and bad < d:
        bad +=1
        
    while fat + bad + dead < n and dead < f:
        dead +=1
        
    print fat, bad, dead