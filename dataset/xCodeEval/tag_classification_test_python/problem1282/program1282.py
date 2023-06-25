def program1282():
    a,b,c,d=map(int, input().split())
    summa=min(a,c,d)*256
    a-=min(a,c,d)
    summa+=min(a,b)*32
    print(summa)