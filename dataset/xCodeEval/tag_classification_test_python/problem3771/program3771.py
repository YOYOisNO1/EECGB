def program3771():
    import sys
    
    l1, s1, r1, p1 = map(int,input().strip().split())
    l2, s2, r2, p2 = map(int,input().strip().split())
    l3, s3, r3, p3 = map(int,input().strip().split())
    l4, s4, r4, p4 = map(int,input().strip().split())
    
    if p1:
    	if l2 or r4 or s3 or l1 or s1 or r1:
    		print("YES")
    		sys.exit()
    
    if p2:
    	if r1 or l3 or s4 or l2 or s2 or r2:
    		print("YES")
    		sys.exit()
    
    if p3:
    	if s1 or r2 or l4 or l3 or s3 or r3:
    		print("YES")
    		sys.exit()
    
    if p4:
    	if l1 or s2 or r3 or l4 or s4 or r4:
    		print("YES")
    		sys.exit()
    
    print("NO")