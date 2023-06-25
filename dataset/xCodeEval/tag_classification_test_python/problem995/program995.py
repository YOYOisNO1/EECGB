def program995():
    n=int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    
    
    
    mini=0
    for i in range(3):
        if A[i]>=B[i]+B[i-1]:
            mini=A[i]-(B[i]+B[i-1])
        if B[i]>=A[i]+A[i-2]:
            mini=B[i]-(A[i]+A[i-2])
    
    print(mini,min(A[0],B[1])+min(A[1],B[2])+min(A[2],B[0]))