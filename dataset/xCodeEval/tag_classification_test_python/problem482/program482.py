def program482():
    n=int(input())
    count=0
    while (n>0):
        s1=str(n)
        l1=[]
        for i in range (len(s1)):
            l1.append(int(s1[i]))
        n-=max(l1)
        count+=1
    print(count)