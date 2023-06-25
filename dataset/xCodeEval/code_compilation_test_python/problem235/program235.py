def program235():
    n=""
    r=0
    c=0
    l=int(input())
    n=input()
    if(len(n)==l):
        for i in range(0,l-1):
            if(n[i]==n[i+1]):
                r=1
                c=c+r
            else:
                r=0
        print c