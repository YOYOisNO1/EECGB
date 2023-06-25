def program1218():
    s = str(input())
    
    s = s.replace("at","@",1)
    s = s.replace("dot",".")
    
    if s[0]==".":
    	s = "dot"+s[1:]
    
    if s[0]=="@":
    	s = s.replace("at","@",1)
    	s = "at"+s[1:]
    	
    
    if s[len(s)-1]==".":
    	s = s[:len(s)-1]+"dot"
    
    print(s)