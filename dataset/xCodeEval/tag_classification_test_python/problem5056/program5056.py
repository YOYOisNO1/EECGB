def program5056():
    
    A,B=list(map(int,input().split()))
    Arreglo=list(map(int,input().split()))
    DIEZ=(A-1)*10
    TIEMPO=sum(Arreglo)
    TOTAL=TIEMPO+DIEZ
    if(TOTAL>B):
        print(-1)
    else:
        print((DIEZ/5)+(B-TOTAL)/5)