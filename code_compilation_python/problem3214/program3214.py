    import sys
    read=lambda:sys.stdin.readline().rstrip()
    readi=lambda:int(sys.stdin.readline())
    writeln=lambda x:sys.stdout.write(str(x)+"\n")
    write=lambda x:sys.stdout.write(x)
def tshirt(s):
        places = []
        i = (s // 50) % 475
        for _ in range(25):
            i = (i*96 + 42) % 475
            places.append(i+26)
        return places
    '''
    s는 승자의 point
    i = (s // 50) % 475
    for _ in range(25):
        i = (i*96 + 42) % 475
        print(i+26) 
    
    1~50 구간에 있는 애들은 다 같은데 떨어짐.
    
    '''
    
    '''
    p := place
    x := points
    y := 이기는데 필요한 점수
    '''
    p,x,y=map(int, read().split())
    unit = 50
    places = tshirt(x)
    if p in places:
        writeln(0)
        exit()
    mid = x
    mag = 1; found = False
    while mid - unit*mag >= y:
        places = tshirt(mid - unit*mag)
        if p in places:
            found = True
            break
        mag += 1
    
    if found:
        writeln(0)
        exit()
    
    mid = x
    mag = 1
    while True:
        places = tshirt(mid + unit*mag)
        if p in places:
            found = True
            break
        mag += 1
    
    answer = (mid + unit*mag) - x
    q,r=divmod(answer, 100)
    if r:
        writeln(q+1)
    else:
        writeln(q)