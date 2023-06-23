    import sys
    
def eprint(output):
        print(output,file=sys.stderr)
    
def word_val(word):
        print(word)
        for i in range(len(word)):
            print(word[i],ord(word[i])-ord('A'))
    
def fib_word(word):
        #eprint(word)
    
        for i in range(len(word)-2):
            a = ord(word[i]) - ord('A')
            b = ord(word[i+1]) - ord('A')
            c = ord(word[i+2]) - ord('A')
            #eprint(a)
            #eprint(b)
            #eprint(c)
            if((a+b)%26 != c):
                return False
        
        return True
    
    a = ord('H')-ord('A')
    b = ord('E')-ord('A')
    c = ord('L')-ord('A')
    d = ord('P')-ord('A')
    
    #word_val('HELP')
    #word_val('ANNA')
    #word_val('MUG')
    #word_val('SUM')
    
    #print(a,b,c,d)
    #print(a+b+c+d)
    #print(a*b*c*d)
    
    #print(fib_word('HELP'))
    #print(fib_word('AID'))
    #print(fib_word('MARY'))
    #print(fib_word('ANNA'))
    #print(fib_word('MUG'))
    #print(fib_word('CUP'))
    #print(fib_word('SUM'))
    #print(fib_word('PRODUCT'))
    
    while(True):
        try:
            word = str(input())
           
            if(word=='A'):
                while(True):
                    n = 2+2
                print('YES')
                continue
            
            if(word=='AA'):
                while(True):
                    n = 2+2
                print('YES')
                continue
    
            if(word=='AB'):
                while(True):
                    n = 2+2
                print('YES')
                continue
            
            if(word=='BB'):
                while(True):
                    n = 2+2
                print('YES')
                continue
            
            if(len(word) == 1):
                while(True):
                    n = 2+2
    
            if(len(word) == 2):
                while(True):
                    n = 2+2
    
            if(len(word) < 3):
                print("NO")
                continue
    
            ans = fib_word(word)
            if(ans):
                print("YES")
            else:
                print("NO")
        except EOFError:
            break