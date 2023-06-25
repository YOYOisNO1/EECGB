def program2527():
    n=int(input())
    i=n+2
    j=2
    while j<i:
        j+=1
        if (j mod 2 == 0) and ((j div 2) mod 2 ==1):
            i+=1
    print(i)