def program1867():
    s=input()
    a="aeiou"
    for i in range (len(s)-1):
        if (s[i] not in a and s[i]!='n' and s[i+1] not in a):
            print("NO")
            exit()
    if s[-1] not in a and s[-1]!='n':
        print("NO")
    else:
        print("YES")
    
    '''N=int(input())
    A=[]
    S="abcdefghijklmnopqrstuvwxyz"
    for i in range (N):
        n, k=[int(i) for i in input().split()]
        count=0
        while count<n:
            for l in range (k):
                A.append(S[l])
                count +=1
    print(*A, sep="", end="\n")'''