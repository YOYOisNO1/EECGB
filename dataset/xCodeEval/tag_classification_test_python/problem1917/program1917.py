    # modules
    from __future__ import print_function
    from sys import stdin, stdout
    read = lambda : stdin.readline()[:-1]
    write = lambda s :stdout.write(str(s) + "\n")
    # end modules
    
    #start programm
    
def __main__():
    	#code
    	n=int(read())
    	s=read()
    	t=n//11
    	if s.count("8") < t:
    		t=s.count("8")
    	write(t)
    if __name__ == '__main__':
        __main__()