def program4369():
    start = 'a'
    
    strInput = input("")
    
    rotate = 0
    
    for c in strInput:
        left = ord(c) - ord(start)
        right = ord(start) - ord(c)
    
        if left < 0:
            left+=26
        if right < 0:
            right+=26
        
        rotate+=min(left,right)
    
        start = c
    
    print(str(rotate))