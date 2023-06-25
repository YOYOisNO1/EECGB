def program1262():
    a = input()
    n = 0
    b = "CODEFORCES"
    for x in a:
    if x == b[n]:
    	n+=1
    if n == len(b):
    	print ("YES")
    else:
    	print ("NO")