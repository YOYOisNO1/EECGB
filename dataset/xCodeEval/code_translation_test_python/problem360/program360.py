def program360():
    n=input()
    s=input()
    l=s.split()
    min=1
    for t in range(1,n):
        if l[t]==l[0]:
            min+=1
    for i in range(1,n):
        temp=1
        for j in range(i+1,n):
            if l[j]==l[i]:
                temp+=1
        if temp>min:
            min=temp
    print(min)
            
            
            
        