    import fileinput
    import sys
    
def helper(trips, currentCombo, prevChar, string):
        if (len(string) == 0):
            sys.stdout.write("%d" % trips)
            return
        
        c = string[0];
        if prevChar != ' ': #if this is not the first character in the str
            if (c == prevChar): #same char as prev
                currentCombo += 1
                if ((currentCombo % 5) == 1):
                    trips += 1
            else:               #different char from prev
                currentCombo = 1
                trips +=1
    
        else:               #if this is the first character in the str
            trips = 1
            currentCombo = 1
    
        return helper(trips, currentCombo, c, string[1:])
        
    
    for line in fileinput.input():
        inputString = line; #get input
        output = helper(0, 0, ' ', inputString)