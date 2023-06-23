    rows, groups = map(int, input().split())
    soldiers=list(map(int, input().split()))
def makePlane(rows):
        plane=[int(rows),2*int(rows),0]
        return(plane)
def rozdelitVojaky(soldiers):
        ctyrky,dvojky,jednicky=0,0,0
        for skupina in soldiers:
            skupina=int(skupina)
            while skupina>=4:
                ctyrky+=1
                skupina-=4
            if skupina>=2:
                dvojky+=1
            if skupina%2==1:
                jednicky+=1
        return([ctyrky,dvojky,jednicky])
def zjistit(rows,groups,soldiers):
        plane=makePlane(rows)
        pasazeri=rozdelitVojaky(soldiers)
    
        #usadit ctverice
        if pasazeri[0]<=plane[0]:
            plane[0]-=pasazeri[0]
            pasazeri[0]=0
        else:
            pasazeri[0]-=plane[0]
            pasazeri[1]+=2*pasazeri[0]
            plane[0]=0
    
        #dvojicky
        #do ctyrmist
        if pasazeri[1]<=plane[0]:
            plane[0]-=pasazeri[1]
            plane[2]+=pazazeri[1]
            pasazeri[1]=0
        else:
            pasazeri[1]-=plane[0]
            plane[2]+=plane[0]
            plane[0]=0
            #do dvojmist
            if pasazeri[1]<=plane[1]:
                plane[1]-=pasazeri[1]
                pasazeri[1]=0
            else:
                pasazeri[1]-=plane[1]
                pasazeri[2]+=2*pasazeri[1]
                plane[1]=0
        #jednotlivci
        pasazeri[2]=pasazeri[2]-2*plane[0]-plane[1]-plane[2]
        if pasazeri[2]<=0:
            return("YES")
        else:
            return("NO")
    
                
    print(zjistit(rows,groups,soldiers))
                