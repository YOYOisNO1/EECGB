def rpm(n):
        output={2:0, 3:0, 5:0, 10:0}
        for i in [2, 3, 5]:
            op=0
            while n%i==0:
                n//=i
                op+=1
            output[i]=op
        output[10]=n
        return output
    A, B=map(rpm, map(int, input().split()))
    if A[10]!=B[10]:
        print(-1)
    else:
        print(max(A[2],B[2])-min(A[2],B[2])+max(A[3],B[3])-min(A[3],B[3])+max(A[5],B[5])-min(A[5],B[5]))