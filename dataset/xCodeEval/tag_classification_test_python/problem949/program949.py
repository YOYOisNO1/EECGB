def program949():
    n=int(input())
    Ar,As,Ap=map(int,input().split())
    br,bs,bp=map(int,input().split())
    print(n-(min(As,n-bp)+min(Ap,n-br)+min(Ar,n-bs)),min(bp,As)+min(Ap,br)+min(Ar,bs))