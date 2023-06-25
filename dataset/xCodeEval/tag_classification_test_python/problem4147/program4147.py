    from collections import Counter
    
def sub(seq):
        if not seq:
            return seq
    
        M = [None] * len(seq)    # offset by 1 (j -> j-1)
        P = [None] * len(seq)
        L = 1
        M[0] = 0
        for i in range(1, len(seq)):
            lower = 0
            upper = L
            if seq[M[upper-1]] <= seq[i]:
                j = upper
    
            else:
                while upper - lower > 1:
                    mid = (upper + lower) // 2
                    if seq[M[mid-1]] <= seq[i]:
                        lower = mid
                    else:
                        upper = mid
    
                j = lower    # this will also set the default value to 0
    
            P[i] = M[j-1]
    
            if j == L or seq[i] < seq[M[j]]:
                M[j] = i
                L = max(L, j+1)
        result = []
        pos = M[L-1]
        for _ in range(L):
            result.append(seq[pos])
            pos = P[pos]
    
        return result[::-1]    # reversing
    
    
    s=input('')
    a=s.split(" ")
    n=int(a[0])
    t=int(a[1])
    s=input('')
    a=s.split(" ")
    arr=[]
    for i in range(0,n):
        arr.append(int(a[i]))
        
    m=min(t,n)
    ar=[]
    for i in range(0,m):
        for j in range(0,n):
            ar.append(arr[j])
    x=len(sub(ar))
    #print(ar)
    
    #print(sub(ar))
    m=t-m
    
    data = Counter(arr)
    #c1=data.most_common()   # Returns all unique items and their counts
    c2=data.most_common(1)  # Returns the highest occurring item
    c=c2[0][1]
    print(x+m*c)