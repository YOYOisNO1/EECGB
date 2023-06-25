def program2010():
    input()
    f=lambda:ap(int,input().split())
    T,l=2**19,list(zip(f(),f()))
    print(sum(any(d%m==r for m,r in l) for d in range(T))/T)