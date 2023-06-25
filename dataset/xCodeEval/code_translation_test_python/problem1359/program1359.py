def program1359():
    n=int(input())
    k=sum(list(map(int,str(n))))
    while k%4!=0:
        n+=1
        k=sum(list(map(int,str(n))))
    print(n)