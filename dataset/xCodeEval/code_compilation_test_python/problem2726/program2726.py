def program2726():
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        a.append(i)
        b.append(i)
    for j in range(n):
        for k in range n:
            if a[j]==b[k]:
                count+=1
    print(count)            
        
        