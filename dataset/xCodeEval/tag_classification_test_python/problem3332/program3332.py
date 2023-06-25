def program3332():
    from sys import stdin, stdout
    
    l, r = stdin.readline().split()
    l, r = int(l), int(r)
    flag = False
    for i in range(l, r + 1):
        lista = list(str(i))
        flag = True
        for x in lista:
            if lista.count(x) > 1:
                flag = False
                break
        if flag:
            stdout.write(str(i)+"\n")
            break
    if not flag:
        stdout.write("-1\n")