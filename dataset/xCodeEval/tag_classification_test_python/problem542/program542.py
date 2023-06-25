def program542():
    n = int(input())
    
    lost = 3
    plays = [1,2]
    
    ans = 'YES'
    
    for i in range(n):
        c = int(input())
        try:
            plays.remove(c)
            new_lost = plays[0]
            plays = [c, lost]
            lost = new_lost
        except:
            ans = 'NO'
            break
    print(ans)