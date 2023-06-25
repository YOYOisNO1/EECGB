def program1535():
    import sys
    
    
    s=sys.stdin.readline().strip()
    t=sys.stdin.readline().strip()
    
    wijzer=0
    
    for x in t:
        if x==s[wijzer]:
            wijzer+=1
            
    
    print(wijzer+1)
        
        