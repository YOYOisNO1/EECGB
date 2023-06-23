    a, b, c = input().split(' ')
    
    note = ['C','C#','D','D#','E','F','F#','G','G#','A','B','H']
    
def diff(str1, str2):
        for i in range[note]:
            if (note[i] == str1):
                x = i
            if (note[i] == str2):
                y = i
            if (x < y):
                return y - x
            else:
                if (y < x):
                    return 12 - y + x
        return 0
    
    one = diff(a, b)
    two = diff(b, c)
    if ((one == 3) | (two == 4)):
        print "minor"
    else:
        if ((one == 4) | (two == 3)):
            print "major"
        else:
            print "strange" 
        