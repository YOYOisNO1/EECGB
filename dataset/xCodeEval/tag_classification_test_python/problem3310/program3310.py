def program3310():
    #556_A
    
    ln = [int(i) for i in input().split(" ")]
    n = ln[0]
    m = ln[1]
    r = ln[2]
    
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    
    if (min(a) > max(b)):
        print(r)
    else:
        print((r // min(a)) * max(b) + (r % min(a)))