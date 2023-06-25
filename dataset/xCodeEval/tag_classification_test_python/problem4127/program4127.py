def program4127():
    x=list(input())
    minx=[]
    for i in range(0,len(x)):
        minx.append('9' if i==0 and x[0]=='9' else min(x[i], str(9-int(x[i]))))
    print("".join(minx))