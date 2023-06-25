def program4663():
    #使用deepcopy使lista不被改变
    #双引号要打一对 不然要出事
    #初始化别加int
    import copy
    lista=[]
    listb=[]
    temp=[]
    a=int(input())
    flag=0
    mark=0
    
    for i in range(0,a):
        str=input()
        for j in range(0,a):
            temp.append(str[j])
        lista.append(temp)
        temp=[]
        
    for i in range(0,a):
        str=input()
        for j in range(0,a):
            temp.append(str[j])
        listb.append(temp)
        temp=[]
    
    listacpy =copy.deepcopy(lista)
    #转90°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[a-1-j][i]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
    
    mark = 0
    
    #转180°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[a-1-i][a-1-j]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
        
    mark = 0
    
    #转270°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[j][a-1-i]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
    
    #翻面
    listtemp=copy.deepcopy(lista)
    for i in range(0,a):
        for j in range(0,a):
            lista[i][j]=listtemp[i][a-1-j]
    
    mark = 0
    
    listacpy =copy.deepcopy(lista)
    #转90°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[a-1-j][i]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
    
    mark = 0
    
    #转180°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[a-1-i][a-1-j]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
        
    mark = 0
    
    #转270°
    for i in range(0,a):
        for j in range(0,a):
            listacpy[j][a-1-i]=lista[i][j]
    
    for i in range(0,a):
        for j in range(0,a):
            if(listacpy[i][j]!=listb[i][j]):
                mark=1
                break
        if(mark==1):
            break
    if(mark==0):
        flag=1
    
     
    if(flag==1):
        print("yes")
    else:
        print("no")
        