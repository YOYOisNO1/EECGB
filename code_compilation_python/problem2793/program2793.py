def program2793():
    x = "abcdefghijklmnopqrstuvwxyz" 
    y = str(input())
    
    yLista =list(y)
    
    #x= '-'.join(x)
    if(len(x)!=len(y)):
      print(-1)
    k=1
    else:
        for i in range(len(y)):
            if (x[i]==yLista[i]):
                pass
              elif (x[i-1]==yLista[i]):
                yLista[i]=x[i]
            else:
                k=0
                print(-1)   
                break
    
    y = ''.join (yLista)
    if(k==1):
        print(y)