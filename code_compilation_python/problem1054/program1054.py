def program1054():
    n=int(input())
    s=input()
    check='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    op=[
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1],
        [2,1,0,1,2,3,4,5,6,7,8,9,10,12,12,13,12,11,10,9,8,7,6,5,4,3],
        [7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1,0,1,2,3,4,5,6],
        [6,5,4,3,2,1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7],
    ]
    ans=10**10
    for i in range(n-3):
        tmp=0
        for j in range(4):
            for k in range(26):
                if s[i+j]==check[k]:
                    tmp+=op[j][k]
        if tmp<ans:
            ans=tmp
    print(ans)