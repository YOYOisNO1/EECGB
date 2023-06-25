def program2615():
    n=int(input())
    
    input=input()
    
    hard=False
    
    for letter in input:
        
        if letter =='1':
            hard=True
            break
            
    if hard:
        print("HARD")
    else:
        print("EASY")