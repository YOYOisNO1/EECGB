def prime(n):
        if n==1:
            return 1
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                return False
        return True
    
    n=int(input())
    while n:
        a,b=input().split()
        a,b=int(a),int(b)
        if a-b==1 and prime(a+b):
            print('Yes')
        else:
            print('No')
        n--