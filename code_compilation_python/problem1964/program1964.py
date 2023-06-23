def program1964():
    n,k=map(int, input().split())
    sum=0
    days=[int(i) for i in input().split(' ')]
    arya=0
    bran=0
    for i in range(0,n):
        arya+=day[i]
        if(arya<=8)
            bran+=arya
            arya=0
        else
            bran+=8
            arya-=8
        if bran>=k:
            print(i+1)
            break
    
    if bran<k:
        print("-1")
            
        