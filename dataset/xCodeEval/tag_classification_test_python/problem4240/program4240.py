def task(input):
        for line in input:
            line = [item for item in line if item in ['W', 'B']]
            if line.count('W') != line.count('B'):
                return "NO"
    
            for i in range(0, len(line) - 1):
                if not((line[i] == 'W' and line[i + 1] == 'B') or (line[i] == 'B' and line[i + 1] == 'W')):
                    return "NO"
    
        return "YES"
    
    input = [str(input()) for i in range(8)]
    print(task(input))