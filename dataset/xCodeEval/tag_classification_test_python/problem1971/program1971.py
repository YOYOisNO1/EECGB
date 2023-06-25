    import sys, math
    input = sys.stdin.readline
    
def getInts():
        return [int(s) for s in input().split()]
    
def getInt():
        return int(input())
    
def getStrs():
        return [s for s in input().split()]
    
def getStr():
        return input().strip()
    
def listStr():
        return list(input().strip())
    
    import collections as col
    import math
    
def solve2(ingreds,full_burgers,one_cost,R):
        #print(ingreds)
        #the case where they're all zero
        if ingreds[2][0] == 0:
            #cost to reach next integer is
            I0, I1, I2 = ingreds
            R -= (I0[2]-I0[1])*I0[3] + (I1[2]-I1[1])*I1[3] + (I2[2]-I2[1])*I2[3]
            if R < 0:
                return full_burgers
            full_burgers += 1 + R//one_cost
            return full_burgers
        
        #the case where the first two are 0
        if ingreds[1][0] == 0:
            I0, I1, I2 = ingreds[0], ingreds[1], ingreds[2]
            R -= (I0[2]-I0[1])*I0[3] + (I1[2]-I1[1])*I1[3]
            if R < 0:
                return full_burgers
            full_burgers += 1
            ingreds[0], ingreds[1], ingreds[2] = [0,0,I0[2],I0[3]], [0,0,I1[2],I1[3]], [I2[0]-1,I2[1]-I2[2],I2[2],I2[3]]
            I0, I1, I2 = ingreds[0], ingreds[1], ingreds[2]
            #target is first to reach ingreds[2][0] burgers
            cost_R = I2[0]*(I1[2]*I1[3]+I0[2]*I0[3])
            if R >= cost_R:
                R -= cost_R
                full_burgers += I2[0]
            else:
                full_burgers += R//(I1[2]*I1[3]+I0[2]*I0[3])
                return full_burgers
            ingreds = [[0,0,I0[2],I0[3]], [0,0,I1[2],I1[3]], [0,I2[1]%I2[2],I2[2],I2[3]]]
            return solve2(ingreds,full_burgers,one_cost,R)
        
        #the case where ingreds[1][0] > 0
        #print(full_burgers,ingreds,one_cost,R)
        I0, I1, I2 = ingreds[0], ingreds[1], ingreds[2]
        cost = (I0[2]-I0[1])*I0[3]
        if cost > R:
            return full_burgers
        R -= cost
        full_burgers += 1
        ingreds[0], ingreds[1], ingreds[2] = [0,0,I0[2],I0[3]], [I1[0]-1,I1[1]-I1[2],I1[2],I1[3]], [I2[0]-1,I2[1]-I2[2],I2[2],I2[3]]
        #print(full_burgers,ingreds,R)
        I0, I1, I2 = ingreds[0], ingreds[1], ingreds[2]
        cost = I1[0]*I0[2]*I0[3]
        if R >= cost:
            R -= cost
            full_burgers += I1[0]
        else:
            full_burgers += R//(I0[2]*I0[3])
            return full_burgers
        ingreds[0], ingreds[1], ingreds[2] = [0,0,I0[2],I0[3]], [0,I1[1]%I1[2],I1[2],I1[3]], [I2[0]-I1[0],I2[1]-I2[2]*I1[0],I2[2],I2[3]]
        return solve2(ingreds,full_burgers,one_cost,R)
    
def solve3(ingreds,full_burgers,R):
        I0, I1 = ingreds
        #I0[0] = 0 and I1[0] = 0
        if I1[0] == 0:
            cost = (I0[2]-I0[1])*I0[3]+(I1[2]-I1[1])*I1[3]
            if cost > R:
                return full_burgers
            full_burgers +=1
            R -= cost
            ingreds = [[0,0,I0[2],I0[3]],[0,0,I1[2],I1[3]]]
            I0, I1 = ingreds
            cost = I0[2]*I0[3]+I1[2]*I1[3]
            return full_burgers + R//cost
        #I0[0] = 0 and I1[0] > 0
        cost = (I0[2]-I0[1])*I0[3]
        if cost > R:
            return full_burgers
        full_burgers += 1
        R -= cost
        ingreds = [[0,0,I0[2],I0[3]],[I1[0]-1,I1[1]-I1[2],I1[2],I1[3]]]
        cost = I0[2]*I0[3]
        if cost*I1[0] > R:
            return full_burgers + R//cost
        full_burgers += I1[0]
        R -= cost*I1[0]
        cost = I0[2]*I0[3] + (I1[2]-I1[1])*I1[3]
        if cost > R:
            return full_burgers
        full_burgers += 1
        R -= cost
        ingreds = [[0,0,I0[2],I0[3]],[0,0,I1[2],I1[3]]]
        return solve3(ingreds,full_burgers,R)
    
def solve():
        burger = listStr()
        NB, NS, NC = getInts()
        PB, PS, PC = getInts()
        R = getInt()
        B, S, C = burger.count('B'), burger.count('S'), burger.count('C')
        ingreds = [[NB//B if B > 0 else 0,NB,B,PB],[NS//S if S > 0 else 0,NS,S,PS],[NC//C if C > 0 else 0,NC,C,PC]]
        ingreds.sort(key = lambda x: x[2])
        if ingreds[1][2] == 0:
            NB, B, PB = ingreds[2][1:]
            full_burgers = NB//B
            NB %= B
            cost = (B-NB)*PB
            if cost > R:
                return full_burgers
            R -= cost
            full_burgers += 1
            return full_burgers + R//(B*PB)
        if ingreds[0][2] == 0:
            ingreds = ingreds[1:]
            I0, I1 = ingreds
            full_burgers = I0[0]
            ingreds = [[0,I0[1]%I0[2],I0[2],I0[3]],[I1[0]-I0[0],I1[1]-I0[0]*I1[2],I1[2],I1[3]]]
            return solve3(ingreds,full_burgers,R)
        assert(B+S+C==len(burger))
        ingreds = [[NB//B,NB,B,PB],[NS//S,NS,S,PS],[NC//C,NC,C,PC]]
        ingreds.sort()
        full_burgers = ingreds[0][0]
        NB -= B*full_burgers
        NS -= S*full_burgers
        NC -= C*full_burgers
        ingreds = [[NB//B,NB,B,PB],[NS//S,NS,S,PS],[NC//C,NC,C,PC]]
        ingreds.sort()
        one_cost = B*PB + S*PS + C*PC
    
        #now we have 0 of the minimum ingredient, and some non-negative amount of the other two ingredients
    
        #if they're all zero, get them all up to 1, then as far as possible
        #if two of them are zero, get those up to 1, then as far as possible towards the third integer, then (if still going) one more, then as far as possible
        #if just one is zero, get that as close to the value of the second, if we reach it, then one more, then as close to the value of the third, then one more,
        #then as far as possible
        #print(full_burgers,ingreds,R,one_cost)
        return solve2(ingreds,full_burgers,one_cost,R)
        
        
        
                
            
    #for _ in range(getInt()):
    print(solve())
        
    