    l = []
    
def start():
    	# global l
    	l.append(0)
    	for i in range(1, 100001):
    		x = str(i)
    		y = x+x[::-1]
    		l.append(int(y))
    	for i in range(1, 100001):
    		l[i] += l[i-1]
    
    if __name__ == '__main__':
    	# global l
    	start()
    	m = input().split()
    	k = m[0]
    	k = int(k)
    	p = m[1]
    	p = int(p)
    	print(l[k] % p)