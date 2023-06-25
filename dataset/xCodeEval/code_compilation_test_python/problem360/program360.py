    
    problemList = []
    n = 0
    k = 0
    
def RecurseFind(l:int, r:int):
        if l==r:
            if problemList[l]<=k:
                return 1
            return 0
    
        ret = 0
        retLeft = 0
        retRight = 0
    
        if problemList[l]<=k:
            retLeft = 1 + RecurseFind(l+1, r)
        if problemList[r]<=k:
            retRight = 1 + RecurseFind(l,r-1)
    
        ret = max(retLeft, retRight)
    
        return ret
    
    if __name__ == "__main__":
    
        n,k = map(int,input().split())
        #k = input()
        n = int(n)
        k = int(k)
    
        i = 0
        # while i<n:
        #     tmp = input()
        #     tmp = int(tmp)
        #     problemList.append(tmp)
        #     i+=1
        problemList = list(map(int,input().split()))
        #print(problemList)
    
        result = RecurseFind(0, len(problemList)-1)
        print(result)
        #print(problemList)