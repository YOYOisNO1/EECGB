    nums = [int(i) for i in input().split()]
    a, b = nums
    
def counter(n,m):
        count = 0
        if m%2:
            count+=1
            m+=1
        while m!=n:
            if m > n:
                if m%2==0:
                    m//=2
                else:
                    m+=1
                count+=1
            else:
                count+=n-m
                m=n
        return count
    
    print(counter(a,b))
                
        