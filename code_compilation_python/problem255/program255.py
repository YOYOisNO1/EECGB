def program255():
    num,time=map(int,input().split())
    string=input()
    list_a=list(string)
    x=0
    while (x!=time):
        for i in range(2,num):
            if 'G' in list_a[i] and 'B' in list_a[i-1] :
                list_a[i]='B'
                list_a[i-1]='G'
                i+=2
                    
                
            x+=1
    string=str(list_a)    
    
    print(string)