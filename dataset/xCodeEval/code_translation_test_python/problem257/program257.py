    value = int(input())
def rec(i,x):
        if sum(l) >= value:
            return x
        if value == 1:
        	return 1
        i = i + x
        l.append(i)
        rec(i,x+1)
    l = []
    rec(1,2)
    print(1 if value == 1 else len(l))