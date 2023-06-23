    tar=input()
    n=int(input())
    A=[]
    for i in range(n):
        A.append(input())
    
def ct(A,tar):
        if tar in A:
            return 'YES'
        a1,a2=False,False
        for x in A:
            if x[1]==tar[0]:
                a1=True
            if x[0]==tar[1]:
                a2=True
        if a1==True and a2==True:
            return 'YES'
        else:
    
    print ct(A,tar)