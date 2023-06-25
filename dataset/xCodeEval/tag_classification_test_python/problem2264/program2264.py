    class NextRound:
    def sovle(self,n,k,numList):
            result = 0
            for i in numList:
                if(i>0 and i>=numList[k-1]):
                    result+=1
            return result
            
            
            
    
    if __name__ == "__main__":
        
        numList = list()
        n,k = map(int,input().split(" "))
        numList = map(int,input().split(" "))
        nr = NextRound()
        print(nr.sovle(n,k,numList))