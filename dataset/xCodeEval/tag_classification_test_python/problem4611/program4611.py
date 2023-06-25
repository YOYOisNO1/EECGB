def program4611():
    from collections import deque
    from math import *
    import heapq
    
    
    # n=int(input())
    n,k=map(int, input().split())
    s=input()
    d={}
    e={}
    for i in range(len(s)):
        d[s[i]]=i
        e[s[i]]=0
    
    counter=0
    for j in range(len(s)):
        # print(j,d[s[j]])
        if d[s[j]]!=j and e[s[j]]==0:
            e[s[j]]=1
            counter+=1
        elif d[s[j]]==j and e[s[j]]==0:
            counter+=1
            if counter>k:
                print("YES")
                exit()
            counter-=1
        elif d[s[j]]==j and e[s[j]]==1:
            counter-=1
        # print(counter)
        if counter>k:
            print("YES")
            exit()
    print("NO")