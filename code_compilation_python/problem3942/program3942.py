    
def clouded_strategy(H,W,cake):
        ans= int (cake[0][0]=='*')
        
        i,j=0,0
        prev= 'S'
        while (i,j)!= (H-1,W-1):
            if i==H-1 or j==W-1:
                if i==H-1:
                    j+=1
                if j==W-1:
                    i+=1
                ans += int (cake[i][j]=='*')
            else:  
                if cake[i][j+1]!='*' and cake[i+1][j]!='*':
                    if prev=='E':
                        i,j = i+1, j
                        prev=='S'
                    if prev=='S':
                        i,j = i, j+1
                        prev=='E'
                
                elif cake[i][j+1]=='*':
                    i,j = i,j+1
                    prev=='E'
                    ans+=1
    
                else:
                    i,j = i+1,j
                    prev=='S'
                    ans+=1
    
    
        print (ans)
    
    
    
    H,W = map (int, input().split(' '))
    cake = [[] for i in range (H)]
    for i in range (H):
        cake[i] = list (input ())
    
    clouded_strategy(H,W,cake)
    