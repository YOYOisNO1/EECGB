    # To change this template, choose Tools | Templates
    # and open the template in the editor.
    __author__="yaroslav"
    __date__ ="$02.08.2011 18:00:13$"
    import math
    
def resheto(num):
        arr = []
        for i in range(1,num/2):
            arr.append(i+1)
    
        for i in range(0,int(math.sqrt(num))):
            if arr[i]!=0:
                for j in range(2*arr[i]-2,(num/2)-1,arr[i]):
                    arr[j]=0
    
        arr2 = []
        for i in range(0,(num/2) - 1):
            if arr[i]!=0:
                arr2.append(arr[i])
    
        kol = 0
        for i in range(0,len(arr2)-1):
            for j in range(i+1,len(arr2)):
                x1 = arr2[i]
                x2 = arr2[j]
                did=0
                while x1*x2<=num:
                    kol+=1
                    x1 *= x1
                    did = 1
                x1 = arr2[i]
                x2 = arr2[j]
    
                while x1*x2<=num:
                    kol+=1
                    x2 *= x2
                    if did==1:
                        did=2
                if did == 2:
                    kol -= 1
    
        return kol
    
    if __name__ == "__main__":
        num = int(input())
        print resheto(num)