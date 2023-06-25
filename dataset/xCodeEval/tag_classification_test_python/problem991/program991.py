def ans(a1, a2, n):
        a_r = a1[0]
        a_s = a1[1]
        a_p = a1[2]
        b_r = a2[0]
        b_s = a2[1]
        b_p = a2[2]
    
        #first maximum
        maxm = min(a_r, b_s)+ min(a_s, b_p) + min(a_p, b_r)
    
        #now, minimun
        minm = n - (min(b_r, a_s+a_r)+ min(b_s, a_p+a_s) + min(b_p, a_r+a_p))
    
        s = str(minm)+' '+str(maxm)
        return(s)
    
    
    n = int(input())
    arr1 = input().split()
    a1 = []
    
    arr2 = input().split()
    a2 = []
    
    
    for i in arr1:
        a1.append(int(i))
    
    for i in arr2:
        a2.append(int(i))
    
    print(ans(a1, a2, n))