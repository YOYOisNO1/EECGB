def __main__():
        __inp = input().split(' ')
    
        b1 = int(__inp[0]) <= int(__inp[2]) + int(__inp[3]);
        at = int(__inp[2]) - int(__inp[4])*(int(__inp[1]) - 1)
        bt = int(__inp[3]) - int(__inp[5])*(int(__inp[1]) - 1)
    
        if b1 and (at + bt <= int(__inp[0])):
            print("YES");
        else:
            print("NO");
            
    
    __main__()