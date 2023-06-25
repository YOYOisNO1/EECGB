def program3797():
    n=int(input())
    if n>=0:
        print(n)
    else:
        k=str(n)
        k=k[1:]
        h=(k[len(k)-1])
        if h=="0":
            j=k[0:len(k)-2]
            w=j+"0"
            if w=="0":
                print(w)
            else:
                w="-"+w
                print(w)
        else:
            if k[len(k)-1]>k[len(k)-2]:
                p=len(k)-1
                l=k[0:p]
                l="-"+l
                print(l)
            else:
                g=k[0:len(k)-2]
                g= g+k[len(k)-1]
                g="-"+g
                print(g)