    # -*- coding: utf-8 -*-
    """
    Created on Sat Jun  8 09:48:23 2019
    
    @author: plosi
    """
    
def main():
        n=int(input()) 
        arr=input().split(" ") 
        for j in range(n): 
            arr[j]=int(arr[j]) 
        prev=arr[0] 
        ct=0
        m=0
        if n==1: 
            print(0)
            return None
        if arr[0]==1 and arr[1]==2: 
            ct=1 
            m=1
        for j in range(1,n-1): 
            if arr[j]==(prev+1) and arr[j]==arr[j+1]-1: 
                ct=ct+1
                m=max(ct,m) 
            else: 
                ct=0 
            prev=arr[j]
        if arr[n-1]==arr[n-2]+1 and arr[n-1]==1000: 
            ct=ct+1 
            m=max(m,ct) 
        print(m)
    main()