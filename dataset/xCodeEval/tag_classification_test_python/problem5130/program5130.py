    """
    Created on Wed Feb 22 20:11:58 2017
    
    Name: MD. Khairul Basar
    Phone: 01760446942
    Email: khairul.basar93@gmail.com
    """
    
def bit_length(x):
        
        ans = 0;
        while(x):
            ans+=1;
            x = x//2;
        return max(ans,1);
    
def solve(x,pos,size,l,r):
        
        if(x <= 1):
            return x;
        
        ans = 0;
        if(l < pos):
            ans+=solve(x//2,pos-size,size//2,l,r);
        if(pos>=l and pos<=r):
            ans+=x%2;
        if(r > pos):
            ans+=solve(x//2,pos+size,size//2,l,r);
    
        return ans;
    
    n,l,r = map(int,input().split());
    length = bit_length(n);
    x = 1<<(length-1);
    ans = solve(n,x,x//2,l,r);
    print(ans);