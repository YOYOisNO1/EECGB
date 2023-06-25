def program1126():
    import math
    
    c=int(input())
    sum=c
    while c>1:
        signal=False
        for i in range(2,int(math.sqrt(c)+1):
            if c%i==0:
                c=c//i
                signal=True
                break
        if signal==False:
            c=1
        sum+=c
    print(sum)
            