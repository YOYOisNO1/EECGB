def main():
        a,n=map(int,input().strip().split())
    
        q=a%n
        r=0
    
        while r<=n:
            q=(2*q)%n
            if q==0:return True
            r+=1
        return False
    
    if main():print "Yes"
    else:print "No