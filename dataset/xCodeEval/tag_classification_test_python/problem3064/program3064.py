    '''
    int main(/*int argc, char *argv[]*/) {
    	//ios::sync_with_stdio(false);
    	long long n,a,b,p,q;
    	scanf("%lld%lld%lld%lld%lld",&n,&a,&b,&p,&q);
    	long long t1,t2,t3,res;
    
    	if(p > q)
    	{
    		res = p * t1 + q * (t2 - t3);
    	}
    	else
    	{
    		res = q * t2 + p * (t1 - t3);
    	}
    	cout<<res<<endl;
    	return 0;
    }
    
    '''
def gcd(a,b):
    	if b == 0:
    		return a
    	else:
    		return gcd(b, a % b)
    		
def lcm(a,b):
    	return a * b // gcd(a, b);
    
    text = input()
    pp = text.split(' ')
    
    n = eval(pp[0])
    a = eval(pp[1])
    b = eval(pp[2])
    p = eval(pp[3])
    q = eval(pp[4])
    
    
    t1 = n // a
    t2 = n // b
    t3 = n // lcm(a,b)
    
    if p > q:
    	res = p * t1 + q * (t2 - t3)
    else:
    	res = q * t2 + p * (t1 - t3)
    print(res)