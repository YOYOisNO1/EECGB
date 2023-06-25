    #from collections import Counter as C
    
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    
    
    maxWin=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    
    
    
    
def dfs(remainingTotal,remainingCombinations):
        if len(remainingCombinations)==0:
    #        print(remainingTotal)#
            minWins.append(sum(remainingTotal[:3]))
            return
        for i in range(len(remainingCombinations)):
            remainingCombinations2=remainingCombinations.copy()
            remainingTotal2=remainingTotal.copy()
            x,y=remainingCombinations2.pop(i)
            subtract=min(remainingTotal2[x],remainingTotal2[y])
            remainingTotal2[x]-=subtract
            remainingTotal2[y]-=subtract
            dfs(remainingTotal2,remainingCombinations2)
    
    arr=a+b #[a1,a2,a3,b1,b2,b3]
    combinations=[(0,3),(0,5),(1,4),(1,3),(2,5),(2,4)]
    minWins=[]
    dfs(arr,combinations)
    
    minWin=min(minWins)
    #print(minWins)
    #print(len(minWins))
    print('{} {}'.format(minWin,maxWin))