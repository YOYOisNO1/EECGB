def main():	
    	from sys import stdin,stdout
    
    	n,k = map(int,stdin.readline().split())
    
    	from collections import Counter
    
    
    
    	fg = stdin.readline()
    	people = Counter(fg)
    
    	l = len(fg)
    
    	occupied = []
    
    	available = []
    
    	for gf in xrange(k):
    		available.append(gf+1)
    	app = available.append
    	aapp = occupied.append
    
    	seen = {}
    	joke = True
    	for h in fg:
    		if h not in seen:
    			seen[h]=0
    
    	for index in xrange(l):
    		
    		if seen[fg[index]]==0:
    			if len(available)==0:
    				joke = False
    				break
    			# occupied.append(available[0])
    			aapp(available[0])
    			del available[0]
    			seen[fg[index]]+=1
    		else:
    			seen[fg[index]]+=1
    
    
    		if seen[fg[index]]==people[fg[index]]:
    			# available.append(occupied[0])
    			app(occupied[0])
    			del occupied[0]
    		# print(seen[fg[index]],people[fg[index]],fg[index])
    
    	if joke == True:
    		print("NO")
    	else:
    		print("YES")
    
    	# print(1000000,1)
    	# print("").join("A" for _ in xrange(1000000))
    if __name__ == "__main__":
    	main()