def get_key(val , freq): 
        for key, value in freq.items(): 
             if val == value: 
                 return key 
    
    n = int(input())
    s = input()
    freq = {}
    y = []
    for i in range(n-1):
        x = s[i:i+2]
        if x in freq:
            freq[x]+=1
        else:
            freq[x] = 1
        
    val = freq.values()
    m = max(val)
    print(get_key(m,freq))