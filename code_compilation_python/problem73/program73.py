def program73():
    
    import sys
    from os import path
    if(path.exists('input.txt')):
        sys.stdin = open("input.txt","r")
        sys.stdout = open("output.txt","w")
    sys.setrecursionlimit(10**6)
    
    
    test_case=int(input())
    for i in range(test_case):
        first_key=int(input())
        arr=[int(x) for x in input().split()]
        ans=[first_key]
        for j in range(3):
            if arr[ans[-1]-1]!=0:
                ans.append(arr[ans[-1]-1])
            else:
                break
        if len(ans)==3:
            print("YES")
        else:
            print("NO")