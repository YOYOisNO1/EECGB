def program403():
    n,a,b,c = map(int,input().split())
    mat = [0]+[-10000]*5000
    for i in range(1,n+1):
        mat[i] = max(mat[i-a],mat[i-b],mat[i-c])+1
    print(mat[n])