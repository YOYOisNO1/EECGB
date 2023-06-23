def main():
    	n = int(input())
    	L = [int(x) for x in input().split()]
    	print(solver(L))
    
def solver(L):
    	S = set(L)
    	L = list(S)
    	L.sort()
    	for i in range(len(L) - 2):
    		if L[i + 1] == L[i] + 1 and \
    		L[i + 2] == L[i + 1] + 1:
    			return "YES"
    	return "NO"
    
    #L = [40, 44, 44, 44, 44, 41, 43]
    #print(list(set(L)))
    #L2 = [18, 55, 16, 17]
    #L3 = [5, 972, 3, 4, 1, 4, 970, 971]
    #print(solver(L3))
    
    main()