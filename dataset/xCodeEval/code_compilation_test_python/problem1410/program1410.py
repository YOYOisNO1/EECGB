    ln = [75]
    for i in range(10**5 + 1):
    	ln.append(max(10**18 + 10, 68 + 2 * ln[-1]))
    
    f0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
    f1_1 = 'What are you doing while sending "'
    f1_2 = '"? Are you busy? Will you send "'
    f1_3 = '"?'
    
def getAns(n, k):
    	while True:
    		if k >= ln[n]:
    			print(n, k)
    			return '.'
    		elif n == 0:
    			return f0[k]
    		elif k < 34:
    			return f1_1[k]
    		elif k < 34 + ln[n - 1]:
    			k -= 34
    			n -= 1
    		elif k < 34 + ln[n - 1] + 32:
    			return f1_2[k - 34 - ln[n - 1]]
    		elif k < 34 + ln[n - 1] + 32 + ln[n - 1]:
    			k -= 34 + ln[n - 1] + 32
    			n -= 1
    		else:
    			return f1_3[k - k - 34 - ln[n - 1] - 32 - ln[n - 1]]		
    
    q = int(input())
    for qq in range(q):
    	n, k = list(map(int, input().split()))
    	print(getAns(n, k - 1), end='')