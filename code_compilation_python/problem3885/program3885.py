def program3885():
    from sys import stdin, stdout
    import math
     
    n = int(stdin.readline())
    ans = n
    for i in range(2, int(math.sqrt(n))+1):
        t = int(math.log(n, i))
        if t!=0:
            ans -= (t-1)
     
    if ans % 2 == 0:
        stdout.write("Petya"+'\n')
    else:
        stdout.write("Vasya"+"\n")