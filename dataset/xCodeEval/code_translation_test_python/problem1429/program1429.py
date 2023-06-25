    a,b=map(int,input().split())
def ggcd(a,b):
    	if b==0:
    		return [1,0,a]
    	else:
    		x,y,d=ggcd(b,a%b)
    		x,y=y,x-a/b*y
    		return [x,y,d]
    y,x,d=ggcd(a,b)
    if d!=1:
    	print("Impossible")
    	exit()
    ans=""
def gao(a,b,c,d):
    	if a==1 and b==0 and c==0 and d==1: return
    	global ans
    	if a>c:
    		t=b/d
    		ans="%dB"%(t)+ans
    		a-=c*t
    		b-=d*t
    		gao(a,b,c,d)
    	else:
    		t=c/a
    		ans="%dA"%(t)+ans
    		c-=a*t
    		d-=b*t
    		gao(a,b,c,d)
    x+=a
    t=(x-1)/a
    x-=t*a
    y+=t*b
    assert 0<x and x<=a and 0<y and y<=b
    gao(x,b-y,a-x,y)
    print(ans)