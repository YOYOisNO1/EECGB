    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    
def solve(a, p, t):
    	n = a[0]
    	c = a[1]
    	points_limak = 0
    	points_radek = 0
    	time = 0
    	for i in range(0, len(p)):
    		time += t[i]
    		points_limak += max(0, p[i]-c*time)
    	time = 0
    	for j in reversed(range(0, len(p))):
    		time += t[j]
    		points_radek += max(0, p[j]-c*time)
    	if points_radek > points_limak:
    		print("Radewoosh")
    	elif points_limak > points_radek:
    		print("Limak")
    	else:
    		print("Tie")
    
    solve(a, p, t)
    