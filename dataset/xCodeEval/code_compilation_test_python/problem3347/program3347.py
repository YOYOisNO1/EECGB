def gcd(x,y):
        r = x % y
        while r != 0:
            x = y
            y = r
            r = x % y
    
        return y
            
    
    
def go(command,now):
        if command == "U":
            return (now[0],now[1]+1)
        elif command == "D":
            return (now[0],now[1]-1)
        elif command == "R":
            return (now[0]+1,now[1])
        else:
            return (now[0]-1,now[1])
    
def same_hugo(x,y):
        if x < 0 and y < 0:
            return True
    
        if x > 0 and y > 0:
            return True
        
        if x == 0 and y == 0:
            return True
    
        return False
    
def solver():
        a,b = map(int, input().split())
        command = input()
        if (a,b) == (0,0):
            print "Yes"
            return
        sa = []
        now = (0,0)
        first = []
        for c in command:
            now = go(c,now)
            sa.append((a-now[0],b-now[1]))
            first.append(now)
            if now == (a,b):
                print "Yes"
                return
            
    
    
    
        for i in range(len(command)):
            now = go(command[i],now)
            temp_sa = sa[i]
            temp_first = first[i]
            sinpo = (now[0] - temp_first[0], now[1]-temp_first[1])
            #print temp_sa,sinpo,now,temp_first
            
            if temp_sa[0] == 0:
                if sinpo[0] == 0:
                    if temp_sa[1] == 0:
                        if sinpo[1] == 0:
                            print "Yes"
                            return
                    else:
                        if temp_sa[1] % sinpo[1] == 0:
                            if same_hugo(temp_sa[1],sinpo[1]):
                                print "Yes"
                                return
            elif temp_sa[1] == 0:
                if sinpo[1] == 0:
                    if temp_sa[0] % sinpo[0] == 0:
                        if same_hugo(temp_sa[0],sinpo[0]):
                            print "Yes"
                            return
            else:
                #print temp_sa
    
                num = abs(gcd(temp_sa[0],temp_sa[1]))
                if temp_sa[0]/num == sinpo[0] and temp_sa[1]/num == sinpo[1]:
                    print "Yes"
                    return
                
    
        print "No"
    
        
    
    if __name__ == "__main__":
        solver()
    