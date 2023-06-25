def program4676():
    n,k = [int(_) for _ in input().strip().split()]
    string = input().strip()
    dau = [1000010]*26
    cuoi = [-1]*26
    result = [0]*(n+20)
    
    A = ord('A')
    for i in range(n):
      position = ord(string[i])-A
      dau[position] = min(dau[position],i)
      cuoi[position] = i
    for i in range(26):
      if cuoi[i] != -1:
        result[dau[i]] += 1
        result[cuoi[i]+1] -= 1
    for i in range(1,n):
      result[i] = result[i-1]+result[i]
    value = max(result)
    if value > k:
      print("YES")
    else:
      print("NO") 