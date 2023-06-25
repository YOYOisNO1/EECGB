def program183():
    n, k, p = map(int, input().split())
    s = '(' + str(k) + ')'
    ans = ''
    
    for i in range (k-p,k+p+1):
        if i == k:
            ans += s+ ' '
        if i <= n and i != k and i > 0:
            ans += str(i) + ' '
    A = ans.split()
    
    if A[-1] == s:
        print('<< ' + ' '.join(A))
    elif (A[0] == '(1)' or int(A[0]) == 1) and int(A[-1]) < n:
        print(' '.join(A) +' >>')
    elif int(A[-1]) == n and (int(A[0]) == 1 or A[0] == '(1)'):
        print(' '.join(A))
    elif int(A[-1]) < n  and int(A[0]) > 1:
       print('<< '+ ' '.join(A) + ' >>')
    elif int(A[-1]) == n and int(A[0]) > 1:
        print('<< ' + ' '.join(A))