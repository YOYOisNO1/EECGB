def program3612():
    string = input().split(' ')
    num = int(string[0])
    t = int(string[1])
    queue = input()
    
    if num == 1:
        print(queue)
    else:
        ans = ''
        for sec in range(0, t):
            switch = False
            if ans != '':
                queue = ans
                ans = ''
    
            for i in range(0, num-1):
                if switch == True:
                    switch = False
                elif queue[i] == 'B' and queue[i+1] == 'G':
                    ans += 'GB'
                    if i == num-3:
                        ans += queue[-1]
                        break
                        
                    switch = True
                else:
                    if i == num - 2:
                        ans += queue[-2] + queue[-1]
                        break
                    ans += queue[i]
        print(ans)