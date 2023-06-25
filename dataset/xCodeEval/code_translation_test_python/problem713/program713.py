def program713():
    n = int(input())
    if n == 0:
    	print('O-|-OOOO')
    while n:
    	n,i = n/10,n%10
    	print('O')*(1-i/5)+'-'+'O'*(i/5)+'|'+'O'*(i%5)+'-'+'O'*(4-i%5)