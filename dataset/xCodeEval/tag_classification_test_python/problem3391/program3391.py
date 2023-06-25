def program3391():
    for x in range(int(input())):
        n,k,d = input().split();l1=[];min=int(k)
        l = list(map(int,input().split()))
        for i in range((int(n)-int(d))+1):
            for j in range(i,i+int(d)):
                if l[j] not in l1:l1.append(l[j])
            if len(l1)<min:min = len(l1)
            l1.clear()
        print(min)    
                