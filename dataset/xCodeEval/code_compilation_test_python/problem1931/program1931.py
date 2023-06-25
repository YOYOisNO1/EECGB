def program1931():
    k=int(input())
    arr=[]
    for i in range(1,k+1):
        arr[i]=int(input())
        
     s=""  
     for digit in arr:
         s=s+str(digit)
         
     print(s[k])    
        