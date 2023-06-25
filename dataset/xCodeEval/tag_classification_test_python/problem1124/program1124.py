def program1124():
    n=int(input());ar,asis,ap=map(int,input().split())
    br,bsis,bp=map(int,input().split())
    max = min(ar,bsis)+min(asis,bp)+min(ap,br)
    min = min(ar,n-bsis)+min(asis,n-bp)+min(ap,n-br)
    print(n-min,max)
    
                      