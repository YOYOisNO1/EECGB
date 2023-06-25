    alphabet = "abcdefghijklmnopqrstuvwxyz"
    pos = {alphabet[i]:i for i in range(26)}
    
def compute(s,n):
    	if len(s)<=1:
    		return 0
    	char = alphabet[n]
    	word = []
    	ans=0
    	for i in range(len(s)):
    		if s[i][0]==char:
    			if (i!=0 and pos[s[i-1][0]]==pos[s[i][0]]-1) or (i!=len(s)-1 and pos[s[i+1][0]]==pos[s[i][0]]-1):
    				ans+=s[i][1]
    			else:
    				ans+=compute(word,n-1)
    				word=[]
    		else:
    			if not word or word[-1][0]!=s[i][0]:
    				word.append(s[i])
    			else:
    				word[-1][1]+=s[i][1]
    	ans+=compute(word,n-1)
    	# print(s,end=":")
    	# print(ans)
    	return ans
    
def simplify(s):
    	lst = []
    	for i in range(len(s)):
    		if not lst or lst[-1][0]!=s[i]:
    			lst.append([s[i],1])
    		else:
    			lst[-1][1]+=1
    	return lst
    
    
    n= input()
    s = simplify(input())
    print(compute(s,25))
    