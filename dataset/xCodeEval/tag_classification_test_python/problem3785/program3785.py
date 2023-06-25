def main():
    	n, ticket=int(input()), input()
    	first, second=sorted(ticket[:n]), sorted(ticket[n:])
    	less=True if first[0]<second[0] else False
    	for a, b in zip(first, second):
    		if (less and a>=b) or (not less and a<=b):
    			print('NO')
    			exit()
    	print('YES')
    	
    if __name__=='__main__':
    	main()