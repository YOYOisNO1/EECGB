    import sys
    import bisect
    #input=sys.stdin.readline
    #t=int(input())
def takeSecond(elem):
        return elem[1]
    
def gcd(a,b): 
        if (b == 0): 
             return a 
        return gcd(b, a%b)    
    
def solve(i1,j1):
        cnt3=0
        y=ord(s[i1])
        if (y>=65 and y<=90) or ( y>=97 and y<=122):
            cnt3=1
        for i2 in range(i1,j1):
            if s[i2]=='_' and (s[i2+1]!='_' and s[i2+1]!=')'):
                cnt3+=1
        
        y=ord(s[j1])
        if (y>=65 and y<=90) or ( y>=97 and y<=122):
            cnt3+=1
            
        return cnt3    
            
    t=1
    for _ in range(t):
        n=int(input())
        #l=list(map(int,input().split()))
        s=input()
        ans1,cnt1=0,0
        ans2=0
        ch=0
        
        for i in range(n):
            x=ord(s[i])
            if s[i]=='(':
                ch+=1
            if s[i]==')':
                ch-=1
            if ((x>=65 and x<=90) or (x>=97 and x<=122)) and ch==0:
                cnt1=1
                for j in range(i+1,n):
                    x=ord(s[j])
                    if (( x>=65 and x<=90) or ( x>=97 and x<=122)):
                        cnt1+=1
                    else:
                        break
                ans1=max(ans1,cnt1)
        i=0
        while i<n:
            if s[i]=='(':
                j=i+1
                while 1:
                    x=ord(s[j])
                    
                    if s[j]==')':
                        ans2+=solve(i+1,j)
                        #print(112,solve(i+1,j),i+1,j,s[i+1])
                        break
                    j+=1
                i=j    
            i+=1    
        print(ans1,ans2)        