    
def main():
        curr = map(int, input().split())
        goal = map(int, input().split())
    
    
        rest = [0, 0, 0]
        need, can_make = 0, 0
        
        for i in range(3):
            diff = goal[i] - curr[i]
    
            if(diff > 0):
                need += diff
    
            elif(diff < 0):
                rest[i] = -1 * diff
    
        for i in range(3):
            can_make += rest[i] / 2
    
    
        if(can_make >= need):
            print("Yes")
    
        else:
            print("No")
    
    ##########################################
    ##########################################
    ##########################################
    if(__name__ == "__main__"):
        main()