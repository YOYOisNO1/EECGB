def soletrar(palavra):
        letras = []
        for a in range(len(palavra)):
            letras.append(palavra[a])
        return letras
    
    n, t = input().split(" ")
    n, t = int(n), int(t)
    nf = []
    b = input()
    f = soletrar(b)
    l = f
    m = ""
    
    if n == 1:
        m = m.join(f)
        print(m)
    else:
        for h in range (0, t):
            z = 0
            while z < len(l):
                z = int(z)
                if l[z] == "B":
                    if z == len(l)-1:
                        nf.append("B")
                    else:
                        if l[z+1] == "G":
                            nf.append("G")
                            nf.append("B")
                            z+=1
                        else:
                            nf.append("B")
                else:
                    nf.append ("G")
                z+=1
            l = nf
            nf = []
        m = m.join(l)
        print((m))
    