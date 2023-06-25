    from itertools import permutations
    n=int(input())
    a,b,c=list(map(int,input().split()))
    x,y,z=list(map(int,input().split()))
    maxi=min(a,y)+min(b,z)+min(c,x)
def solve(p,q):
        temp=min(p,q)
        p-=temp
        q-=temp
        return p,q
    lis=permutations([0,1,2,3,4,5])
    mini=maxi
    for num in lis:
        arr1=[a,b,c]
        arr2=[x,y,z]
        arr=[[0,0],[0,2],[1,1],[1,0],[2,2],[2,1]]
        for i in range(6):
            arr1[arr[num[i]][0]],arr2[arr[num[i]][1]]=solve(arr1[arr[num[i]][0]],arr2[arr[num[i]][1]])
        mini=min(mini,(sum(arr1)+sum(arr2))//2)
    print(mini,maxi)