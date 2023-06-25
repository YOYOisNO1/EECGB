def solution():
        a = [int(x) for x in input().split()]
        d = a[0]
        sumtime = a[1]
        time = []
        i=0
        possible,final=[],[]
        while i<d:
            b = [int(x) for x in input().split()]
            possible.append(b[0])
            final.append(b[1])
            i+=1
        i=0
        smalls=possible.copy()
        if sum(final)<sumtime or sum(possible)>sumtime: return "NO"
    
        while i<len(possible):
            j=0
            while sum(possible)<sumtime and j<len(possible):
                possible[j]=final[(j)]
                j+=1
            if sum(possible)==sumtime:
                break
            if sum(possible)>sumtime:
                #print("HEOORE")
                targ = sum(possible)-sumtime
                l =0
                finals=[]
                while l<len(smalls):
                    finals.append(final[l]-smalls[l])
                    l+=1
                k=0
                done = 0
                #print(smalls,final,possible,targ)
                #print(finals)
                while k<len(finals):
                    if finals[k]>=targ:
                        possible[k]-=targ
                        done = 1
                        break
                    k+=1
                if done: break
            i+=1
        c_out=""
        for x in possible:
            c_out+=str(x)+" "
        print("YES")
        return c_out
    
    
    print(solution())