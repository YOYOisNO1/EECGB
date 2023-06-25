    x = map(int,input().split())
    a = x[0]
    b = x[1]
    
def zeros(n):
    	if n == 1:
    		return 0
        l = len(bin(n)) - 3
        x = l * (l-1) / 2
        if len(bin(n)[2:].replace("1","")) == 1:
            x += bin(n)[2:].find("0")
        else:
            x += (bin(n)[2:].find("0") - 1)
        return x
    print zeros(b) - zeros(a-1)