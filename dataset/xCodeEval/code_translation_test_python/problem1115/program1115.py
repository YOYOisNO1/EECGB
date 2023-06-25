def program1115():
    import sys
    import math
    
    values = sys.stdin.readline().split()
    num1, num2 = int(values[0]), int(values[1])
    distance = math.sqrt((num1 ** 2) + (num2 ** 2))
    
    if num1 == 0 or num2 == 0:
        print("black")
        sys.exit(0)
    
    cur_distance = 0
    state = 1 if num1 * num2 >= 0 else -1
    
    for i in range(0, 2000):
        cur_distance = i
        state *= -1
        
        if distance == cur_distance:
            print("black")
            break
        elif distance < cur_distance:
            if state == -1:
                print("white")
            else:
                print("black")
            break
    