def program3643():
    string = input().split(' ')
    num = int(string[0])
    t = int(string[1])
    queue = input()
    ans = ''
    
    for sec in range(0, t):
        switch = False
        if ans != '':
            queue = ans
            ans = ''
        if num == 1:
            ans = queue
            break
        for i in range(0, num-1):
            if switch == True:
                switch = False
            elif queue[i] == 'B' and queue[i+1] == 'G' and i == num-3:
                ans += 'GB' + queue[-1]
                break
            elif queue[i] == 'B' and queue[i+1] == 'G':
                ans += 'GB'
                switch = True
            elif i == num-2:
                ans += queue[i] + queue[i+1]
                break
            else:
                ans += queue[i]
    
    print(ans)