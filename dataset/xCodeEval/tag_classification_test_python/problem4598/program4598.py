def program4598():
    n, k = input().split()
    
    n = int(n)
    k = int(k)
    
    s = input()
    
    A = [-1]*28
    B = [-1]*28
    
    for num, c in enumerate(s):
      A[ord(c)-65] = num+1
    
    s = s[::-1]
    for num, c in enumerate(s):
      B[ord(c)-65] = len(s)-num-1
    
    maxi = 0 
    cur = 0
    
    for i in range(0, len(s)):
      for j in range(0, 28):
        if i == A[j]:
          cur = cur-1
      
      for j in range(0, 28):
        if i == B[j]:
          cur = cur+1
          maxi = max(maxi, cur)
    
    if maxi > k:
      print("YES")
    else:
      print("NO")