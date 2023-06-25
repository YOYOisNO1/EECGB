    import sys
    
def solver(text,t):
        text=list(text)
        for i in range(t):
            change(text)
            # print(''.join(text))
        return ''.join(text)
    
def change(text):
        i=0;l=len(text)
        while i < l-1:
            if text[i]=='B' and text[i+1]=='G':
                text[i],text[i+1]='G','B'
                i+=2
            else:
                i+=1
            
def get_ints():
        return map(int,sys.stdin.readline().split())
        
    if __name__=='__main__':
        a,b=get_ints()
        tmp=str(sys.stdin.readline())
        sys.stdout.write(solver(tmp,b))
        
        
        