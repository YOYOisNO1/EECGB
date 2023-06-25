    
    Input=lambda:map(int,input().split())
    
def cal(num):
        s = bin(num)
        s = s.replace("0b","")
        k = len(s)
        #print(s,k)
        #print(set(s[:k//2+1]),set(s[k//2+1:]))
        if k%2!= 0 and s[:k//2+1] == "1"*(k//2+1) and s[k//2+1:] == '0'*(k-(k//2+1)) :
            return True
        else:
            return False
    
def divisor(n):
        yield n
        yield n//2
        n//=2
        while n!=0:
            n-=1
            yield n
    
    
    n = int(input())
    
    for i in divisor(n):
        if n%i==0:
            
            if cal(i):
                print(i)
                break