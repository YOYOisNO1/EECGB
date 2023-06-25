def program1264():
    # cook your dish here
    b=int(input())
    g=int(input())
    n=int(input())
    
    if min(b,g,n)==n:
        print(n+1)
    elif max(b,g,n)==n:
        print(abs(n-g-b)+1)
    else:
        x=min(b,g)
        print(x+1)
                