def program3618():
    n, t = map(int, input().split())
    S = list(input())
    
    for i in xrange(t):
      j = 0
      while(j < n - 1):
        if (S[j] == "B") and (S[j + 1] == "G"):
          S[j], S[j + 1] = S[j + 1], S[j]
          j += 1
        
        j += 1
      
    print("").join(S)