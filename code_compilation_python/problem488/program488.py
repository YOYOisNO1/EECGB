def program488():
    inp = input().strip().split()
    amount=inp[0]
    coins=inp[1:]
    
    d={}
    if amount==0:
        return 0
    ans=[]
    queue=[]
    queue.append(amount)
    d[amount]=1
    level=0
    l = len(queue)
    while queue:
        remaining=queue.pop()
        l-=1
        for i in coins:
            tmpRemaining=remaining-i
            if tmpRemaining == 0:  ans.append(level+1)
            if tmpRemaining not in d and tmpRemaining > 0:
                queue.insert(0,tmpRemaining)
                d[tmpRemaining]=1
    
        if l == 0:
            l=len(queue)
            level+=1
    
    if not ans:
        print(-1)
    else: print(max(ans))
                    