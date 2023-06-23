    import math
    cnt=0
    st=""
    from itertools import combinations 
def powerset(string):
        global cnt
        for i in range(0,len(string)+1):
            for element in combinations(string,i):
                if(''.join(element)=="QAQ"):
                    cnt+=1
def powerSet(arr, n) :
        global cnt
        global st
        opsize = math.pow(2, n)
        for counter in range( 1, (int)(opsize)) :
            st=""
            for j in range(0, n) : 
                if (counter & (1<<j)) :
                    st+=arr[j]
                    print(st)
                    if(st=="QAQ"):
                        cnt+=1
    if(__name__=='__main__'):
        s1=input()
        index=0
        curr=""
        powerset(s1)
        print(cnt)