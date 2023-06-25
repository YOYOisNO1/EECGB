def program3253():
    n=int(input())
    s=input()
    array = list(string)
    left = 0
    right = 0
    up = 0
    down = 0
    
    for i in array:
        if i == "U":
          up += 1
        elif i == "D":
          down += 1
        elif i == "L":
          left += 1
        else:
          right += 1
    
    return 2*min(left, right) + 2*min(up, down)