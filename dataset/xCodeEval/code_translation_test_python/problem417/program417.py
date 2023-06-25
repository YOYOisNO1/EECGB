    time = input()
    
def toStr(num):
        s = str(num)
        return "0" * (2 - len(s)) + s
    
def rev(s):
        return s[::-1]
    
def isValid(time):
        h, m = time.split(":")
        return int(h) >= 0 and int(h) < 24 and int(m) >= 0 and int(m) < 60
    
def getNext(time):
        h, m = time.split(":")
        palindrome = h + ":" + rev(h)
        if isValid(palindrome) and int(rev(h)) > int(m):
            return palindrome
        elif h == "23":
            return "00:00"
        else:
            return getNext(toStr(int(h) + 1) + ":00")
    
    print(getNext(time))