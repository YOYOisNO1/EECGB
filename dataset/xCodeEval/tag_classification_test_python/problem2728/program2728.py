    while True:
    	try:
		def solution(s, t):
    			tems = list(s)
    			temt = list(t)
    			tems.sort()
    			temt.sort()
    			ln1 = len(s)
    			ln2 = len(t)
    			#print(tems, temt, s, t)
    			if ln2 > ln1 or (ln1 == ln2 and tems != temt):
    				print("need tree")
    			elif ln2 == ln1:
    				print("array")
    			else:
    				i =j = cunt = 0
    				while i < ln2:
    					while j < ln1:
    						if t[i] == s[j]:
    							cunt += 1;break
    						j += 1
    					i += 1;j += 1
    				if cunt == ln2:print("automaton")
    				else:
    					i = j = cunt = 0
    					while i < ln2:
    						while j < ln1:
    							if t[i] == tems[j]:
    								cunt += 1
    								tems[j] = 7;break
    							j += 1
    						i += 1;j = 0
    					if cunt == ln2:print("both")
    					else:print("need tree")				
    		
		def read():
    			s = input()
    			t = input()
    			solution(s, t)
    			
    		if __name__ == "__main__":
    			read()
    	except EOFError:
    		break