def program1154():
    from sys import stdin, stdout
    
    info = map(int, stdin.readline().rstrip().split())
    jump = info[1]
    
    flowerPath = [int(n) for n in stdin.readline().rstrip()]
    
    jumps = 0
    
    current = 0
    final = len(flowerPath) - 1
    
    #print(flowerPath)
    breaking = False
    
    while current != final:
        for x in range(current + jump, current, -1):
            if x <= final and flowerPath[x] == 1:
                current = x
                jumps = jumps + 1
                break
            if x == current + 1:
                breaking = True
                break
        if breaking:
            break
    
    if breaking:
        stdout.write(str(-1) + "\n")
    else:
        stdout.write(str(jumps) + "\n")