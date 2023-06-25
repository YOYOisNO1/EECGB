def program2817():
    a=list(map(int,input().split()))
    
    for num in range(a[0],a[1]+1):
        ab=[]
        while(num>0):
            remaing=num%10
            ab.append(remaing)
            num=int(num/10)
        n=len(ab)
        print(ab)
        print(num)
        print("n={}".format(n))
        for i in range(0,n):
            
            for j in range(i+1,n):
                print("i={}".format(i))
                print("j={}".format(j))
                if(ab[i]== ab[j]):
                    a="-1"
                    break
                else{a=num}