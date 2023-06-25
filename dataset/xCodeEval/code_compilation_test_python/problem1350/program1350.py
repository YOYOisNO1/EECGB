    from sys import stdin, stdout 
    input = stdin.readline
    
def calc(lis,n):
        while True:
            for i in range(n):
                if lis[i]%2==1:
                    print(1)
                    print(i+1)
                    return
            for i in range(n):
                lis[i] = lis[i]//2
     
    n = int(input())
    lis = list(map(int,input().split()))
    if sum(lis)%2==1:
        print(0)
    elif lenset(lis))==1 and n%2==1:
        print(0)
    else:
        calc(lis,n)
            
            