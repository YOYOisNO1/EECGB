    #! /usr/bin/env python
    
    from sys import stdin
    
def solve(bits):
    	bits.sort()
    	for i,bit in enumerate(bits):
    		x=bit
    		y=x+x
    		if bit==1:
    			y=1
    		for other in bits[i+1:]:
    			if other>bit and y>other:
    				return "YES"
    	return "NO"
    
    if __name__=='__main__':
    	n=int(stdin.readline())
    	bits=map(int,stdin.readline().split())
    	print solve(bits)