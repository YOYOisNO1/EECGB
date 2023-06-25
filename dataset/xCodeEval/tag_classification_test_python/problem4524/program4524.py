def program4524():
    n = int(input())
    
    c, out = 2, n
    while (c * c <= n):
        if out%c**2==0:
            out//=c
        else:
            c+=1
    print(out)