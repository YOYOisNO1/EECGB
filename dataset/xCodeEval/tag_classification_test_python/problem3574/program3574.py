def program3574():
    num,time=map(int,input().split())
    string=input()
    list_a=list(string)
    while (time>0):
        i=0
        while i<(len(list_a)-1):
            #to check if 'G' is standing behind 'B',If yes thn swap their positions
            if (list_a[i]=='B' and list_a[i+1]=='G'):
                list_a[i],list_a[i+1]=list_a[i+1],list_a[i]
                #as i and i+1 as swapped so it vl be 'B' therefore there is a need to increment
                i+=1
            i+=1
        time-=1
        
    string="".join([str(elem) for elem in list_a])    
    print(string)