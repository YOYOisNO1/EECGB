def main():
    	n, t = [int(x) for x in input().split()]
    	s = list(input())
    	while(t):
    		t -= 1
    		i = 0
    		while(i < n-1):
    			if s[i] == 'B' and s[i+1] == 'G':
    				temp = s[i+1]
    				s[i+1] = s[i]
    				s[i] = temp
    				i += 1
    			i += 1
    	print("".join(s))	
    
    if __name__ == "__main__":
    	main()