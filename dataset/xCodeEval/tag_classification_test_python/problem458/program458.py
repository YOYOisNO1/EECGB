    a, b = map(int, input().split(' '))
def cal(a, b):
        a %= 2 * b
        return a, b
        
    
    while (a > 0 and b > 0 and (a >= 2 * b or b >= 2 * a)):
        if (a > b):
    	a, b = cal(a, b)
        else:
    	b, a = cal(b, a)
    
    print(a,) b