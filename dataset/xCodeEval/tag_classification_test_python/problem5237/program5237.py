def program5237():
    n, m = [int(i) for i in input().split()]
    freq_n = {i: 0 for i in range(5)}
    freq_m = {i: 0 for i in range(5)}
    
    for i in range(5):
        freq_n[i] = n // 5
        freq_m[i] = m // 5
    
    for i in range(1, (n % 5) + 1):
        freq_n[i] += 1
        
    for i in range(1, (m % 5) + 1):
        freq_m[i] += 1
    
    res = 0
    
    res += freq_n[0] * freq_m[0]
    res += freq_n[1] * freq_m[4]
    res += freq_n[2] * freq_m[3]
    res += freq_n[3] * freq_m[2]
    res += freq_n[4] * freq_m[1]
    
    print(res)