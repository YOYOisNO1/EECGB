def program237():
    n=int(input())
    a=list(input())
    i=1
    while(i<len(a)):
        if a[i]==a[i-1]:
            a.pop(i-1)
    print(len(a))