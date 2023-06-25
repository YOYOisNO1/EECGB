def program1250():
    n=int(input())
    x=input()
    s=0
    while x[0]!="+":
        x=x[1:]
        if len(x)==0:
            break
    for i in range(len(x)):
        if x[i]=="+":
            s+=1
        else:
            s-=1
            if s==-1:
                s=0
    
    print(s)