def program4648():
    number, guard = map(int, input().split())
    
    line = input()
    
    record = [[-1, -1] for i in range(0, 26)]
    
    for i in range(0, len(line)):
        if record[ord(line[i]) - ord('A')][0] == -1:
            record[ord(line[i]) - ord('A')][0] = i
        if i > record[ord(line[i]) - ord('A')][1]:
            record[ord(line[i]) - ord('A')][1] = i
    
    F = True
    for i in range(0, len(line)):
        if i == record[ord(line[i]) - ord('A')][0]:
            guard -= 1
            if guard < 0:
                F = False
        if i == record[ord(line[i]) - ord('A')][1]:
            guard += 1
    
    if F:
        print('NO')
    else:
        print('YES')