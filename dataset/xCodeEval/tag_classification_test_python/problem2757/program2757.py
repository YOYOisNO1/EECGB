    from math import factorial as fact
    n,m,t=[int(x) for x in input().split()]
    ans=0
def fc(n):
    	return int(fact(n))
    for i in range(1,t-3):
    	if i>m or (t-i)<4:
    		break
    	if (t-i)>n:
    		continue
    	ans+=int(fc(m)/(fc(m-i)*fc(i)))*int(fc(n)/(fc(t-i)*fc(n-t+i)))
    	# print(ans)
    print(int(ans))