def program159():
    nk=input()
    NK=[]
    NK=nk.split(' ')
    for i in range(len(NK)):
        NK[i]=int(NK[i])
    K=NK[1]
    
    
    ch=input()
    ch+=' '
    n=len(ch)
    
    
    H=0
    ch1=''
    i=0
    while( i<n):
        if(ch[i] != ' '):
            ch1+=ch[i]
        else:
            S=int(ch1)
            if((K%S==0) and( S>H)):
                H=S
            ch1=''
        i+=1
    
      
    print(K/H)
            
            
        