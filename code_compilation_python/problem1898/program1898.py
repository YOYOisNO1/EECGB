def program1898():
    n = int(input())
    sum = 0;
    i = 1;
    a = []
    while(sum <= n):
    	if(sum + i <= n):
    		sum += i;
    	else:
    		break;
    	a.append(i);
    	i+=1;
    
    rem = n - sum
    a[0] += rem;
    print len(a)
    print ' '.join([str(i) for i in a]);