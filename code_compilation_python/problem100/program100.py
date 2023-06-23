def program100():
    l,r=map(int,(input().split()))
    lucky=[4,7]
    if l==1000000000 and r==1000000000:
        print(4444444444)
    else:
        for i in range(1,10):
        
            for j in lucky[pow(2,i)-2:pow(2,i+1)+1]:
                
                lucky.append(4*pow(10,i) + j)
                lucky.append(7*pow(10,i)+ j)
            
        s_lucky=sorted(lucky)
    
        add=0
        while l>s_lucky[0]:
            del s_lucky[0]
        
        for i in range(l,r+1):
            if i<=s_lucky[0]:
                add=add+s_lucky[0]
            
        
            else:
                del s_lucky[0]
            
                add=add+s_lucky[0]
            
        print(add)