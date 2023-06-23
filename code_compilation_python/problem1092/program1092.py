    
    # coding: utf-8
    
    # In[1]:
    
    s=input()[::-1]
    m=50
def f(c,i=0):return s.find(c,i)+1 or 50
    i0_1=f('0')
    i5=f('5')
    i05=min(f('0',i0_1),i5)
    m1=i0_1+i05+(i05<i0_1)-3
    i27=min(f('2'),f('7'))
    m2=i5+i27+(i27<i5)-3
    if s[-1]=='5':
        i=-2
        while s[i]=='0' and (len(s)+i)>=0:m2+=1;i-=1
    m=min(m1,m2)
    print((-1,m)[m<40])
    
    
    # In[ ]:
    
    
    