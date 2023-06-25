def program938():
    x = input()
    
    for i in range(x):
        arr[i] = input()
        
    for i in range(x):
        if arr[i] == 1:
            print("HARD")
            return
        
    print("EASY")
    return