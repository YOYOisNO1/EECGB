def read(is_int,split_by):
    	if(is_int):
    		return [int(x) for x in input().split(split_by)]
    	else:
    		return [x for x in input().split(split_by)]
    
    s,f = read(False," ")
    n = int(input())
    seq = ['<','^','>','v']
    k = n%4
    spin = "undefined"
    ind_s = seq.index(s)
    # Case of k == 0 undefined
    if not(k%2==0) or not(s == f):
    	if f == seq[ind_s-k]:
    		spin = "ccw"
    	elif f == seq[ind_s+k]:
    		spin = "cw"
    print(spin)
    