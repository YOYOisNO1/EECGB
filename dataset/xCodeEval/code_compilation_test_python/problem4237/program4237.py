    #from math import ceil, floor #, gcd, log, factorial, comb, perm,
    #log10, log2, log, sin, asin, tan, atan, radians
    #from heapq import heappop,heappush,heapify #heappop(hq), heapify(list)
    #from collections import defaultdict as dd
    #mydd=dd(list) for .append
    #from collections import deque as dq #deque  e.g. myqueue=dq(list)
    #append/appendleft/appendright/pop/popleft
    #from bisect import bisect as bis #a=[1,3,4,6,7,8] #bis(a,5)-->3
    #import bisect #bisect.bisect_left(a,4)-->2 #bisect.bisect(a,4)-->3
    #import statistics as stat  # stat.median(a), mode, mean
    #from itertools import permutations(p,r)#combinations(p,r)
    #combinations_with_replacement#combinations(p,r) gives r-length tuples,
    #in sorted order, with repeated elements#product gives outer product combos
    import sys
    input = sys.stdin.readline
    #print = sys.stdout.write
    #sys.setrecursionlimit(100000) #default is 1000 
    ############ ---- Input Functions ---- ############
def inp():
        return(int(input()))
def inlt():
        return(list(map(int,input().split())))   #.split(','), default is space
    #list([0,*map(int,input().split(" "))]) # pad a zero to avoid zero indexing
def insr():
        s = input()
        return(list(s[:len(s) - 1]))
    ####################################################
    t=1
    #t = int(input())
    for tc in range(t):
        p1,t1=map(int, input().split())
        p2,t2=map(int, input().split())
        h,s=map(int, input().split())
        if t2<t1: p1,t1,p2,t2=p2,t2,p1,t1
    #    n=inp()
    #    a=inlt()
    #    x=list(input().strip("\n").split())
    #    s=input().strip("\n")
    #    s=input()[:-1]
    #    s=insr()
    #    occ=dd(list) #dd(int)
    #    occ=dict();
    #    for i in range(n):occ[i]=[]
    #    for i in range(n):
    #        occ[i].append(inlt())
    #    a=[]
    #    for i in range(n):
    #        a.append(inlt())
        if (p1)/(t2%t1+t1)>(p1-s)/t1:#wait
            
        else:#don't wait
            d=(p1-s)/t1+(p2-s)
        ans=0
        print(ans)
        
    #print(*ans,sep=' ')##print("{:.3f}".format(ans)+"%")
    #:b binary :% eg print("{:6.2%}".format(ans))
    #print(" ".join(str(i) for i in ans))
    #print(" ".join(map(str,ans))) #seems faster
    #print(a[0] if a else 0)
    #prefixsum a=[a1...an] #psa=[0]*(n+1)
    #for i in range(n): psa[i+1]=psa[i]+a[i]
    #sum[:ax]=psa[x+1] e.g. sum 1st 5 items in psa[5]
    #ASCII<->number ord('f')=102 chr(102)='f'
#def binary_search(li, val, lb, ub):
    #    while ((ub-lb)>1):
    #        mid = (lb + ub) // 2
    #        if li[mid] >= val:
    #            ub = mid
    #        else:
    #            lb = mid
    #    return lb+1 #return index of elements <val in li
#def binary_search(li, val, lb, ub):
    #    ans = -1
    #    while (lb <= ub):
    #        mid = (lb + ub) // 2
    #        if li[mid] > val:
    #            ub = mid - 1
    #        elif val > li[mid]:
    #            lb = mid + 1
    #        else:
    #            ans = mid  # return index
    #            break
    #    return ans
    ##########
#def pref(li):
    #    pref_sum = [0]
    #    for i in li:
    #        pref_sum.append(pref_sum[-1] + i)
    #    return pref_sum
    ##########
#def suff(li):
    #    suff_sum = [0]
    #    for i in range(len(li)-1,-1,-1):
    #        suff_sum.insert(0,suff_sum[0] + li[i])
    #    return suff_sum
    #############
#def maxSubArraySumI(arr): #Kadane's algorithm with index
    #    max_till_now=arr[0];max_ending=0;size=len(arr)
    #    start=0;end=0;s=0
    #    for i in range(0, size):
    #        max_ending = max_ending + arr[i]
    #        if max_till_now < max_ending:
    #            max_till_now=max_ending
    #            start=s;end=i
    #        if max_ending<0:
    #            max_ending=0
    #            s=i+1
    #    return max_till_now,start,end
    ############# avoid max for 2 elements - slower than direct if
#def maxSubArraySum(arr): #Kadane's algorithm
    #    max_till_now=arr[0];max_ending=0;size=len(arr)
    #    for i in range(0, size):
    #        max_ending = max_ending + arr[i]
    #        if max_till_now < max_ending:max_till_now=max_ending
    #        if max_ending<0:max_ending=0
    #    return max_till_now
    #############
#def findbits(x):
    #    tmp=[]
    #    while x>0:tmp.append(x%2);x//=2
    #    tmp.reverse()
    #    return tmp
    ##############Dijkstra algorithm example
    #dg=[999999]*(n+1);dg[n]=0;todo=[(0,n)];chkd=[0]*(n+1)
    #while todo:#### find x with min dg in todo
    #    _,x=hq.heappop(todo)
    #    if chkd[x]:continue
    #    for i in coming[x]:going[i]-=1
    #    for i in coming[x]:
    #        tmp=1+dg[x]+going[i]
    #        if tmp<dg[i]:dg[i]=tmp;hq.heappush(todo,(dg[i],i))   
    #    chkd[x]=1
    ################ 
    # adj swaps to match 2 binary strings: sum_{i=1}^n(abs(diff in i-th prefix sums))
    ###############
    ##s=[2, 3, 1, 4, 5, 3]
    ##sorted(range(len(s)), key=lambda k: s[k])
    ##gives sorted indices [2, 0, 1, 5, 3, 4]
    ##m= [[3, 4, 6], [2, 4, 8], [2, 3, 4], [1, 2, 3], [7, 6, 7], [1, 8, 2]]
    ##m.sort(reverse=True,key=lambda k:k[2]) #sorts m according to 3rd elements
    #import bisect  #li = [1, 3, 4, 4, 4, 6, 7]#sorted li, use b search, so log(n)
    #bisect.bisect(li,4)-->5 #bisect.bisect_left(li,4)-->2
    ###############
##def chkprime(x):
    ##    if x==2 or x==3:return True
    ##    if x%2==0 or x<2:return False
    ##    for i in range(3,int(x**0.5)+1,2):
    ##        if x%i==0:return False
    ##    return True
    ############### two factoring functions, seems to have the same performance
##def factors(n):
    ##    f=[];t=2
    ##    while n>1:
    ##        if n%t==0:
    ##            f.append(t);n//=t;t=2
    ##        else:
    ##            t+=1
    ##            if t*t>n:f.append(n);break
    ##    return f
    ##################
##def factors(n):
    ##    f=[]
    ##    while n > 1:
    ##        for i in range(2, int((n+0.02)**0.5)+1):
    ##            if n%i==0:f.append(i);n//=i;break
    ##        else:
    ##            f.append(n);n=1
    ##    return f