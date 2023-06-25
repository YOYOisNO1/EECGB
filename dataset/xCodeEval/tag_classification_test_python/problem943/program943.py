def program943():
    l=''
    k=int(input())
    index=0
    counter=1
    while True:
        for i in str(counter):
            if index<=k-1:
              l+=i
              index+=1
        counter+=1
        if index>k-1:
              break 
          
    if 1<=k <=10000:      
         print(l[k-1])