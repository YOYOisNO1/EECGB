def program506():
    # Made By Mostafa_Khaled 
     bot = True 
    n=int(input())
    
    r=['','O-|-OOOO'][n<1]
    
    while n:t=n%10;r+=['O-','-O'][t//5]+'|';t=t%5;r+='O'*t+'-'+'O'*(4-t)+'\n';n//=10
    
    print(r)
    
    # Made By Mostafa_Khaled