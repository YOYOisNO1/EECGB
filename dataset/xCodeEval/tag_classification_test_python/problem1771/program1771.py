    
    
def sub(str1,str2,m,n): 
        j = 0   
        i = 0    
        while j<m and i<n: 
            if str1[j] == str2[i]:     
                j = j+1    
            i = i + 1          
        return j==m 
    s1 = input()
    s2 = input()
    
    c = 0
    for i in range(len(s1)):
        for j in range(i,len(s1)):
            s3 = s1[:i] + s1[j+1:]
            if sub(s2,s3,len(s2),len(s3)) == True:
                c = max(c,min(j+1,len(s1))-i)
    print(c)