    from collections import Counter
    import string
    import math
    import sys
def array_int():
        return [int(i) for i in sys.stdin.readline().split()]
def vary(number_of_variables):
        if number_of_variables==1:
            return int(sys.stdin.readline())
        if number_of_variables>=2:
            return map(int,sys.stdin.readline().split()) 
def makedict(var):
        return dict(Counter(var))
    mod=100000007
    # sys.stdin=open('input.txt','r')
    # sys.stdout=open('output.txt','w')
    dic={'1':'','0':'','2':'2','3':'3','4':'322','5':'5','6':'53','7':'7','8':'7222','9':'7332'}
    n=vary(1)
    num=input()
    ans=''
    for i in num:
        ans+=dic[i]
    ans=list(ans)
    ans.sort(reverse=True)
    for i in ans:
        print(i,end="")
    
    
        
    
    
        
    
    
        
    
    
    