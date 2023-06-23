def program184():
    i = map(int, input().split())
    n = i[0]
    p = i[1]
    k = i[2]
    j = k
    stri = ''
    
    if p - 2 > 1:
       stri += "<< "
    
    while j > 0:
      if p - j > 0:
        stri = stri + str(p - j) + ' '
      j = j - 1
    
    stri = stri + '(' + str(p) + ') '
    j = 1  
     
    while j <= (k + 1) & (p + j) <= n:
      print(str(j) + str(k) + str(p) + str(n))
      if (p + j) <= n:
        stri = stri + str(p + j) + ' '
      j = j + 1
    
    if (p + j) < n + 1:
       stri = stri + '>>'
      
    print(stri)
    input()