    from fractions import gcd
    from math import factorial, ceil, sqrt, atan2, log, pi, e, asin,acos, cos, sin, floor
    from itertools import *
    from fractions import Fraction
    import string
    import copy
    import random
    import bisect
    from decimal import *
def id_generator(size=20, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
     
def mp():
        return map(int,str(input()).split())
    
    n=input()
    case=['25','50','75','00']
    if n<100:
        if n==25 or n==50 or n==75:
            print(0)
        elif n==52 or n==57:
            print(1)
        else:
            print(-1)
    else:
        a1=10**18
        a2=10**18
        s=list(str(n))
        l=len(s)
        flag=0
        z=copy.deepcopy(s)
        for i in range(1,l+1):
            if s[l-i]=='5':
                flag=1
                break
        if flag:
            pre=i-1
            i=l-i
            #count=0
            #while i<l-1 and s[i+1]=='0':
            #	count+=1
            #	i+=1
            q=i
            count=0
            for j in range(q+1,l-1):
            	if s[j]=='0':
            		count+=1
            	else:
            		break
            #print(i,) 
            for j in range(i,l-1):
                s[j],s[j+1]=s[j+1],s[j]
            flag=0
            #print(s,pre)
            for i in range(1,l+1):
                if s[l-i]=='7' or s[l-i]=='2':
                    flag=1
                    break
            
            if flag:
    			a1=(pre+i-2+count)
            else:
                pass
        else:
            pass
        if 1:
        	#print(z)
        	s=copy.deepcopy(z)
            for i in range(1,l+1):
                if s[l-i]=='0':
                    flag=1
                    break
            if flag:
                pre=i-1
                i=l-i
                for j in range(i,l-1):
                    s[j],s[j+1]=s[j+1],s[j]
                flag=0
                #print(s,pre)
                for i in range(2,l+1):
                    if s[l-i]=='0' or s[l-i]=='5':
                        flag=1
                        break
                if flag:
                    a2=pre+i-2
                else:
                    pass
            
        #print(a1,a2)
        if min(a1,a2)==10**18:
            print(-1)
        else:
            print(min(a1,a2))
            