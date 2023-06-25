    import sys
    import  random
    
    input = sys.stdin.readline
    
    
def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    
def lcm(a, b):
        return (a * b) / gcd(a, b)
    
def main():
        # a=random.randint(1,100)
        # b=random.randint(1,100)
        a,b=map(int, input().split())
        k=min(a,b)
        t=max(a,b)
        a=k
        b=t
        #print(a,b)
        k=float('inf')
        ind=0
        i=1
        divs=[]
        while(i*i<=(b-a)):
            if (b-a)%i==0:
                divs.append(i)
                divs.append((b-a)//i)
            i+=1
        divs.sort()
        for i in divs:
            if a%i==b%i:
                if a%i==0:
                    if k>lcm(a,b):
                        k=lcm(a,b)
                        ind=0
                else:
                    if k>lcm(i-a%i+a,i-b%i+b):
                        k=lcm(i-a%i+a,i-b%i+b)
                        ind=i-a%i
        print(ind)
        return
    
    if __name__=="__main__":
        main()
    