    s = [input() for _ in xrange(10)]
    
def horizontal(s):
        for i in xrange(10):
            for j in xrange(6):
                x = 0
                for k in xrange(5):
                    if s[i][j+k] == "O":
                        break
                    if s[i][j+k] == ".":
                        x += 1
                        if x > 1:
                            break
                    if k == 4:
                        return True
    
def vertical(s):
        for i in xrange(10):
            for j in xrange(6):
                x = 0
                for k in xrange(5):
                    if s[j+k][i] == "O":
                        break
                    if s[j+k][i] == ".":
                        x += 1
                        if x > 1:
                            break
                    if k == 4:
                        return True
    
def diagonal1(s):
        for i in xrange(6):
            for j in xrange(6):
                x = 0
                for k in xrange(5):
                    if s[i+k][j+k] == "O":
                        break
                    if s[i+k][j+k] == ".":
                        x += 1
                        if x > 1:
                            break
                    if k == 4:
                        return True
    
def diagonal2(s):
        for i in xrange(4,10):
            for j in xrange(6):
                x = 0
                for k in xrange(5):
                    if s[i-k][j+k] == "O":
                        break
                    if s[i-k][j+k] == ".":
                        x += 1
                        if x > 1:
                            break
                    if k == 4:
                        return True              
    
    print("YES") if any((horizontal(s), vertical(s), diagonal1(s), diagonal2(s))) else "NO"