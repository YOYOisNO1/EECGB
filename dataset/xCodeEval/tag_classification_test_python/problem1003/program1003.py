    
def find_max_winning_rounds(p1,p2):
        result=0
        for i in range(3):
            max_winnable=min(p1[i],p2[(i+1)%3])
            result+=max_winnable
        return result
    
    '''      
def find_min_winning_rounds(p1,p2):
        for i in range(3):
            find_bigger_item_to_subtract(p2, i, p1)           
        result = 0
        for i in range(3):
            result += p1[i]
        return result
    
def find_bigger_item_to_subtract(p2, i, p1):
        if p2[(i+2)%3]>=p2[i]:
            p1[i],p2[(i+2)%3]=sub(p1[i],p2[(i+2)%3])
            if p1[i]>0:
                p1[i],p2[i]=sub(p1[i],p2[i])
        else:
            p1[i],p2[i]=sub(p1[i],p2[i])
            if p1[i]>0:
                p1[i],p2[(i+2)%3]=sub(p1[i],p2[(i+2)%3])  
                  
def sub(a,b):
        if a >= b:
            return a-b,0
        else:
            return 0,b-a
    '''
    
def calculate_max(p1,p2):
        result=0
        for i in range(3):
            re=p1[i]-p2[i]-p2[(i+2)%3]
            result+=max(0,re)
        return result
    rounds=int(input())
    
    player1_strategy=list(map(int,input().split()))
    player2_strategy=list(map(int,input().split()))
    print(calculate_max(player1_strategy,player2_strategy),find_max_winning_rounds(player1_strategy,player2_strategy))
    
    
    
    