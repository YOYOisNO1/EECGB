def program1021():
    #!/usr/local/bin/python
    
    n = input()
    tmp = 1
    for i in xrange(n-1):
            tmp += (1 + i)
            tmp %= n
            if tmp == 0:print n,
            else: print tmp,
    [operin@panda 15:46:56 test] $ cat test.py
    #!/usr/local/bin/python
    import math
    n,m = map(int,input().split(" "))
    if n == 2 and m == 3:
            print("YES")
            exit()
    tmp = n
    while True:
            tmp += 2
            for i in xrange(2,int(round(math.sqrt(tmp)))+2):
                    if tmp % i == 0:
                            break
                    if tmp % i != 0 and i == int(round(math.sqrt(tmp)))+1:
                            if tmp == m: print("YES")
                            else: print("NO")
                            exit()