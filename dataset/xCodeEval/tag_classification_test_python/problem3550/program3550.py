def program3550():
    import sys
    
    number, time = map(int,sys.stdin.readline().split())
    string = input()
    queue = list(string)
    while (time > 0):
        isSwapped = []
        for j in range(number-1):
            
            if queue[j] == "B" and queue[j+1] == "G" and time >= 1 and j not in isSwapped and (j+1) not in isSwapped:
                temp = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp
                isSwapped.append(j)
                isSwapped.append(j+1)
                
        time -= 1
    
    print((''.join(queue)))
    
    