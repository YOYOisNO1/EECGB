    #for input: list(int(i) for i in input().split())
def main():
    	n = map(int,input().split())
    	if n%2==0:
    		print "white"
    		print "1 2"
    	else:
    		print "black"
    
    if __name__ == '__main__':
        main()