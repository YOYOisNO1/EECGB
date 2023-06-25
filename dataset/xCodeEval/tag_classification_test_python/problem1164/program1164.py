def program1164():
    k= int(input())
    
    c='a'
    
    while ( k != 0):
    
       j = 1
    
       while ((j+1)*(j+2) < 2*k):
    
          j = j+1
    
       
    
       for i in range (0,j+1):
    
          print(c,end="")
    
       c=chr(ord(c)+1)
    
       k=k-((j+1)*(j))/2
    
    print("z")
    
    
    
    
    
    # Made By Mostafa_Khaled