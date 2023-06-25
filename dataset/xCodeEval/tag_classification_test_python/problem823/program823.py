def program823():
    __author__ = 'Think'
    word=[(ord(i)-64) for i in input().split()[0]]
    letters=[0]*26
    substring=-1
    for i in range(len(word)):
    	position=i%26
    	letters[position]=-1
    	current=word[i]
    	if current==-1:
    		letters[position]=current
    	elif current in letters:
    		letters[letters.index(current)]=0
    		letters[position]=current
    	if 0 in letters:
    		letters[position]=current
    	else:
    		substring=i-25
    		letters[position]=current
    		break
    if 0 not in letters and substring==-1:
    	substring=len(word)-26
    if substring==-1:
    	print(-1)
    else:
    	substring_letters=[0]*26
    	for i in range(substring, substring+26):
    		position=i%26
    		if letters[position]>0:
    			substring_letters[i-substring]=letters[position]
    		elif letters[position]==0:
    			print("ERROR 0 in letters", letters, position, substring)
    	for i in range(1, 27):
    		if i not in substring_letters:
    			substring_letters[substring_letters.index(0)]=i
    	if 0 in substring_letters:
    		print("ERROR 0 in substring_letters", substring_letters)
    	for i in range(len(word)):
    		current=word[i]
    		if (i<substring) or (i>substring+25):
    			if current==-1:
    				print("A", end="")
    			else:
    				print(chr(current+64), end="")
    
    		else:
    			print(chr(substring_letters[i-substring]+64), end="")
    	print("\n")