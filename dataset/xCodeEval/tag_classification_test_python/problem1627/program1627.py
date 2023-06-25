    from itertools import chain, combinations
def powerset(iterable):
      xs = list(iterable)
      return chain.from_iterable( combinations(xs,n) for n in range(len(xs)+1) )
    s = input()
    l = len(s)
    hope = range(1,l+1)
    hope = powerset(hope)
    maxst = ""
    for x in hope:
    	st = ""
    	for p in x:
    		st+=s[p-1]
    	if(st==st[::-1] and st>maxst):
    		maxst=st
    print(maxst)