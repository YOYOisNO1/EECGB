def program2601():
    n=int(input().strip())
    a=[int(i) for i in input().strip().split()]
    x=0
    r=0
    for i in a:
        if i==0 or (x xor i)==0:
            x=0
            r+=1
        else:
            x= x xor i
    print(r)