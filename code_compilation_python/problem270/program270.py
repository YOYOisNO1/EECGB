    m,s=map(int,input().split())
def f(intial,final,s,k):
        for i in range(initial,final+k,k):
            l=list(map(int,str(i)))
            if sum(l)==s:
                return l
        return -1
    print(f(pow(10,m-1),pow(10,m)-1,s,1),end=" ")
    print(f(pow(10,m)-1,pow(10,m-1),s,-1))
                