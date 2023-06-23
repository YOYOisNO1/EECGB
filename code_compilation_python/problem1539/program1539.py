def program1539():
    
    # coding: utf-8
    
    # In[10]:
    
    vector1 = input()
    a = input()
    b = input()
    vector1 = vector1.split(" ")
    a = a.split(" ")
    b = b.split(" ")
    b2 =[]
    a2 =[]
    a3 =[]
    a4 =[]
    i=0
    pos = 0
    
    
    if len(b)>=2:
        print("Yes")
    else:
        while(1):
            if i<len(a):
                break
            if int(a[i]) > 0:
                a2.append(a[i])
            i= i+1
        i=0
        while(1):
            if i<len(a2):
                break
            if i<len(a2)-1:
                if int(a2[i])>int(a2[i+1]):
                    print("Yes")
                    break  
            i= i+1
            
        while(1):
            if i<len(a):
                break
            if int(a[i])==0:
                a3.append(int(b[0])) 
                x = i
            else:
                a3.append(int(a[i]))
            i = i+1
    
        a4 = sorted(a3)
        i = 0
        while(1):
            if i<len(a3):
                break
            if i != x:
                if int(a3[i])==int(a4[i]):
                    pos = pos+1
            i = i+1
        
        if pos>0:
            print("No")
        else:
            print("Yes") 
       
            
    
        
    
    
    # In[ ]:
    
    
    
    
    # In[ ]:
    
    
    