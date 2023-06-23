    import sys
    import time
def remplacerParDiff(lt,i,j,n):
        #print(lt[i],"  ",lt[j])
        if(lt[i]=='B' and lt[j]=='G'):diff='R'
        if(lt[i]=='B' and lt[j]=='R'):diff='G'
        if(lt[i]=='R' and lt[j]=='G'):diff='B'
        if(lt[i]=='R' and lt[j]=='B'):diff='G'
        if(lt[i]=='G' and lt[j]=='R'):diff='B'
        if(lt[i]=='G' and lt[j]=='B'):diff='R'
        t=[None] * (n-1)
        for k in range(0,j):
            if k==i:
                t[k]=diff 
            else:
                t[k]=lt[k]
    
        for k in range(j+1,n):
            t[k-1]=lt[k]
        catherine(t,n-1);
    
def remplacerParSim(lt,i,j,n):
        sim=lt[i]
        t=[None] * (n-1)
        for k in range(0,j):
            if k==i:
                t[k]=sim 
            else:
                t[k]=lt[k]
    
        for k in range(j+1,n):
            t[k-1]=lt[k]
        catherine(t,n-1);
    
def catherine(t,n):
        if n == 1:
            last_chars.append(t[0])
            #print(t[0])
        else:
            #print(t)
            for i in range(0,n-1):
                for j in range(i+1,n):
                    if t[i]==t[j]:
                        #print("t[",i,"]= ",t[i],"\n")
                        #print("t[",j,"]= ",t[j],"\n")
                        #print("remplacerParsim\n")
                        remplacerParSim(t,i,j,n)
                    else:
                        #print("t[",i,"]= ",t[i],"\n")
                        #print("t[",j,"]= ",t[j],"\n")
                        #print("remplacerParDiff\n")
                        remplacerParDiff(t,i,j,n)
                        
    
def main():
    
        try:
            n=int(input())
            
        except ValueError:
            #print "Not a number"
        try:
            t=str(input())
            
        except ValueError:
            #print "Not a string"
    
        start_time = time.time()
        catherine(list(t),list(t).__len__())
        #print("--- %s seconds ---" % (time.time() - start_time))
        print(''.join(list(set(last_chars))))
    last_chars=[]
    if __name__ == "__main__":
        
        main()
        