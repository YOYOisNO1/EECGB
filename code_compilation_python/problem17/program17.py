def program17():
    n=int(input())
    sr=input()
    sr=sr[::-1]
    final=list()
    for i in sr:
        i=int(i)
        if i not in final:
            final.append(i)
    count=0
    #final=list(set(z))
    print(final)
    #final.sort(reverse=True)
    for i in final:
        count=count+1
    print(count)
    final.reverse()
    for i in final:
        print(i,end=' ')