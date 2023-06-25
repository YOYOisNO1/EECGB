def program952():
    import sys
    
    # sys.stdin = open('test.txt', 'r')
    
    w = 0
    b = 0
    
    while True:
        try:
            s = input()
            
            w += sum([9 for i in s if i is 'Q'])
            w += sum([5 for i in s if i is 'R'])
            w += sum([3 for i in s if i is 'B'])
            w += sum([3 for i in s if i is 'N'])
            w += sum([1 for i in s if i is 'P'])
        
            b += sum([9 for i in s if i is 'q'])
            b += sum([5 for i in s if i is 'r'])
            b += sum([3 for i in s if i is 'b'])
            b += sum([3 for i in s if i is 'n'])
            b += sum([1 for i in s if i is 'p'])
    
        except:
            break
            
            
    if w>b:
        print('White')
    elif w==b:
        print('Draw')
    elif w<b:
        print('Black')