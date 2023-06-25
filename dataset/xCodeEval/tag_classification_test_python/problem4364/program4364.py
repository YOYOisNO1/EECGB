    x,y,l,r=list(map(int,input().split()))
    indexx=0
    indexy=0
def mult(k,x):
        if x==0:return 1
        if x%2==1:return mult(k,x/2)*mult(k,x/2)*k
        if x%2==0:return mult(k,x/2)*mult(k,x/2)
    
    multi=1
    while True:
        multi*=x
        if multi>r:break
        indexx+=1
    
    multi=1
    while True:
        multi*=y
        if multi>r:break
        indexy+=1
    
    un=[]
    for i in range(indexx,-1,-1):
        for j in range(indexy+1):
            if (mult(x,i)+mult(y,j)<=r) and (mult(x,i)+mult(y,j))>=l:
                un.append(mult(x,i)+mult(y,j))
            if (mult(x,i)+mult(y,j))>r:
                break
    
    if len(un)==0:print(r-l+1)
    else:
        un.sort()
        max1=0
    
        for i in range(len(un)-1):
           max1=max(un[i+1]-un[i]-1,max1)
        max1=max(un[0]-l,r-un[len(un)-1],max1)
        print(max1)
    