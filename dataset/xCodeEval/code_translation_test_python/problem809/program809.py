def program809():
    x,k=map(str,input().split())
    k=int(k)
    x=list(x)
    z=pow(10,k)
    x.reverse()
    m=0
    l=x.count('0')
    if(l==0):
        print(len(x))
    elif(l>0 and l<k):
        print(len(x)-1)
    else:
        for i in range(len(x)):
            if(x[i]=='0'):
                m+=1
                if(m==k):
                    s=i
                    break
        print(i-k+1)