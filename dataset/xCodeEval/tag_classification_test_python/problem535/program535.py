def program535():
    s1 = input()
    s2 = input()
    s3 = str(int(s1) + int(s2))
    
    s_1 = ""
    s_2 = ""
    s_3 = ""
    for i in range(len(s1)):
    	if s1[i] != '0':
    		s_1 += s1[i]
    for i in range(len(s2)):
    	if s2[i] != '0':
    		s_2 += s2[i]
    for i in range(len(s3)):
    	if s3[i] != '0':
    		s_3 += s3[i]
    if int(s_1) + int(s_2) == int(s_3):
    	print("YES")
    else:
    	print("NO")