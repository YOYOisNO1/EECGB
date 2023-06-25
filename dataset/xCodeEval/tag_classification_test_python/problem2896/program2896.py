def WeatherTomorrow(n,seq):
    	i=1
    	firstDiff = seq[1] - seq[0]
    	while i<n-1:
    		diff = seq[i+1] - seq[i]
    		if diff!=firstDiff:
    			return seq[n-1]
    		i+=1
    
    	return seq[n-1]+firstDiff
    
    n = int(input())
    seq = [int(x) for x in input().split()]
    
    print(WeatherTomorrow(n,seq))