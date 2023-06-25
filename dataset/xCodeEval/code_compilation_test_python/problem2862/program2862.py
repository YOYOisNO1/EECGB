def program2862():
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        if i%3==0:
            if i!=0:
            l[0]=l[0]+l[i]
        elif i%3==1:
            if i!=1:
            l[1]=l[1]+l[i]
        elif i%3==2:
            if i!=2:
            l[2]=l[2]+l[i]
    if l[0]==max(l):
        print('chest')
    elif l[1]==max(l):
        print('biceps')
    elif l[2]==max(l):
        print('back')
        