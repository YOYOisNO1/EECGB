    from sys import stdin
    
def main():
    	n = int(stdin.readline())
    	line = stdin.readline().strip()
    	i,j = 0,len(line)-1
    	ans = ["" for i in range(len(line))]
    	visited = [False for i in range(27)]
    	ok = True
    	for i in range(len(line)):
    		if(96< ord(line[i]) <123):
    			cont = ord(line[i])-97
    			visited[cont] = True
    			if cont > n:
    				ok = False
    	N = len(line)
    	if(N%2 != 0):
    		mid = N//2
    		i =  mid-1
    		j = mid+1
    		if(line[mid] == "?"):
    			v = 0
    			while v < n:
    				if(not visited[n-v-1]):
    					ans[mid] = chr(n-v-1+97)
    					visited[n-v-1] = True
    					break
    				v+=1
    			if(ans[mid] == ""):
    				ans[mid] = "a"
    		else:
    				ans[mid]=line[mid]
    	else:
    		mid = N//2
    		i =  mid-1
    		j = mid
    	while(j < len(line)):
    		#print(ans)
    		if(line[j] == "?" and line[i] != "?"):
    			ans[i] = line[i]
    			ans[j] = line[i]
    			visited[ord(line[i])-97] = True
    		elif(line[j] != "?" and line[i] == "?"):
    			ans[i] = line[j]
    			ans[j] = line[j]
    			visited[ord(line[j])-97] = True
    		elif(line[j] == "?" and line[i] == "?"):
    			v = 0
    			while v < n:
    				if(not visited[n-v-1]):
    					ans[i] = chr(n-v-1+97)
    					ans[j] = chr(n-v-1+97)
    					visited[n-v-1] = True
    					break
    				v+=1
    			if(ans[i] == ""):
    				ans[i] = "a"
    				ans[j] = "a"
    		elif(line[j] == line[i]):
    			ans[i]=line[j]
    			ans[j]=line[j]
    			visited[ord(line[j])-97] = True
    		else:
    			ok = False
    		j+=1
    		i-=1
    	w = 0
    	while w < n :
    		if(not visited[w]):
    			ok = False
    		w+=1
    	while w < len(visited) :
    		if(visited[w]):
    			ok = False
    		w+=1
    	#print(ans)
    	if(ok):
    		aux = ""
    		for k in range(len(ans)):
    			aux += ans[k]
    		print(aux)
    	else:
    		print("IMPOSSIBLE")
    main()