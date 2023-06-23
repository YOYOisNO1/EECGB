def program322():
    n = int(input())
    
    nums = map(int, input().split())
    
    freq = [0 for i in range(200)]
    for i in range(n):
    	freq[nums[i]] += 1
    
    print max(freq)