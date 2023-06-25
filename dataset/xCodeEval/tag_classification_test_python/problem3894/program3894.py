def program3894():
    n=int(input())
    
    mas=list(map(int,input().split()))
    
    for i in range(n):
        while mas.count(mas[i])>1 and mas[i]>0:
            mas[i]-=1
    print(sum(mas))