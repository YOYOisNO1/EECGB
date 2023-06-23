def program1073():
    for j in range(int(input())):
        a = int(input())
        
        
        if a%2==  0:
            print(a//2, a//2) 
        else:
              i=3
              while(i<=(a//2)+1) :
                    
               
                   if a%i==0:
                        print(a//i,a-(a//i))
                        
                        break
                   i+=2
             else:
                print(1, a-1) 
            