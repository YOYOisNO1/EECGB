    # coding=utf-8
    
    import sys
    
def main():
    	n, c = map(int, sys.stdin.readline().split())
    	ps = sys.stdin.readline().split()
    	ts = sys.stdin.readline().split()
    
    	accts = []
    	acct = 0
    	for t in ts:
    		acct += t
    		accts.append(acct)
    
    	acctsrev = []
    	acct = 0
    	for i in xrange(len(ts), 0, -1):
    		acct += ts[i]
    		acctsrev.insert(0, acct)
    
    	limak = 0
    	for i in xrange(0, n):
    		limak += max(0, ps[i]-c*accts[i])
    
    	rade = 0
    	for i in xrange(n, 0, -1):
    		rade += max(0, ps[i]-c*acctsrev[i])
    
    
    	if limak > rade:
    		print 'limak'
    	elif limak < rade:
    		print 'rade'
    	else:
    		print 'tie'
    
    if __name__ == '__main__':
    	main()