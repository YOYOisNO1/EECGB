    # -*- coding: utf-8 -*-
    """
    Created on Sat Jun  8 10:08:27 2019
    
    @author: plosi
    """
    import math
    
def issame(arr,m): 
        for i in range(len(arr)):
            if arr[i]!=m: 
                return False 
        return True 
    
def ispower(m): 
        if m%2==0: 
            m=int(m/2)
            while m%2==0: 
                m=m/2
            if m!=1: 
                return False
            else: 
                return True 
        return False
                
    
        
            
            
    
def SOE(n): 
        p=2
        global ps
        primes=[True for i in range(n+1)]
        primes[0]=False 
        primes[1]=False 
        while p<=n**(0.5):
            cur=p
            cur=cur+p 
            while cur<=n: 
               
                primes[cur]=False 
                cur=cur+p
            p=p+1
            while not primes[p]: 
                p=p+1
        ps=[i for i in range(len(primes)) if primes[i]] 
        global pset
        pset=set(ps)
    
def fact(n): 
        val=ps[0]
        bs=[]
        fs=[]
        ct=0 
        if n in pset: 
            return (n,0) 
        
        while n>1:
            if n%val==0: 
                a=1  
                n=int(n/val)
                bs.append(val)
                while n%val==0: 
                    n=n/val
                    a=a+1
                fs.append(a)
            ct=ct+1
            val=ps[ct]     
        m=max(fs) 
        p=1 
        for val in bs: 
            p=p*val 
        if m==1: 
            return (p,0)
        
        if issame(fs,m): 
            if ispower(m): 
                num=int(math.log2(m))
            else: 
                num=int(math.log2(m))+1
                num=num+1
        else: 
            if ispower(m):
                num=int(math.log2(m))
            else: 
                num=int(math.log2(m))+1
            num=num+1
        
            
        return (p,num) 
    
def main(): 
        n=int(input()) 
        if n==1: 
            print(str(1)+" "+str(0))
            return None
        SOE(n)
        p,ct=fact(n) 
        print(str(p)+" "+str(ct))
    main()
                
                    
            
            