def program2811():
    from __future__ import print_function
    import sys
    it = iter(sys.stdin.read().splitlines())
    n = int(next(it))
    lista =[int(x) for x in next(it).split()]
    f = -1
    move = True
    i = 0
    while(i < (len(lista) - 1)):
        if (f == 0):
            if (lista[i] == lista[i + 1]):
                i += 1
            else:
                if (lista[i] < lista[i + 1]):
                    move = False
                    break
                f += 1
        elif (f == -1):
            if (lista[i] < lista[i + 1]):
                i += 1
            else:
                f += 1
        else:
            if(lista[i] > lista[i+1]):
                i += 1
            else:
                move = False
                break
    if(move):
        print("YES")
    else:
        print("NO")