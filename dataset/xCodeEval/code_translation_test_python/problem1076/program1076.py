def program1076():
    a=int(input())
    if a>0 or a<=-9:
        for i in range(a,10000000000000000000000):
            k=i+1
            k=str(k)
            if '8' in k:
                k=int(k)
                print(k-a)
                break
            else:
                continue
    elif -9<a<=0:
        print(8-a)
    
    
    