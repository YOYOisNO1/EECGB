def program245():
    from sys import stdin,stdout
    ii1 = lambda: int(stdin.readline().strip())
    is1 = lambda: stdin.readline().strip()
    iia = lambda: list(map(int, stdin.readline().strip().split()))
    isa = lambda: stdin.readline().strip().split()
    mod = 1000000007
    
    n = is1()
    if int(n) < int('4' * len(n)):
        n = '4' * len(n)
    elif int(n) > int('7' * len(n)):
        n = '4' * (len(n) + 1)
    if len(n) % 2 != 0:
        n += '4'     
        
    while True:
        if set(list(n)) == set(['4', '7']) and n.count('4') == n.count("7"):
            print(n)
            break
        n = str(int(n) + 1)