def program773():
    s = input()
    pos = 0
    t = input()
    for i in range(len(t)):
    	if t[i] == s[pos]:
    		pos += 1
    print(pos+1)
     