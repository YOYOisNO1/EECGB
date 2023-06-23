    cnt=0
def powerSet(string,index,curr):
        global cnt
        if(index==len(string)):
           if(curr=="QAQ"):
               cnt+=1
           return
        powerSet(string,index+1,curr+string[index])
        powerSet(string,index+1,curr)
    if(__name__=='__main__'):
        s1=input()
        index=0
        curr=""
        powerSet(s1,index,curr)
        print(cnt)