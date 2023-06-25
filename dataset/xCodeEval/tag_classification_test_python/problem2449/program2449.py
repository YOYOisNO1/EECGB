def program2449():
    import re
    n=int(input())
    s=input()
    within_paren=re.findall(r'\(.*?\)',s)
    for w in within_paren :
    	s=s.replace(w,"_")
    within_paren_words=[]
    for w in within_paren:
    	within_paren_words.extend(w[1:-1].split("_"))
    s_words=s.split("_")
    
    leng=0
    for w in s_words :
    	if len(w) > leng :
    		#longest=w
    		leng=len(w)
    
    cnt=0
    for w in within_paren_words :
    	#print(w)
    	if len(w) :
    		cnt+=1
    print(leng,cnt)